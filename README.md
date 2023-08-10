# ROS Test
This is a simple programming assignment designed to test your abilities to use ROS to solve a problem.

## Background

### LeoRover
![LeoRover](https://uploads-ssl.webflow.com/5aeedc7c6154a8acb0b29044/5e8e4d5a3fd0013dab1d3ded_leo%20rover%20showcase.jpg)

At Discover, we use LeoRovers as our UGVs. Information about the LeoRover can be found [here](leorover.tech). The LeoRovers use a series of ROS topics and nodes to control and access different components and sensors. The full rqt graph of the topics and nodes is below. 

![RQT_GRAPH](rosgraph.svg)
#### Important Topics
The most important topics for operation and sensing of the LeoRovers include:
* /cmd_vel: This topic is used to move the rover by turning the wheels. The topic listens for geometry_msgs/Twist messages.
* /wheel_odom_with_covariance: This topic contains a lot of useful information about the current position and velocity of the robot. Information is published in the format of a nav_msgs/Odometry message.
* /joint_states: This topic also contains a lof of useful information about the current position and velocity of the robot. Information is published in the format of a sensor_msgs/JointState message.
* /imu/data_raw: This topic contains useful information published from the robot's inertial measuring unit. Messages on this topic are published in the sensor_msgs/Imu format.
* /camera/image_raw: This topic is used by the raspicam to publish image data. Images are published in the sensor_msgs/Image format.

### ARTags

![ARTag](http://wiki.ros.org/ar_track_alvar?action=AttachFile&do=get&target=artags.png)

ARTags are markers that are used to support 3D alignment and tracking in augmented reality systems. More information about ARTags can be
found [here](https://www.cs.cmu.edu/afs/cs/project/skinnerbots/Wiki/AprilTags/NRC-47419.pdf). We use the [ar_track_alvar](http://wiki.ros.org/ar_track_alvar).
ROS package to generate and track ARTags. Launch and configuration files to use integrate this package with the LeoRovers are included in our RoverAPI package.

## The Task
Your task is to create a ROS package that utilizes the topics published by the LeoRover and the ar_track_alavar package to have the robot follow an ARTag as it moves. 

![Video](https://drive.google.com/file/d/10pCkqGRu3OJQssxBhGJ9wco14s3YWYRL/view?usp=sharing)



