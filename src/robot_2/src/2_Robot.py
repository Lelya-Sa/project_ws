import threading
import time
import rospy
import actionlib
from geometry_msgs.msg import Pose
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
from collections import deque


class Robot:
    _id_counter = 0
    _id_lock = threading.Lock()

    def __init__(self, robot_name, action_name, storages, dispatches, order_controller):
        with Robot._id_lock:
            self._id = Robot._id_counter
            Robot._id_counter += 1

        self._object_name = f"{robot_name}#{self._id}"
        self._type = "objectRobot"
        self._storages = storages
        self._dispatches = dispatches
        self._order_controller = order_controller
        self._action_name = action_name
        self._status = "offline"
        self._cargo_bin_products = []
        self._cargo_bin_lock = threading.Lock()
        self._order = None
        self.threads = []
        rospy.loginfo(f"Robot {self._object_name} initialized.")

    def __del__(self):
        rospy.loginfo(f"Shutting down Robot {self._object_name}")
        self._status = "offline"

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status

    def get_cargo_bin_products_name(self):
        with self._cargo_bin_lock:
            return [p.get_name() for p in self._cargo_bin_products]

    def start_operation(self):
        if self._status == "offline":
            self._status = "startup"
            thread = threading.Thread(target=self._operate)
            thread.daemon = True
            self.threads.append(thread)
            thread.start()

    def get_storages_to_go(self):
        product_list = self._order.get_product_list()
        storages_to_go = deque()

        for storage in self._storages:
            if storage.get_production_model_name() in product_list:
                storages_to_go.append(storage)
                del product_list[storage.get_production_model_name()]

        return storages_to_go

    def _move(self, ac, goal_pose):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = goal_pose

        ac.send_goal(goal)
        ac.wait_for_result()
        return ac.get_state() == actionlib.GoalStatus.SUCCEEDED

    def _operate(self):
        rospy.loginfo(f"{self._object_name} started operating.")
        ac = actionlib.SimpleActionClient(self._action_name, MoveBaseAction)
        target_dispatch = None
        storages_to_go = deque()
        target_storage = None

        while self._status != "offline":
            if self._status == "startup":
                if ac.wait_for_server(rospy.Duration(5.0)):
                    rospy.loginfo("Startup complete, action client connected.")
                    self._status = "request_order"
                time.sleep(1)

            elif self._status == "standby":
                time.sleep(0.5)

            elif self._status == "request_order":
                self._order = self._order_controller.request_next_order_with_timeout(self._object_name, 1000)
                if self._order:
                    rospy.loginfo(f"Received order {self._order.get_name()}")
                    self._status = "process_order"

            elif self._status == "process_order":
                target_storage = None
                target_dispatch = None
                storages_to_go.clear()

                storages_to_go = self.get_storages_to_go()
                if not storages_to_go:
                    rospy.logwarn("No storages found for this order. Discarding.")
                    self._status = "close_order"
                    continue

                target_dispatch = next(
                    (d for d in self._dispatches if d.get_model_name() == self._order.get_goal_dispatch_name()), None
                )
                if not target_dispatch:
                    rospy.logwarn("No valid dispatch found. Discarding order.")
                    self._status = "close_order"
                    continue

                self._status = "plan"

            elif self._status == "plan":
                if storages_to_go:
                    target_storage = storages_to_go.popleft()
                    if target_storage:
                        self._status = "move_to_storage"
                else:
                    if target_dispatch:
                        self._status = "move_to_dispatch"
                    else:
                        self._status = "request_order"

            elif self._status == "move_to_storage":
                rospy.loginfo(f"Moving to {target_storage.get_name()}")
                if self._move(ac, target_storage.get_product_output_pose()):
                    rospy.loginfo(f"Arrived at {target_storage.get_name()}, requesting products.")
                    self._status = "request_product"
                else:
                    rospy.logwarn(f"Failed to move to {target_storage.get_name()}, retrying...")

            elif self._status == "request_product":
                product_name = target_storage.get_production_model_name()
                required_qty = self._order.get_product_list()[product_name]

                for _ in range(required_qty):
                    if self._status != "request_product":
                        break
                    product = target_storage.request_product()
                    if product:
                        rospy.loginfo(f"Got {product.get_name()}")
                        with self._cargo_bin_lock:
                            self._cargo_bin_products.append(product)
                    else:
                        time.sleep(0.5)

                rospy.loginfo(f"Collected {product_name} from {target_storage.get_name()}.")
                self._status = "plan"

            elif self._status == "move_to_dispatch":
                rospy.loginfo(f"Moving to {target_dispatch.get_name()}")
                if self._move(ac, target_dispatch.get_pick_pose()):
                    rospy.loginfo(f"Arrived at {target_dispatch.get_name()}, dispatching products.")
                    self._status = "dispatch_order"
                else:
                    rospy.logwarn(f"Failed to move to {target_dispatch.get_name()}, retrying...")

            elif self._status == "dispatch_order":
                while self._cargo_bin_products:
                    with self._cargo_bin_lock:
                        product = self._cargo_bin_products.pop()
                        target_dispatch.pick_product(product)
                        rospy.loginfo(f"Dispatched {product.get_name()} to {target_dispatch.get_name()}")
                    time.sleep(0.1)

                rospy.loginfo(f"Order {self._order.get_name()} completed.")
                self._status = "close_order"

            elif self._status == "close_order":
                self._order_controller.close_order(self._order)
                self._order = None
                self._status = "request_order"
