#!/bin/sh
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 1_my_world.launch" &
sleep 7
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 2_spawn_robot.launch" &
sleep 5
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 3_ros_controllers.launch" &
sleep 5
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 5_amcl.launch" &
sleep 5
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 6_view_navigation.launch" &
sleep 5
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 warehouse_simulation.launch" &

# rostopic pub /warehouse/order/add std_msgs/String "data: 'DispatchA ProductR 6 ProductG 4'"