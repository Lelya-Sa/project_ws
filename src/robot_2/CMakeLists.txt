cmake_minimum_required(VERSION 3.1.3)
project(robot_2)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages rospack depends robot_2
find_package(catkin REQUIRED
COMPONENTS
    my_simulations
    gazebo_plugins
	roscpp
	rospy
	std_msgs
	tf
	gazebo_ros
	geometry_msgs
	gazebo_msgs
	cpp_common
	rostime
	roscpp_traits
	roscpp_serialization
	catkin
	genmsg
	genpy
	message_runtime
	gencpp
	geneus
	gennodejs
	genlisp
	message_generation
	rosbuild
	rosconsole
	rosgraph_msgs
	xmlrpcpp
	eigen_stl_containers
	random_numbers
	ros_environment
	rospack
	roslib
	resource_retriever
	shape_msgs
	visualization_msgs
	geometric_shapes
	rosconsole_bridge
	pluginlib
	urdf
	kdl_parser
	octomap_msgs
	actionlib_msgs
	sensor_msgs
	rosbag_migration_rule
	trajectory_msgs
	object_recognition_msgs
	moveit_msgs
	pybind11_catkin
	rosgraph
	urdfdom_py
	srdfdom
	tf2_msgs
	tf2
	tf2_eigen
	rosclean
	rosmaster
	rosout
	rosparam
	rosunit
	roslaunch
	rostest
	actionlib
	message_filters
	tf2_py
	tf2_ros
	tf2_geometry_msgs
	moveit_core
	tf2_kdl
	moveit_kinematics
	moveit_ros_occupancy_map_monitor
	topic_tools
	roslz4
	rosbag_storage
	std_srvs
	rosbag
	rosmsg
	rosservice
	dynamic_reconfigure
	moveit_ros_planning
	moveit_ros_move_group
	moveit_fake_controller_manager
	interactive_markers
	moveit_ros_robot_interaction
	image_transport
	cv_bridge
	bond
	smclib
	bondcpp
	nodelet
	moveit_ros_perception
	rostopic
	rosnode
	roswtf
	warehouse_ros
	moveit_ros_warehouse
	moveit_ros_manipulation
	eigenpy
	moveit_ros_planning_interface
	media_export
	angles
	laser_geometry
	nav_msgs
	map_msgs
	python_qt_binding
	rviz
	moveit_ros_visualization
	xacro
	moveit_setup_assistant
	control_msgs
	moveit_simple_controller_manager
	joint_state_publisher
	robot_state_publisher
	realtime_tools
	control_toolbox
	controller_interface
	joint_trajectory_controller
	gazebo_dev
	controller_manager
	hardware_interface
	transmission_interface
	joint_limits_interface
	gazebo_ros_control
	class_loader
 )

## Declare ROS messages and services
## add_message_files(DIRECTORY msg FILES Num.msg)
## add_service_files(DIRECTORY srv FILES AddTwoInts.srv)

## Generate added messages and services
## generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)

install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(${catkin_INCLUDE_DIRS}
  )


 # https://wiki.ros.org/octomap
#find_package(octomap REQUIRED)
#include_directories(${OCTOMAP_INCLUDE_DIRS})
# target_link_libraries(robot_2 ${OCTOMAP_LIBRARIES})


find_package(Threads REQUIRED)

## find_package(gazebo REQUIRED)
## include_directories(${GAZEBO_INCLUDE_DIRS})
## list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")


#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_warehouse-robot-simulation.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)

add_executable(robot_2 src/WarehouseSimulation.cpp src/ModelController.cpp src/Product.cpp src/Storage.cpp src/Dispatch.cpp src/WarehouseObject.cpp src/Order.cpp src/OrderController.cpp src/Robot.cpp)
target_link_libraries(robot_2 ${catkin_LIBRARIES} Threads::Threads )
#add_dependencies(WarehouseSimulation warehouse_robot_simulator_generate_messages_cpp)

## target_link_libraries(robot_2 ${GAZEBO_LIBRARIES})
##  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")