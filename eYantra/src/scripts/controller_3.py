#!/usr/bin/env python3

from geometry_msgs import msg
import rospy
# publishing to /cmd_vel with msg type: Twist
from geometry_msgs.msg import Twist, Pose2D,Pose
# subscribing to /odom with msg type: Odometry
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
# for finding sin() cos() 
import math

# Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle

hola_x = 0
hola_y = 0
hola_theta = 0

def odometryCb(msg):
    global hola_x, hola_y, hola_theta
    hola_x = msg.Pose.position.x
    hola_y = msg.Pose.position.y
    (roll, pitch, yaw) = (0, 0, hola_theta)
    quarternion = [msg.Pose.orientation.x, m sg.Pose.orientation.y, msg.Pose.orientation.z, msg.Pose.orientation.w]

    
    

        # logging once every 100 times (Gazebo runs at 1000Hz; we save it at 10Hz)
    logging_counter += 1
    if logging_counter == 100:
        logging_counter = 0
        trajectory.append([pose.x, self.pose.y])  # save trajectory
        # display (x, y, theta) on the terminal
        rospy.loginfo("odom: x=" + str(self.pose.x) +\
            ";  y=" + str(self.pose.y) + ";  theta=" + str(yaw))
 

	# Write your code to take the msg and update the three variables


def main():
	# Initialze Node
	# We'll leave this for you to figure out the syntax for 
	# initialising node named "controller"
	
	# Initialze Publisher and Subscriber
	# We'll leave this for you to figure out the syntax for
	# initialising publisher and subscriber of cmd_vel and odom respectively

	# Declare a Twist message
	vel = Twist()
	# Initialise the required variables to 0
	# <This is explained below>
	
	# For maintaining control loop rate.
	rate = rospy.Rate(100)

	# Initialise variables that may be needed for the control loop
	# For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
	# and also Kp values for the P Controller
    #
	# 
	# Control Loop goes here
	#
	#


if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass

    while not rospy.is_shutdown():

            # Find error (in x, y and theta) in global frame
            # the /odom topic is giving pose of the robot in global frame
            # the desired pose is declared above and defined by you in global frame
            # therefore calculate error in global frame

            # (Calculate error in body frame)
            # But for Controller outputs robot velocity in robot_body frame, 
            # i.e. velocity are define is in x, y of the robot frame, 
            # Notice: the direction of z axis says the same in global and body frame
            # therefore the errors will have have to be calculated in body frame.
            # 
            # This is probably the crux of Task 1, figure this out and rest should be fine.

            # Finally implement a P controller 
            # to react to the error with velocities in x, y and theta.

            # Safety Check
            # make sure the velocities are within a range.
            # for now since we are in a simulator and we are not dealing with actual physical limits on the system 
            # we may get away with skipping this step. But it will be very necessary in the long run.

            vel.linear.x = vel_x
            vel.linear.y = vel_y
            vel.angular.z = vel_z

            pub.publish(vel)
            rate.sleep()