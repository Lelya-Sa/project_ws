killall gzserver

killall gzclient

---------------------------

source /opt/ros/noetic/setup.bash 

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
    
rosdep update

rosdep install --from-paths src --ignore-src -r -y --rosdistro noetic    

---------------------------

roslaunch my_simulations my_world.launch --screen

---------------------------

---------------------------
