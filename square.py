#!/usr/bin/env python
import os

import rospy
from math import radians
from geometry_msgs.msg import Twist


def square():
    global velocity_publisher
    # Starts a new node
    rospy.init_node('Walker', anonymous=True)
    rate = rospy.Rate(5)  # 5hz
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    desired_velocity = Twist()

    desired_velocity.linear.y = 0
    desired_velocity.linear.z = 0
    desired_velocity.angular.x = 0
    desired_velocity.angular.y = 0
    desired_velocity.angular.z = 0

    desired_velocity.linear.x = 0.2

    for i in range(30):
        velocity_publisher.publish(desired_velocity)
        rate.sleep()

    desired_velocity.linear.x = 0
    velocity_publisher.publish(desired_velocity)

    speed = 45  # (degrees/sec)
    angle = 90  # degrees

    angular_speed = radians(speed)
    relative_angle = radians(angle)

    desired_velocity.linear.x = 0
    desired_velocity.linear.y = 0
    desired_velocity.linear.z = 0
    desired_velocity.angular.x = 0
    desired_velocity.angular.y = 0
    desired_velocity.angular.z = angular_speed

    # Setting the current time
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while current_angle < relative_angle:
        velocity_publisher.publish(desired_velocity)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed * (t1 - t0)

    # Stop rotating
    desired_velocity.angular.z = 0
    velocity_publisher.publish(desired_velocity)


def shutdown():
    global velocity_publisher
    velocity_publisher.publish(Twist())
    os._exit(0)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            square()
            pass
    except rospy.ROSInterruptException:
        pass
