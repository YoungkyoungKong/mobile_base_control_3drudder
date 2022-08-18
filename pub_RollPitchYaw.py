#!/usr/bin/env python
############### importing ###############
import time
import platform
import rospy
from std_msgs.msg import String



############### talker ###############
def talker():
   pub = rospy.Publisher('/roll_pitch_yaw_angle', String, queue_size=10)
   rospy.init_node('publish_roll_pitch_yaw', anonymous=True)
   rate = rospy.Rate(10)


   ############### receive 3DRudder data ###############
   #define status
   status_3dRudder = [ "None",
                     "Puts the 3DRudder on the floor",
                     "The 3dRudder initialize for about 2 seconds",
                     "Put your first feet on the 3dRudder",
                     "Put your second Foot on the 3dRudder",
                     "The user must wait still for half a second for calibration until a last short beep is heard from the device. The 3DRudder is ready to be used.",
                     "The 3dRudder is in use",
                     "The 3dRudder is in use and is fully operational with all the features enabled"
                     ]

   ############### run ###############
   print ("Start publisher")
   print ("------------------------")

   try:

      sdk=GetSDK()
      sdk.Init()

      nPortNumber=0


      while not sdk.IsDeviceConnected (nPortNumber):
         print("3dRudder is not Connected")
         time.sleep(1)


      version=sdk.GetVersion(nPortNumber)
      print ("Version FirmWare : {:1x}".format(version))

      print ("Get the Number of the 3dRudder are connected : {:1x}".format(sdk.GetNumberOfConnectedDevice()))

      sdk.PlaySnd(nPortNumber,1000,1000) 


      while(sdk.GetStatus(nPortNumber)<2):
         print("3drudder init...")
         time.sleep(1)

   except KeyboardInterrupt as e:
      print ("->Stop by User")
      
   except ValueError as err:
      print ("Error : ",err )

   
   #loop
   while not rospy.is_shutdown():
      #declare axis
      axis = Axis()
      print ("*****************************************************************")
      print ("Status 3dRudder : {:1} ".format(status_3dRudder[sdk.GetStatus(nPortNumber)]))
      sdk.GetAxis(0,UserRefAngle,axis)

      if (status_3dRudder[sdk.GetStatus(nPortNumber)] != "The 3dRudder is in use") & (status_3dRudder[sdk.GetStatus(nPortNumber)] != "The 3dRudder is in use and is fully operational with all the features enabled"):
         axis.m_aX = 0
         axis.m_aY = 0
         axis.m_rZ = 0

      
      axis_m_aX_str = str(axis.m_aX)
      axis_m_aY_str = str(axis.m_aY)
      axis_m_rZ_str = str(axis.m_rZ)
      print('roll angle : ' + axis_m_aX_str)
      print('pitch angle : ' + axis_m_aY_str)
      print('yaw angle : ' + axis_m_rZ_str)
      roll_pitch_yaw = axis_m_aX_str+','+axis_m_aY_str+','+axis_m_rZ_str
      pub.publish(roll_pitch_yaw)
      rate.sleep()



if __name__ == '__main__':
   try:
      val_max=platform.architecture()
      print(val_max[0])
      if (val_max[0]=='32bit') : 
         from win32.Python363.ns3DRudder import * #import SDk 3dRudder
      else:
         from x64.Python363.ns3DRudder import * #import SDk 3dRudder
      talker()
   except rospy.ROSInterruptException:
      pass