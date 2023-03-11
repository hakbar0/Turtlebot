
from geometry_msgs.msg import Twist
from math import pi

def publisher():
    # Create a publisher object that publishes Twist messages to the 'cmd_vel' topic
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    # Initialize the node with the name 'Walker'
    rospy.init_node('Walker', anonymous=True)

    # Set the publishing rate to 10Hz
    rate = rospy.Rate(10)

    # Create a Twist message object with a desired velocity
    desired_velocity = Twist()

    while True:
        # Move forward for 2.5 seconds (25 iterations at 10Hz)
        desired_velocity.linear.x = 1 # Forward with 1 m/sec.
        desired_velocity.angular.z = 0.0
        for i in range(25):
            pub.publish(desired_velocity)
            rate.sleep()

        # Stop the robot for 1 second
        desired_velocity.linear.x = 0.0
        desired_velocity.angular.z = 0.0
        for i in range(10):
            pub.publish(desired_velocity)
            rate.sleep()

        # Rotate 90 degrees counterclockwise
        desired_velocity.linear.x = 0.0
        desired_velocity.angular.z = 1.0 # Rotate at 1 rad/sec (counterclockwise)
        for i in range(int(0.75 * pi * 0.35 * 10)): # Rotate for 75% of the time it takes to rotate 90 degrees
            pub.publish(desired_velocity)
            rate.sleep()
        desired_velocity.angular.z = 0.0 # Stop rotating
        pub.publish(desired_velocity)

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass