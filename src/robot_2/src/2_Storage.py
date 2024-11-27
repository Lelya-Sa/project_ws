import threading
import rospy
from geometry_msgs.msg import Pose
from product import Product  # Assume this module is implemented
from model_controller import ModelController  # Assume this module is implemented


class Storage:
    _id_counter = 0
    _id_lock = threading.Lock()

    def __init__(self, model_name, product_model_name, max_capacity, storage_pose, product_output_pose, model_controller):
        with Storage._id_lock:
            self._id = Storage._id_counter
            Storage._id_counter += 1

        self._object_name = f"{model_name}#{self._id}"
        self._type = "objectStorage"
        self._storage_model_name = model_name
        self._production_model_name = product_model_name
        self._storage_pose = storage_pose
        self._max_capacity = max_capacity
        self._product_output_pose = product_output_pose
        self._model_controller = model_controller

        self._stored_products = []
        self._storage_lock = threading.Lock()
        self._stop_production = threading.Event()
        self.threads = []

        rospy.loginfo(f"[{self._object_name}] Initialized.")

    def __del__(self):
        self.stop_operation()
        rospy.loginfo(f"[{self._object_name}] Shutting down.")

    def get_model_name(self):
        return self._storage_model_name

    def get_production_model_name(self):
        return self._production_model_name

    def get_pose(self):
        return self._storage_pose

    def get_product_output_pose(self):
        return self._product_output_pose

    def request_product(self):
        with self._storage_lock:
            if self._stored_products:
                product = self._stored_products.pop()
                self._model_controller.spawn(product.get_name(), product.get_model_name(), self._product_output_pose)

                rospy.loginfo(
                    f"[{self._object_name}] Product {product.get_name()} requested. Remaining storage: {len(self._stored_products)}"
                )
                return product
            else:
                rospy.logwarn(f"[{self._object_name}] No products available for request.")
                return None

    def start_operation(self):
        production_thread = threading.Thread(target=self._production)
        production_thread.daemon = True
        self.threads.append(production_thread)
        production_thread.start()

    def stop_operation(self):
        self._stop_production.set()
        for thread in self.threads:
            thread.join()

    def _production(self):
        rospy.loginfo(f"[{self._object_name}] Starting {self._production_model_name} production.")

        while not self._stop_production.is_set() and self._production_model_name:
            rospy.sleep(2.0)  # Simulated production time

            with self._storage_lock:
                if len(self._stored_products) < self._max_capacity:
                    product = Product(self._production_model_name)
                    self._stored_products.append(product)
                    rospy.logdebug(
                        f"[{self._object_name}] Produced {product.get_name()}. Total storage size: {len(self._stored_products)}"
                    )

        rospy.loginfo(f"[{self._object_name}] Production stopped.")
