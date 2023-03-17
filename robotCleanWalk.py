#!/usr/bin/env python

import rospy as ros
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Forward:
    def __init__(self):
        # Initialize the ROS node and create a publisher and subscriber
        ros.init_node('control')
        ros.loginfo('control node has been created')
        self.pub = ros.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = ros.Subscriber('/odom', Odometry, self.subscribe, queue_size=10)
        self.robot = Twist()

        # Keep the node running
        ros.spin()

    def forward(self):
        # Set the robot's linear and angular velocities for forward motion
        self.robot.linear.x = 0.5
        self.robot.angular.z = 0
        self.pub.publish(self.robot)

    def stop(self, odom_x):
        # Set the robot's linear and angular velocities for stopping
        self.robot.linear.x = 5 if odom_x < 2 else 0
        self.robot.angular.z = 0
        self.pub.publish(self.robot)

    def subscribe(self, odom):
        # Log the Odometry data and decide whether to move forward or stop
        ros.loginfo(odom)
        odom_x = odom.pose.pose.position.x

        if odom_x < 2:
            self.forward()
        else:
            self.stop(odom_x)

if __name__ == '__main__':
    Forward()
