#!/usr/bin/env python3
import rospy as ros
from sensor_msgs.msg import LaserScan
import numpy as np
from numpy import Inf
from geometry_msgs.msg import Twist
from nav_msgs.msg  import Odometry
from std_srvs.srv import Empty

class Env:
    def __init__(self):
        ros.init_node('Env')
        ros.loginfo('Env node has been created')
        self.sub_scan = ros.Subscriber('/scan', LaserScan, self.scan, queue_size=None)
        self.sub_odom = ros.Subscriber('/odom', Odometry, self.odom, queue_size=1)
        self.pub_robot = ros.Publisher('/cmd_vel', Twist, queue_size=1)
        
        # $ rostopic hz /scan
        # $ rostopic hz /odom
        self.rate = ros.Rate(5) # 5 is the frequency of scan (we can reduce here to reduce the overhead but responsiveness will degrade)
        self.robot = Twist()
        
    def step(self, a):
        if a==0: self.left()
        if a==1: self.forward()
        if a==2: self.right()

        self.pub_robot.publish(self.robot)
        self.rate.sleep()

    def reset(self):
        self.done = False
        # reset_world service
        # $ rosservice list
        # $ rosservice info /gazebo/reset_world
        # $ rossrv show std_srvs/Empty # yeilds nothing meaning we can call() without passing arguemnt
        try:    ros.ServiceProxy('/gazebo/reset_world', Empty).call()
        except: print('could not reset world')

    def left(self):
        self.robot.linear.x  =  0
        self.robot.angular.z = .5
    def forward(self):
        self.robot.linear.x  = .5
        self.robot.angular.z =  0
    
    def right(self):
        self.robot.linear.x  =  0
        self.robot.angular.z =-.5
    
    def stop(self):
        self.robot.linear.x = 0
        self.robot.angular.z = 0
        self.pub_robot.publish(self.robot)
        self.rate.sleep()

    def scan(self, scans):
        # print(scans.range_max)
        range_max = scans.range_max
        range_min = scans.range_min + .35 # extra safty buffer to stop a bit early
        scans = np.array(scans.ranges)
        scans[scans==Inf] = range_max
        print('scans = ', scans[:10].round(2))
        self.done = scans.min() <= range_min
        self.rate.sleep()

    def odom(self, odoms):
        self.x = round(odoms.pose.pose.position.x, 3)
        self.y = round(odoms.pose.pose.position.y, 3)
        self.θ = round(odoms.pose.pose.orientation.z,3) # in python3 we can use greek letters

        print('x, y, θ =', self.x, self.y, self.θ)
        
        # disabling sleep allows us to see that odom is 5 to 6 times more frequent than scan 
        self.rate.sleep() 
        
        