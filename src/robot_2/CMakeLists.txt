cmake_minimum_required(VERSION 3.1.3)
project(robot_2)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED
COMPONENTS
 roscpp
 rospy
 std_msgs
 tf
 gazebo_ros
 geometry_msgs
 gazebo_msgs
 )

find_package(Threads REQUIRED)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)

install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

include_directories(include ${catkin_INCLUDE_DIRS})

# add_executable()

# target_link_libraries(WarehouseSimulation ${catkin_LIBRARIES} Threads::Threads)
