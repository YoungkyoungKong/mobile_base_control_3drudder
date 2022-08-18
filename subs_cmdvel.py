#!/usr/bin/env python
import rospy
import geometry_msgs.msg

def callback(data):
    # R : radius of the wheel
    # l1 : x-dir distance between the center of the wheel and the center of the base
    # l2 : y-dir distance between the center of the wheel and the center of the base

    # kinematics controller
    # Please modify!
    # TO_DO
    R = 0
    l1 = 0
    l2 = 0

    Vx = data.linear.x
    Vy = data.linear.y
    Wz = data.angular.z

    w1 = (Vx - Vy - (l1 + l2) * Wz) * (1 / R)
    w2 = (Vx + Vy + (l1 + l2) * Wz) * (1 / R)
    w3 = (Vx + Vy - (l1 + l2) * Wz) * (1 / R)
    w4 = (Vx - Vy + (l1 + l2) * Wz) * (1 / R)
    
    print("w1 : " + str(w1) + ", w2 : " + str(w2) + ", w3 : " + str(w3) + ", w4 : " + str(w4))

    # run motors using w1,w2,w3,w4
    # TO_DO

def listener():
    rospy.init_node("move_mobile_base", anonymous=True)
    rospy.Subscriber("/cmd_vel", geometry_msgs.msg.Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

