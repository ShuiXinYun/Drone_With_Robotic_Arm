# Project Drone Coupled With 6-DOF Robotic Arm Controled By Human Gesture

> This project is inspired and support by 2016 NUAA TianGong Postgraduate Innovation Cup

---

## Part 1 Robotic Arm Design

+ A 6-DOF Robotic Arm was designed with Catia and manufactured with alumunum alloys.
+ ![](./Model.jpg)

## Part 2 Control Program

+ Based on Ubuntu 14.04 with python 2.7 、PyQt4、ROS Indigo、Leap Motion SDK
+ Kinematic inverse solution for the Robotic Arm was built and UI program to interact was developed.
+ [Arm Controlled using GUI, ROS Rviz Environment](https://www.youtube.com/embed/pT87frJrrzI).
+ ![](./GUI_Motion.gif)
+ Leap Motion and Kinect program to illustrate the input of the control .
+ ![](./LeapMotion.gif)

## Part 3 Arm Servo Drive

+ Servo drive board was developed.
+ 7-sections S curve was used to adjust the speed of servo to avoid abrupt change of its angular acceleration, in which way the impact on the aircraft caused by the sudden movement of the robotic arm was eased.
+ ![](./S-Curve/S-Curve.png)
