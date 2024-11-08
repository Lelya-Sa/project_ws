1. install ros noetic: https://wiki.ros.org/noetic/Installation/Ubuntu
2. install gazebo: https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=
3. instal moveit: https://moveit.ai/install/
4. install RViz: https://wiki.ros.org/rviz/UserGuide
5. clone the project
---------------------------
after cloning source ROS in bash:

    source /opt/ros/noetic/setup.bash 

change directory to project_wc:

    cd project_wc
  
then source the project workspace:

    source ./devel/setup.bash

* make sure you have these packages:

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
        ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
        ros-noetic-rosserial-python ros-noetic-rosserial-client \
        ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
        ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
        ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
        ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
        
      sudo apt install ros-noetic-dynamixel-sdk
      
      sudo apt install ros-noetic-turtlebot3-msgs
      
      sudo apt install ros-noetic-turtlebot3
      
      sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control
      
      sudo apt-get install \
          ros-noetic-gazebo-ros \
          ros-noetic-eigen-conversions \
          ros-noetic-object-recognition-msgs \
          ros-noetic-roslint
          
      sudo apt-get install ros-noetic-trac-ik-kinematics-plugin
          
      rosdep update
      
      rosdep install --from-paths src --ignore-src -r -y --rosdistro noetic


---------------------------
then build it:

    cd ~/project_ws
    catkin_make
    
---------------------------
To see the environment in gazebo type in termenal:

    roslaunch my_simulations my_world.launch --screen

---------------------------

roslaunch robot_2 demo_gazebo.launch

---------------------------
note if you encounter gazebo initiation problems type in terminal:

    killall gzserver
    
    killall gzclient
