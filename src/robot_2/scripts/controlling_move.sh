#!/bin/sh
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 1_my_world.launch" &
sleep 15
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 2_spawn_robot.launch" &
sleep 1
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 3_ros_controllers.launch" &
sleep 5
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; rosrun teleop_twist_keyboard teleop_twist_keyboard.py" & 
sleep 3
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 4_move_group_moveit.launch " &
sleep 5
#xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 5_slam_gmapping.launch " &
#sleep 3
#xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 5_amcl.launch" &
#sleep 5
#xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 6_view_navigation.launch" &
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 6_RViz.launch.launch" &

# 
# remider: to save the generated map, run: rosrun map_server map_saver -f warehouse
