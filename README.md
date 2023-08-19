# ROS Test
This simple programming assignment is designed to test your abilities to use ROS to solve a problem.
## How to use this package 
myleo is a very simple package built over Python and rospy.

### preparation
we assume that you are working on Ubuntu or Debian base systems 
to install docker, you should open a terminal and copy and paste these lines

```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
```

After installing the docker, pull the docker image for the project:
  ```bash  
    docker pull cjb873/sim_image:1.0
  ```
### Running 
To run the image in a container, use the command docker
```bash
     run -p 9000:80 --name sim -it cjb873/sim_image:1.0
 ```
Then open a web browser and go to localhost:9000. You should see the desktop for your container.
### Simulation 
To start the simulated environment, use the command:
```bash 
    roslaunch myleo sim_and_ardetector.launch
```
This command will bring up the gazebo simulation with a Leo robot  and a rqt_view_image node to see the image of the RGB camera, and it will also launch the ARTag tracking node with its default configs
### Run the tracker 
For running the listener node to do the task, you should run:
```bash
    rosrun myleo listener.py
```
as it runs, it will print the linear x-axis  and angular z-axis velocity
### Examine the code 
to see the result, you should insert a marker from prepared AR tags in the gazebo and put it in front of the FOV of the robot's camera( you can see the image of the camera live in rqt_view_image)
as you put the marker in front of the camera, the robot will move toward the marker until  the ARTag tracking node cannot recognize the marker, and then the robot will stop



https://github.com/Behzadmcki/ROSTest/assets/46256757/ee211c42-d211-43cf-97aa-954de7cea998



## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/behzad-mckizade-595284148/)










