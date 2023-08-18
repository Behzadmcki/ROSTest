#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray
from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Twist
from math import atan2


class Server:
    def __init__(self):
        rospy.init_node('mynode', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        rospy.Subscriber('/wheel_odom_with_covariance', Odometry, self.odometry_callback)
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers,self.marker_callback)

        self.rate = rospy.Rate(10)
        self.marker_position_X = None
        self.marker_position_Y = None
        self.robot_position_X = None
        self.robot_position_Y = None
        self.cmd_msg = Twist()

    def odometry_callback(self,data):


        self.robot_position_X=round(data.pose.pose.position.x,5)
        self.robot_position_Y=round(data.pose.pose.position.y,5)
        
        # print("Position x: ", x)


    def marker_callback(self,data):

        # print("Received Marker data:")
        if (data.markers):
            self.marker_position_X=round(data.markers[0].pose.pose.position.x,5)
            self.marker_position_Y=round(data.markers[0].pose.pose.position.y,5)
            self.compute_stuff()
            # print("Received Marker data: \n ",data)
 
        else:
            pass
            # print("no marker in the picture")

        # print("Position x: ", x)

    def compute_stuff(self):
        if self.marker_position_X is not None and self.marker_position_X is not None :
            X=round(self.marker_position_X*4,3)
            Y=round(self.marker_position_Y*4,3)
            # criteria=X/Y
            if Y<0.05 and Y>-0.05 :
                self.cmd_msg.linear.x = 0.1
                self.cmd_msg.angular.z = 0
            else:
                self.cmd_msg.linear.y = 0
                self.cmd_msg.angular.z = atan2(Y,X)

            print(f'the result is : {self.cmd_msg.angular.z}   {self.cmd_msg.linear.x }' )
        else :

            self.cmd_msg.linear.y = 0
            self.cmd_msg.linear.x = 0
            print("not valid")
              # Compute something.
        #  self.talker()  
        self.talker()
        

    def talker(self):
            self.pub.publish(self.cmd_msg)
            # self.rate.sleep()
            



 
   
    

if __name__ == '__main__':
    try:



        server = Server()
        while not rospy.is_shutdown():
            server.compute_stuff()
            rospy.spin()






    except rospy.ROSInterruptException:
        pass