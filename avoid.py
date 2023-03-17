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

    def avoid_wall(self):
        # Turn the robot to avoid the wall
        self.robot.linear.x = 0
        self.robot.angular.z = 0.5
        self.pub.publish(self.robot)

    def subscribe_laser(self, laser):
        # Get the minimum distance from the laser scan data
        min_distance = min(laser.ranges)

        # If the minimum distance is less than a threshold, avoid the wall
        if min_distance < 0.1:
            self.avoid_wall()
        else:
            self.forward()

if __name__ == '__main__':
    Forward()
