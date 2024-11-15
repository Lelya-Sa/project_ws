cmake_minimum_required(VERSION 3.1.3)
project(robot_2)

find_package(catkin REQUIRED REQUIRED COMPONENTS roscpp rospy std_msgs tf)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
include_directories(include ${catkin_INCLUDE_DIRS})
add_executable()
target_link_libraries(joint_state_publisher ${catkin_LIBRARIES})
