#!/usr/bin/env python3

import rospy
import signal
import threading
import time
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler
from gazebo_msgs.srv import SpawnModel, DeleteModel

# Import custom modules (assuming they are Python equivalents of the C++ classes)
from model_controller import ModelController
from storage import Storage
from dispatch import Dispatch
from robot import Robot
from order_controller import OrderController

is_shutdown = False


def print_message(message):
    """Thread-safe logging using rospy."""
    rospy.loginfo(f"[WarehouseSimulation] {message}")


def sigint_handler(sig, frame):
    """Custom SIGINT handler for clean shutdown."""
    global is_shutdown
    print_message("Simulation is being shut down.")
    is_shutdown = True


def get_pose_from_string(x, y, z, roll, pitch, yaw):
    """Build and return a geometry_msgs/Pose from string values of xyzrpy."""
    pose = Pose()
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z

    # Convert RPY to quaternion
    quaternion = quaternion_from_euler(roll, pitch, yaw)
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]
    return pose


def load_models(model_controller, project_directory):
    """Load all specified models to the model controller."""
    model_controller.add("ProductR", f"{project_directory}/models/warehouseObjects/ProductR.sdf")
    model_controller.add("ProductG", f"{project_directory}/models/warehouseObjects/ProductG.sdf")
    model_controller.add("ProductB", f"{project_directory}/models/warehouseObjects/ProductB.sdf")

    model_controller.add("StorageR", f"{project_directory}/models/warehouseObjects/StorageR.sdf")
    model_controller.add("StorageG", f"{project_directory}/models/warehouseObjects/StorageG.sdf")
    model_controller.add("StorageB", f"{project_directory}/models/warehouseObjects/StorageB.sdf")

    model_controller.add("DispatchA", f"{project_directory}/models/warehouseObjects/Dispatch.sdf")
    model_controller.add("DispatchB", f"{project_directory}/models/warehouseObjects/Dispatch.sdf")


def instantiate_warehouse_objects(storages, dispatches, model_controller, project_directory):
    """Instantiate warehouse objects from config files."""
    try:
        # Read storages configuration
        with open(f"{project_directory}/configs/storages") as storages_config:
            for line in storages_config:
                if line.startswith("#"):  # Skip comments
                    continue
                data = line.split()
                storage_model, production_model, max_capacity = data[:3]
                storage_pose = get_pose_from_string(*map(float, data[3:9]))
                product_output_pose = get_pose_from_string(*map(float, data[9:]))
                storages.append(
                    Storage(storage_model, production_model, int(max_capacity), storage_pose, product_output_pose,
                            model_controller))

        # Read dispatches configuration
        with open(f"{project_directory}/configs/dispatches") as dispatches_config:
            for line in dispatches_config:
                if line.startswith("#"):
                    continue
                data = line.split()
                dispatch_model = data[0]
                dispatch_pose = get_pose_from_string(*map(float, data[1:7]))
                product_pick_pose = get_pose_from_string(*map(float, data[7:]))
                dispatches.append(Dispatch(dispatch_model, dispatch_pose, product_pick_pose, model_controller))

        print_message(f"Storages created: {len(storages)}")
        print_message(f"Dispatches created: {len(dispatches)}")
        return True
    except Exception as e:
        print_message(f"Error instantiating warehouse objects: {e}")
        return False


def main():
    rospy.init_node("WarehouseSimulation", disable_signals=True)
    signal.signal(signal.SIGINT, sigint_handler)

    project_directory = "../catkin_ws/src/warehouse_robot_simulation"
    model_controller = ModelController("ModelController")
    order_controller = OrderController("OrderController")
    storages, dispatches, robots = [], [], []

    # Load models and instantiate warehouse objects
    load_models(model_controller, project_directory)
    if not instantiate_warehouse_objects(storages, dispatches, model_controller, project_directory):
        print_message("Check configuration files and try again.")
        rospy.signal_shutdown("Configuration Error")
        return

    # Add robot and start operations
    robots.append(Robot("amr", "move_base", storages, dispatches, order_controller))
    for storage in storages:
        model_controller.spawn(storage.get_name(), storage.get_model_name(), storage.get_pose())
        storage.start_operation()
    for dispatch in dispatches:
        model_controller.spawn(dispatch.get_name(), dispatch.get_model_name(), dispatch.get_pose())
    for robot in robots:
        robot.start_operation()

    rospy.Subscriber("warehouse/order/add", String, order_controller.add_order)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown() and not is_shutdown:
        rate.sleep()

    # Clean up spawned objects
    for storage in storages:
        model_controller.delete(storage.get_name())
    for dispatch in dispatches:
        model_controller.delete(dispatch.get_name())
    for robot in robots:
        for product_name in robot.get_cargo_bin_products_name():
            model_controller.delete(product_name)

    time.sleep(1)  # Wait to ensure deletions are processed
    rospy.signal_shutdown("Simulation Complete")


if __name__ == "__main__":
    main()
