1. install ros noetic: https://wiki.ros.org/noetic/Installation/Ubuntu
2. install gazebo: https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=
3. install moveit if you want to control the robot manually: https://moveit.ai/install/
4. install RViz: https://wiki.ros.org/rviz/UserGuide
5. clone the project:
``` git clone https://github.com/Lelya-Sa/project_ws.git```
---------------------------
---------------------------

after cloning source ROS in bash:
```
    source /opt/ros/noetic/setup.bash 
```

change directory to project_ws:

```
    cd project_ws
```

then source the project workspace:
```
    source ./devel/setup.bash
```
* make sure you have these packages:

```
sudo apt install ros-noetic-ros-control* && ros-noetic-control* && ros-noetic-moveit*

sudo apt-get install ros-noetic-ros-controllers

sudo apt-get install ros-noetic-gazebo-ros ros-noetic-eigen-conversions ros-noetic-object-recognition-msgs ros-noetic-roslint

sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-msgs ros-noetic-gazebo-plugins ros-noetic-gazebo-ros-control

sudo apt-get install ros-noetic-moveit ros-noetic-moveit-plugins ros-noetic-moveit-planners

sudo apt-get install ros-noetic-joint-state-controller ros-noetic-position-controllers ros-noetic-joint-trajectory-controller
      
sudo apt-get install ros-noetic-gmapping
      
sudo apt-get install ros-noetic-map-server
      
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
        ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
        ros-noetic-rgbd-launch \
        ros-noetic-rosserial-python ros-noetic-rosserial-client \
        ros-noetic-rosserial-msgs ros-noetic-amcl \
        ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
        ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
        ros-noetic-navigation ros-noetic-interactive-markers
        
sudo apt install ros-noetic-dynamixel-sdk
      
sudo apt install ros-noetic-turtlebot3-msgs
      
sudo apt install ros-noetic-turtlebot3
                                		
sudo apt-get install ros-noetic-dwa-local-planner
			
sudo apt-get install ros-noetic-slam-gmapping
		
sudo apt-get install ros-noetic-scan-tools

sudo apt install python3-rosmake

sudo apt-get install ros-noetic-trac-ik-kinematics-plugin

sudo apt install ros-noetic-tf2-tools
          
rosdep update
      
rosdep install --from-paths src --ignore-src -r -y --rosdistro noetic
```

------------------------------------------------------------
------------------------------------------------------------

**Xterm** were used to execute launch files individually. If you want to use it and don't have it installed, then run:

```
sudo apt-get install xterm
```

then build it:
```
cd ~/project_ws
catkin_make
```
    
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------

make script files executable before run them:

```
cd ~/catkin_ws/src/warehouse_robot_simulation/scripts
chmod +x *.sh
```

To run the simulation, there are options:

```
	source ~/.bashrc
	roscore
```

- to run all the simulation (not done yet)  Open a terminal in the `scripts` folder and run `warehouse_simulation.sh`:

```
./warehouse_simulation.sh
    
```
# option 1

- to run the controlling for development Open a terminal in the `scripts` folder and run `controlling_move.sh`:
```
    ./controlling_move.sh
    
```
# option 2
- Or launch the following `.launch` files in the specified sequence:

# 1
to launch the world:
```
	source ~/.bashrc
	roslaunch robot_2 1_my_world.launch
```
# 2
to spawn the robot:
```
	source ~/.bashrc
	roslaunch robot_2 2_spawn_robot.launch
```
# 3
to load the robot controllers:
```
	source ~/.bashrc
	roslaunch robot_2 3_ros_controllers.launch
```
# 4
**not necessary** , if you want to control the robot control groups manually:
```
	source ~/.bashrc
	roslaunch robot_2 4_move_group_moveit.launch
```
# 5
**not necessary** , if you want to move the robot in space manually:
```
	source ~/.bashrc
	rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
# 6
mapping the map or moving base in an existing map.
```
	source ~/.bashrc
```
	
### if map is not ready ( for developing or if you want another warehouse map)
```
	roslaunch robot_2 5_slam_gmapping.launch
```
	
### if map is ready ( for final )
```
	roslaunch robot_2 5_amcl.launch
```

# 7 
**not necessary** , for developers, if you want to see how the robot works and navigate:
```
	source ~/.bashrc
	roslaunch robot_2 6_RViz.launch
```

---------------------------
---------------------------
---------------------------
---------------------------
---------------------------
---------------------------






---------------------------
# notes:
- link to a video of my robot picking and placing a box from the shelf:
  https://technionmail-my.sharepoint.com/:v:/r/personal/sa_lelya_campus_technion_ac_il/Documents/97244%20-%20%D7%A8%D7%95%D7%91%D7%95%D7%98%D7%99%D7%9D%20%D7%A7%D7%95%D7%92%D7%A0%D7%99%D7%98%D7%99%D7%91%D7%99%D7%99%D7%9D/vid/pick_and_place.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=tX3Ffj
- used Onshape CAD to calculate inertia. 
- used move group for pick and place poses.
- will use ``` ~/get_model_state ``` : ```gazebo_msgs/GetModelState``` - This service returns the states of a model in simulation.
- rosservice call gazebo/get_joint_properties '{joint_name: joint1}'
type: 0
damping: []
position: [0.403249745392813]
rate: [0.014711402265945629]
success: True
status_message: "GetJointProperties: got properties"
- rosservice call gazebo/get_model_state '{model_name: mixed_robot}'
header: 
  seq: 1
  stamp: 
    secs: 1370
    nsecs: 639000000
  frame_id: ''
pose: 
  position: 
    x: 0.00020166388125387514
    y: -0.00016675479282465442
    z: -4.7395556354856705e-06
  orientation: 
    x: -6.658904667255289e-06
    y: 5.322692176398447e-08
    z: -0.0007139137125695
    w: 0.9999997451414011
twist: 
  linear: 
    x: -1.1541245281820859e-05
    y: 0.0001841961922394613
    z: 0.0030772001310822574
  angular: 
    x: 0.01265736766702449
    y: -6.15374216035987e-05
    z: -5.8696718001216e-07
success: True
status_message: "GetModelState: got properties"






