#!/usr/bin/env python
from std_msgs.msg import String
import geometry_msgs.msg
import rospy



#print message
def callback(data):
    roll_pitch_yaw = data.data.split(',')
    roll = float(roll_pitch_yaw[0])/18
    pitch = float(roll_pitch_yaw[1])/18
    yaw = float(roll_pitch_yaw[2])/25


    if roll > 1:
        roll = 1
    if roll < -1:
        roll = -1
    if (roll < 7/18) & (roll > -7/18):
        roll = 0
    
    if pitch > 1:
        pitch = 1
    if pitch < -1:
        pitch = -1
    if (pitch < 7/18) & (pitch > -7/18):
        pitch = 0
    
    if yaw > 1:
        yaw = 1
    if yaw < -1:
        yaw = -1
    if (yaw< 12/25) & (yaw > -12/25):
        yaw= 0

    if yaw != 0:
        roll=pitch=0

    print ( "roll : "+str(roll)+", pitch : "+str(pitch)+", yaw : "+str(yaw))

    
    tw = geometry_msgs.msg.Twist()
    tw.linear.x = pitch
    tw.linear.y = -roll
    tw.angular.z = -yaw

    pub.publish(tw)

def listener():
    global pub
    rospy.init_node("control_mobile_base")
    rospy.Subscriber("/roll_pitch_yaw_angle", String, callback)
    pub = rospy.Publisher("/cmd_vel", geometry_msgs.msg.Twist, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
        
