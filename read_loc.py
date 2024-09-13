#!/usr/bin//env python
import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry 
import matplotlib.pyplot as plt
import numpy as np
import time

orientationb = 0
def callback(data):
      global orientationb, brake, vel
      orientationb = data.pose.pose.position.y
      global pub, pubBrake
      pub = rospy.Publisher("/cmd_vel", Float64, queue_size=0)
      pubBrake = rospy.Publisher('/brakes',Float64, queue_size=0)
      rate = rospy.Rate(10)

   
      
        #istener()
      if orientationb>=48:
            vel=0
            brake=.8
            
      else:
            vel=1
            brake=0
      pub.publish(vel)
      pubBrake.publish(brake)
      rospy.loginfo(f"The BRAKE is at {brake}")
      

def listener():
     rospy.Subscriber("/odom",Odometry,callback)
     rospy.spin()


    
         
   # rospy.spin()

if __name__=='__main__':
    rospy.init_node('pionner_control',anonymous=True)
    listener()

    