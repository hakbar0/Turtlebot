#!/usr/bin/env python

import rospy as ros
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Forward:
    def __init__(self):
        # Initialize the ROS node and create a publisher and subscriber
        ros.init_node('control')
        ros.loginfo('control node has been created')
        self.pub = ros.Publisher('/cmd_vel', Twist, queue_size=10)
        self.laser_sub = ros.Subscriber('/kobuki/laser/scan', LaserScan, self.subscribe_laser, queue_size=10)
        self.robot = Twist()

        # Keep the node running
        ros.spin()

    def forward(self):
        # Set the robot's linear and angular velocities for forward motion
        self.robot.linear.x = 0.5
        self.robot.angular.z = 0
        self.pub.publish(self.robot)

    def rotate_right(self):
        # Rotate the robot 90 degrees to the right
        start_time = ros.Time.now()
        while ros.Time.now() - start_time < ros.Duration(1.8):  # Adjust the duration as needed
            self.robot.linear.x = 0
            self.robot.angular.z = -0.5
            self.pub.publish(self.robot)

    def subscribe_laser(self, laser):
        # Get the front and right distances from the laser scan data
        front_distance = min(laser.ranges[0:30] + laser.ranges[-30:])
        right_distance = laser.ranges[len(laser.ranges) // 2 + 90]

        # If the robot is within 0.2 meters of the front wall, rotate 90 degrees to the right
        if front_distance < 0.2:
            self.rotate_right()
        # If the robot is too close to the right-side wall, steer away
        elif right_distance < 0.2:
            self.robot.linear.x = 0.5
            self.robot.angular.z = -0.5
            self.pub.publish(self.robot)
        # If the robot is too far from the right-side wall, steer towards
        elif right_distance > 0.4:  # Adjust this threshold as needed
            self.robot.linear.x = 0.5
            self.robot.angular.z = 0.5
            self.pub.publish(self.robot)
        else:
            self.forward()

if __name__ == '__main__':
    Forward()
