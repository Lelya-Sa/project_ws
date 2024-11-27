import threading
from enum import Enum
import rospy

class ObjectType(Enum):
    NO_OBJECT = 0

class WarehouseObject:
    _total_objects = 0
    _cout_lock = threading.Lock()

    def __init__(self):
        self._type = ObjectType.NO_OBJECT
        self._id = WarehouseObject._total_objects
        WarehouseObject._total_objects += 1
        self._object_name = f"Object_{self._id}"
        self.threads = []

    def __del__(self):
        for t in self.threads:
            t.join()

    def get_name(self):
        return self._object_name

    def get_type(self):
        return self._type

    @staticmethod
    def print_message(message, object_name="WarehouseObject"):
        with WarehouseObject._cout_lock:
            rospy.loginfo(f"[{object_name}] {message}")
