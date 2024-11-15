#!/bin/sh
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 world.launch" &
sleep 7
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 robot_spawner.launch" &
sleep 5
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; rosrun teleop_twist_keyboard teleop_twist_keyboard.py" & 
sleep 3
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 slam_gmapping.launch " & 
sleep 3
xterm  -e  " source /opt/ros/noetic/setup.bash; source ~/project_ws/devel/setup.bash; roslaunch robot_2 view_navigation.launch" & 
# 
# remider: to save the generated map, run: rosrun map_server map_saver -f warehouse
