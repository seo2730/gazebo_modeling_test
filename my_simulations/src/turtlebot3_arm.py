#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

# Keyboard in Linux
import sys
import tty
import termios

def getKey():
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return ch

def arm(joint1, joint2, joint3, joint4):   
    position1 = joint1
    position2 = joint2
    position3 = joint3
    position4 = joint4

    pub1.publish(position1)
    pub2.publish(position2)
    pub3.publish(position3)
    pub4.publish(position4)
    rate.sleep()
        

if __name__== '__main__': 
    rospy.init_node('turtlebot3_arm')

    pub1 = rospy.Publisher('/joint1_position_controller/command', Float64 ,queue_size=10)
    pub2 = rospy.Publisher('/joint2_position_controller/command', Float64 ,queue_size=10)
    pub3 = rospy.Publisher('/joint3_position_controller/command', Float64 ,queue_size=10)
    pub4 = rospy.Publisher('/joint4_position_controller/command', Float64 ,queue_size=10)
    
    rate = rospy.Rate(50) # 50hz 

    try:
        
        while not rospy.is_shutdown():
            key = getKey()
            if key == 'z':
                arm(-0.9,-0.9,0.9,0.9)

            elif key == 'x':
                arm(0.0,0.0,0.0,0.0)

    except rospy.ROSInterruptException:
        rospy.loginfo("Arm deactivated.")
    finally:
        arm(0.0,0.0,0.0,0.0)

    if ox.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)