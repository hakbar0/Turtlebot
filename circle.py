#!/usr/bin/env python

import rospy
from math import radians
from geometry_msgs.msg import Twist


def publisher():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('Walker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    desired_velocity = Twist()
    desired_velocity.linear.x = -1  # backward with 1 m/sec.
    desired_velocity.angular.z = radians(180)
    while not rospy.is_shutdown():
        pub.publish(desired_velocity)
        rate.sleep()
    pass


if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
