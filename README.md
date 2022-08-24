mobile_base_control_3drudder
============================

## Introduction
This is a program to control mecanum wheel mobile base using 3D Rudder.

## Prerequisites
* ROS on Windows : 
http://wiki.ros.org/Installation/Windows
* Python 3.6.3 (or maybe Python 3.5.2)
* A mecanum wheel mobile base which has a MCU to run the ROS node
* 3D Rudder (most important!)


## Getting started
1. Open ROS on Windows terminal and start roscore
```
roscore
```


2. Open another ROS terminal and run the publisher node by typing
```
py -3.6 pub_tilt.py
```


3. Open the third ROS terminal and run the middle node(it subscribes and also publishes) by typing
```
py -3.6 subs_tilt_pub_vel.py
```


4. Download 'subs_vel.py' to your mobile base MCU and run the node by typing
```
py -3.6 subs_vel.py
```
And make sure you have modified the code before running it. (```#TO_DO``` part)



5. Put your feet on the rudder and control the mobile base!


***
## Reference
* 3DRudder SDK : https://github.com/3DRudder/3DRudderPython
