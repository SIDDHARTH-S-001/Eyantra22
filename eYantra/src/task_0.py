#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

def move_semicircle():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    p = math.pi
    #Receiveing the user's input
    print("Let's move your robot")
    ang_speed = float(input("Input your angular speed:"))
    speed_x = float(input("Input your speed in x:"))
    angle = p
    isMove = input("Move?: ")#True or False

    #Checking if the movement is forward or backwards
    if(isMove):
        vel_msg.angular.z = abs(ang_speed)
        vel_msg.linear.x = abs(speed_x)
    else:
        vel_msg.linear.x = -abs(ang_speed)
        vel_msg.linear.x = 0
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        #Loop to move the turtle in an specified distance
        while(current_angle < p):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_angle= ang_speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.angular.z = 0
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)
        vel_msg.linear.x = 0    
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 1
        angle_z = 0
        while(angle_z <= p/2.0):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t2=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            angle_z= ang_speed*(t2-t1)
       
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)
        
        d = 2.0
        distance = 0.0
        vel_msg.linear.x = speed_x
        while (distance <= d):
            velocity_publisher.publish(vel_msg)
            t3 = rospy.Time.now().to_sec()
            distance = speed_x*(t3-t2)

        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)
        break
        

    

if __name__ == '__main__':
    try:
        #Testing our function
        move_semicircle()
    except rospy.ROSInterruptException: 
        pass