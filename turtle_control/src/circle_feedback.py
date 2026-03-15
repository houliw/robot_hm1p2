#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import numpy as np


def pos_callback(data):

    turtle_pos = data
    rospy.loginfo("linear velocity = %.2f,angular velocity = %.2f",data.linear_velocity,data.angular_velocity)


def main():
    rospy.init_node('circle_control')
    sub = rospy.Subscriber('/turtle1/pose', Pose,pos_callback,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)

        msg  = Twist()

        msg.linear.x -= (turtle_pos.linear_velocity - 1.5)
        msg.angular.z -= (turtle_pos.angular_velocity - 1.0)

        pub.publish(msg)

        rospy.loginfo("Turtle is drawing a circle...")
        # print('gogogo')

        rate.sleep()

    rospy.spin()



if __name__ == "__main__":
    turtle_pos = Pose()
    main()