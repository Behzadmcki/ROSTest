# ROS Test
This is a simple programming assignment designed to test your abilities to use ROS to solve a problem.
## How to use this package 
myleo is very simple package that is buit over python and rospy.

### prepration
we assume that you are working on ubuntu or debian base systems 
to install docker you should open terminal and copy and paste these lines 
    "$curl -fsSL https://get.docker.com -o get-docker.sh"
    "$sudo sh get-docker.sh"
after installing the docker pull the docker image for the project:
    "docker pull cjb873/sim_image:1.0"
### Running 
To run the image in a container, use the command docker run -p 9000:80 --name sim -it cjb873/sim_image:1.0, then open a web browser and go to localhost:9000. You should see the desktop for your container.
### Simulation 
To start the simulated environment, use the command:
 "$roslaunch myleo sim_and_ardetector.launch"
This command will bring up the gazebo simulation with a leo robot  and a rqt_view_image node to see the image of the RGB camera and it will also launch ARTag tracking node with its default configs
### Run the tracker 
For running the listener node to do the task you should run:
    "rosrun myleo listener.py"
as it runs it will print the linear x axis  and angular z axis velocity
### examine the code 
to see the resault you should insert a marker from prepared AR tags in gazebo and put it in front of FOV of the robot's camera( you can see the image of the camera live in rqt_view_image)
as you put the marker in front of the camera the robot will move toward the marker until  ARTag tracking node could not recognise the marker and then the robot will stop












