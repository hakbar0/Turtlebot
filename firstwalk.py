#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def publisher():
    # Create a publisher object that publishes Twist messages to the 'cmd_vel' topic
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    # Initialize the node with the name 'Walker'
    rospy.init_node('Walker', anonymous=True)

    # Set the publishing rate to 10Hz
    rate = rospy.Rate(10)

    # Create a Twist message object with a desired velocity
    desired_velocity = Twist()
    desired_velocity.linear.x = 0.2 # Forward with 0.2 m/sec.
    desired_velocity.angular.z = 0.5 # rotate with 0.5 m/s

    # Move forward for 3 seconds (30 iterations at 10Hz) and rotate
    for i in range (30):
        pub.publish(desired_velocity)
        rate.sleep()

    # Stop the robot for 1 second
    desired_velocity.linear.x = 0.0
    desired_velocity.angular.z = 0.0
    for i in range(10):
        pub.publish(desired_velocity)
        rate.sleep()

    # Set the desired angular velocity to rotate the robot
    desired_velocity.angular.z = 0.5 # Rotate at 0.5 rad/sec (clockwise)

    # Rotate the robot for 3 seconds (30 iterations at 10Hz)
    for i in range(30):
        pub.publish(desired_velocity)
        rate.sleep()

    # Stop the robot for 1 second
    desired_velocity.linear.x = 0.0
    desired_velocity.angular.z = 0.0
    for i in range(10):
        pub.publish(desired_velocity)
        rate.sleep()

    # Set the desired angular velocity to rotate the robot in the opposite direction
    desired_velocity.angular.z = -0.5 # Rotate at -0.5 rad/sec (counterclockwise)

    # Rotate the robot for 3 seconds (30 iterations at 10Hz)
    for i in range(30):
        pub.publish(desired_velocity)
        rate.sleep()

    # Stop the robot
    desired_velocity.linear.x = 0.0
    desired_velocity.angular.z = 0.0
    pub.publish(desired_velocity)

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
