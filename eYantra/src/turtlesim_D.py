#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

def T_sim_D():
    rospy.init_node('turtle_D', anonymous = True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    move_turtle = Twist()
    print("Let's move the turtle")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec

        rospy.loginfo("Turtle moves")
        move_turtle.linear.x = 1.0
        move_turtle.angular.z = 1.0
        t1 = rospy.Time.now().to_sec

        pub.publish(move_turtle)
        rate.sleep()

        # sleep()
'''
        t = t1-t0
        angle = 0
        angle = move_turtle.angular.z*t'''

if __name__ == '__main__':
    try:
        T_sim_D()
        time,time.sleep(1)
    except:
        rospy.ROSInterruptException




