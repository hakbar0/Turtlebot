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

    # Move forward for 3 seconds (30 iterations at 10Hz)
    for i in range (30):
        pub.publish(desired_velocity)
        rate.sleep()

    # Set the desired velocity to move backwards
    desired_velocity.linear.x = -0.2 # Backward with 0.2 m/sec.

    # Move backwards for 3 seconds (30 iterations at 10Hz)
    for i in range(30):
        pub.publish(desired_velocity)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass