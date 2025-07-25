#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def callback(msg):
    # print('X: %s, Y: %s' % (msg.pose.pose.position.x, msg.pose.pose.position.y))
    print("yes")

def main():
    sub = rospy.Subscriber('/cmd_vel', Twist, callback)
    #pub = rospy.Publisher('/odom', Odometry, queue_size=10)
    rospy.init_node('exercise_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    #     msg = Twist()
    #     msg.angular.z = 0.3
    #     msg.linear.x = 0.3
    #     pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass