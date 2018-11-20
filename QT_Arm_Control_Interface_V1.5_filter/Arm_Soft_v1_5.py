# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Arm_Soft_v1_4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName(_fromUtf8("Mainwindow"))
        Mainwindow.resize(995, 638)
        #########################################################
        self.joint_values=[45.0,45.0,45.0,45.0,45.0,45.0,0.0,0.0]
        self.random_angles=[45.0,45.0,45.0,45.0,45.0,45.0,0.0,0.0]
        self.submit_joint_values=[45.0,45.0,45.0,45.0,45.0,45.0,0.0,0.0]
        self.tip_inverse_position=[0.0,0.0,0.0,0,0]
        self.joint_value_limit=[[0.0,90.0],[0.0,90.0],[0.0,90.0],[0.0,90.0],[0.0,90.0],[0.0,90.0],[0.0,90.0]]
        self.is_stand_by=False
        self.is_simulation_mode_on=False
        self.is_joint_angle_control_on=False
        self.is_tip_inverse_control_on=False
        self.is_leapmotion_control_mode_on=False
        self.is_servo_speed_fast=False
        self.is_servo_speed_medium=True
        self.is_servo_speed_slow=False
        self.is_submit_value_correct=[True,True,True,True,True,True,True]
        #########################################################
        self.centralwidget = QtGui.QWidget(Mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_standby = QtGui.QPushButton(self.centralwidget)
        self.button_standby.setGeometry(QtCore.QRect(520, 360, 161, 61))
        self.button_standby.setObjectName(_fromUtf8("button_standby"))
        self.slider_joint1 = QtGui.QSlider(self.centralwidget)
        self.slider_joint1.setGeometry(QtCore.QRect(100, 80, 341, 21))
        self.slider_joint1.setMinimum(0)
        self.slider_joint1.setMaximum(900)
        self.slider_joint1.setSliderPosition(450)
        self.slider_joint1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_joint1.setObjectName(_fromUtf8("slider_joint1"))
        self.slider_joint2 = QtGui.QSlider(self.centralwidget)
        self.slider_joint2.setGeometry(QtCore.QRect(100, 130, 341, 21))
        self.slider_joint2.setMinimum(0)
        self.slider_joint2.setMaximum(900)
        self.slider_joint2.setSliderPosition(450)
        self.slider_joint2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_joint2.setObjectName(_fromUtf8("slider_joint2"))
        self.slider_joint3 = QtGui.QSlider(self.centralwidget)
        self.slider_joint3.setGeometry(QtCore.QRect(100, 180, 341, 21))
        self.slider_joint3.setMinimum(0)
        self.slider_joint3.setMaximum(900)
        self.slider_joint3.setSliderPosition(450)
        self.slider_joint3.setOrientation(QtCore.Qt.Horizontal)
        self.slider_joint3.setObjectName(_fromUtf8("slider_joint3"))
        self.slider_joint4 = QtGui.QSlider(self.centralwidget)
        self.slider_joint4.setGeometry(QtCore.QRect(100, 230, 341, 21))
        self.slider_joint4.setMinimum(0)
        self.slider_joint4.setMaximum(900)
        self.slider_joint4.setSliderPosition(450)
        self.slider_joint4.setOrientation(QtCore.Qt.Horizontal)
        self.slider_joint4.setObjectName(_fromUtf8("slider_joint4"))
        self.slider_joint5 = QtGui.QSlider(self.centralwidget)
        self.slider_joint5.setGeometry(QtCore.QRect(100, 280, 341, 21))
        self.slider_joint5.setMinimum(0)
        self.slider_joint5.setMaximum(900)
        self.slider_joint5.setSliderPosition(450)
        self.slider_joint5.setOrientation(QtCore.Qt.Horizontal)
        self.slider_joint5.setObjectName(_fromUtf8("slider_joint5"))
        self.slider_joint6 = QtGui.QSlider(self.centralwidget)
        self.slider_joint6.setGeometry(QtCore.QRect(100, 330, 341, 21))
        self.slider_joint6.setMinimum(0)
        self.slider_joint6.setMaximum(900)
        self.slider_joint6.setSliderPosition(450)
        self.slider_joint6.setOrientation(QtCore.Qt.Horizontal)
        self.slider_joint6.setObjectName(_fromUtf8("slider_joint6"))
        self.slider_hand_open = QtGui.QSlider(self.centralwidget)
        self.slider_hand_open.setGeometry(QtCore.QRect(100, 380, 341, 21))
        self.slider_hand_open.setMinimum(0)
        self.slider_hand_open.setMaximum(600)
        self.slider_hand_open.setSliderPosition(0)
        self.slider_hand_open.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hand_open.setObjectName(_fromUtf8("slider_hand_open"))
        self.label_joint1 = QtGui.QLabel(self.centralwidget)
        self.label_joint1.setGeometry(QtCore.QRect(30, 80, 51, 20))
        self.label_joint1.setTextFormat(QtCore.Qt.AutoText)
        self.label_joint1.setScaledContents(False)
        self.label_joint1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_joint1.setWordWrap(False)
        self.label_joint1.setIndent(0)
        self.label_joint1.setObjectName(_fromUtf8("label_joint1"))
        self.label_joint2 = QtGui.QLabel(self.centralwidget)
        self.label_joint2.setGeometry(QtCore.QRect(30, 130, 51, 20))
        self.label_joint2.setTextFormat(QtCore.Qt.AutoText)
        self.label_joint2.setScaledContents(False)
        self.label_joint2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_joint2.setWordWrap(False)
        self.label_joint2.setIndent(0)
        self.label_joint2.setObjectName(_fromUtf8("label_joint2"))
        self.label_joint3 = QtGui.QLabel(self.centralwidget)
        self.label_joint3.setGeometry(QtCore.QRect(30, 180, 51, 20))
        self.label_joint3.setTextFormat(QtCore.Qt.AutoText)
        self.label_joint3.setScaledContents(False)
        self.label_joint3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_joint3.setWordWrap(False)
        self.label_joint3.setIndent(0)
        self.label_joint3.setObjectName(_fromUtf8("label_joint3"))
        self.label_joint4 = QtGui.QLabel(self.centralwidget)
        self.label_joint4.setGeometry(QtCore.QRect(30, 230, 51, 16))
        self.label_joint4.setTextFormat(QtCore.Qt.AutoText)
        self.label_joint4.setScaledContents(False)
        self.label_joint4.setWordWrap(False)
        self.label_joint4.setIndent(0)
        self.label_joint4.setObjectName(_fromUtf8("label_joint4"))
        self.label_joint5 = QtGui.QLabel(self.centralwidget)
        self.label_joint5.setGeometry(QtCore.QRect(30, 280, 51, 16))
        self.label_joint5.setTextFormat(QtCore.Qt.AutoText)
        self.label_joint5.setScaledContents(False)
        self.label_joint5.setWordWrap(False)
        self.label_joint5.setIndent(0)
        self.label_joint5.setObjectName(_fromUtf8("label_joint5"))
        self.label_joint6 = QtGui.QLabel(self.centralwidget)
        self.label_joint6.setGeometry(QtCore.QRect(30, 330, 51, 16))
        self.label_joint6.setTextFormat(QtCore.Qt.AutoText)
        self.label_joint6.setScaledContents(False)
        self.label_joint6.setWordWrap(False)
        self.label_joint6.setIndent(0)
        self.label_joint6.setObjectName(_fromUtf8("label_joint6"))
        self.textlabel_joint1 = QtGui.QLabel(self.centralwidget)
        self.textlabel_joint1.setGeometry(QtCore.QRect(450, 80, 31, 20))
        self.textlabel_joint1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textlabel_joint1.setScaledContents(False)
        self.textlabel_joint1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textlabel_joint1.setObjectName(_fromUtf8("textlabel_joint1"))
        self.textlabel_joint2 = QtGui.QLabel(self.centralwidget)
        self.textlabel_joint2.setGeometry(QtCore.QRect(450, 130, 31, 20))
        self.textlabel_joint2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textlabel_joint2.setObjectName(_fromUtf8("textlabel_joint2"))
        self.textlabel_joint3 = QtGui.QLabel(self.centralwidget)
        self.textlabel_joint3.setGeometry(QtCore.QRect(450, 180, 31, 20))
        self.textlabel_joint3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textlabel_joint3.setObjectName(_fromUtf8("textlabel_joint3"))
        self.textlabel_joint4 = QtGui.QLabel(self.centralwidget)
        self.textlabel_joint4.setGeometry(QtCore.QRect(450, 230, 31, 20))
        self.textlabel_joint4.setObjectName(_fromUtf8("textlabel_joint4"))
        self.textlabel_joint5 = QtGui.QLabel(self.centralwidget)
        self.textlabel_joint5.setGeometry(QtCore.QRect(450, 280, 31, 20))
        self.textlabel_joint5.setObjectName(_fromUtf8("textlabel_joint5"))
        self.textlabel_joint6 = QtGui.QLabel(self.centralwidget)
        self.textlabel_joint6.setGeometry(QtCore.QRect(450, 330, 31, 20))
        self.textlabel_joint6.setObjectName(_fromUtf8("textlabel_joint6"))
        self.label_Joint_Angle_Control = QtGui.QLabel(self.centralwidget)
        self.label_Joint_Angle_Control.setGeometry(QtCore.QRect(150, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(12)
        font.setItalic(False)
        self.label_Joint_Angle_Control.setFont(font)
        self.label_Joint_Angle_Control.setTextFormat(QtCore.Qt.AutoText)
        self.label_Joint_Angle_Control.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Joint_Angle_Control.setWordWrap(False)
        self.label_Joint_Angle_Control.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_Joint_Angle_Control.setObjectName(_fromUtf8("label_Joint_Angle_Control"))
        self.label_hand_open = QtGui.QLabel(self.centralwidget)
        self.label_hand_open.setGeometry(QtCore.QRect(10, 380, 81, 16))
        self.label_hand_open.setTextFormat(QtCore.Qt.AutoText)
        self.label_hand_open.setScaledContents(False)
        self.label_hand_open.setWordWrap(False)
        self.label_hand_open.setIndent(0)
        self.label_hand_open.setObjectName(_fromUtf8("label_hand_open"))
        
        self.textlabel_hand_open = QtGui.QLabel(self.centralwidget)
        self.textlabel_hand_open.setGeometry(QtCore.QRect(450, 380, 31, 16))
        self.textlabel_hand_open.setObjectName(_fromUtf8("textlabel_hand_open"))
        self.lineEdit_joint1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_joint1.setGeometry(QtCore.QRect(10, 460, 51, 23))
        self.lineEdit_joint1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_joint1.setObjectName(_fromUtf8("lineEdit_joint1"))
        self.lineEdit_joint2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_joint2.setGeometry(QtCore.QRect(80, 460, 51, 23))
        self.lineEdit_joint2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_joint2.setObjectName(_fromUtf8("lineEdit_joint2"))
        self.lineEdit_joint3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_joint3.setGeometry(QtCore.QRect(150, 460, 51, 23))
        self.lineEdit_joint3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_joint3.setObjectName(_fromUtf8("lineEdit_joint3"))
        self.lineEdit_joint4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_joint4.setGeometry(QtCore.QRect(220, 460, 51, 23))
        self.lineEdit_joint4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_joint4.setObjectName(_fromUtf8("lineEdit_joint4"))
        self.lineEdit_joint5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_joint5.setGeometry(QtCore.QRect(290, 460, 51, 23))
        self.lineEdit_joint5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_joint5.setObjectName(_fromUtf8("lineEdit_joint5"))
        self.lineEdit_joint6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_joint6.setGeometry(QtCore.QRect(360, 460, 51, 23))
        self.lineEdit_joint6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_joint6.setObjectName(_fromUtf8("lineEdit_joint6"))
        self.lineEdit_hand_open = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_hand_open.setGeometry(QtCore.QRect(430, 460, 51, 23))
        self.lineEdit_hand_open.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_hand_open.setObjectName(_fromUtf8("lineEdit_hand_open"))
        self.pushButton_angle_submit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_angle_submit.setGeometry(QtCore.QRect(300, 530, 120, 40))
        self.pushButton_angle_submit.setObjectName(_fromUtf8("pushButton_angle_submit"))
        self.pushButton_angle_random = QtGui.QPushButton(self.centralwidget)
        self.pushButton_angle_random.setGeometry(QtCore.QRect(60, 530, 120, 40))
        self.pushButton_angle_random.setObjectName(_fromUtf8("pushButton_angle_random"))
        self.label_joint1_limit = QtGui.QLabel(self.centralwidget)
        self.label_joint1_limit.setGeometry(QtCore.QRect(10, 490, 55, 16))
        self.label_joint1_limit.setObjectName(_fromUtf8("label_joint1_limit"))
        self.label_joint2_limit = QtGui.QLabel(self.centralwidget)
        self.label_joint2_limit.setGeometry(QtCore.QRect(80, 490, 55, 16))
        self.label_joint2_limit.setObjectName(_fromUtf8("label_joint2_limit"))
        self.label_joint3_limit = QtGui.QLabel(self.centralwidget)
        self.label_joint3_limit.setGeometry(QtCore.QRect(150, 490, 55, 16))
        self.label_joint3_limit.setObjectName(_fromUtf8("label_joint3_limit"))
        self.label_joint4_limit = QtGui.QLabel(self.centralwidget)
        self.label_joint4_limit.setGeometry(QtCore.QRect(220, 490, 55, 16))
        self.label_joint4_limit.setObjectName(_fromUtf8("label_joint4_limit"))
        self.label_joint5_limit = QtGui.QLabel(self.centralwidget)
        self.label_joint5_limit.setGeometry(QtCore.QRect(290, 490, 55, 16))
        self.label_joint5_limit.setObjectName(_fromUtf8("label_joint5_limit"))
        self.label_joint6_limit = QtGui.QLabel(self.centralwidget)
        self.label_joint6_limit.setGeometry(QtCore.QRect(360, 490, 61, 16))
        self.label_joint6_limit.setObjectName(_fromUtf8("label_joint6_limit"))
        self.label_hand_open_limit = QtGui.QLabel(self.centralwidget)
        self.label_hand_open_limit.setGeometry(QtCore.QRect(430, 490, 55, 16))
        self.label_hand_open_limit.setObjectName(_fromUtf8("label_hand_open_limit"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(510, 460, 461, 111))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(470, 10, 31, 571))
        self.line_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_1 = QtGui.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(10, 50, 471, 20))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 420, 471, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_version = QtGui.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(780, 570, 211, 31))
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName(_fromUtf8("label_version"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(490, 420, 501, 21))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 440, 211, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox_simulation_mode = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_simulation_mode.setGeometry(QtCore.QRect(500, 50, 261, 21))
        #self.checkBox_simulation_mode.setChecked(True)
        self.checkBox_simulation_mode.setObjectName(_fromUtf8("checkBox_simulation_mode"))
        self.checkBox_Leapmotion_mode = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_Leapmotion_mode.setGeometry(QtCore.QRect(780, 80, 201, 21))
        self.checkBox_Leapmotion_mode.setChecked(False)
        self.checkBox_Leapmotion_mode.setObjectName(_fromUtf8("checkBox_Leapmotion_mode"))
        self.checkBox_joint_angle_control_mode = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_joint_angle_control_mode.setGeometry(QtCore.QRect(500, 80, 221, 21))
        self.checkBox_joint_angle_control_mode.setChecked(False)
        self.checkBox_joint_angle_control_mode.setObjectName(_fromUtf8("checkBox_joint_angle_control_mode"))
        self.checkBox_tip_inverse_control_mode = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_tip_inverse_control_mode.setGeometry(QtCore.QRect(780, 50, 201, 21))
        self.checkBox_tip_inverse_control_mode.setChecked(False)
        self.checkBox_tip_inverse_control_mode.setObjectName(_fromUtf8("checkBox_tip_inverse_control_mode"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(490, 340, 501, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_control_model = QtGui.QLabel(self.centralwidget)
        self.label_control_model.setGeometry(QtCore.QRect(510, 10, 451, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_control_model.setFont(font)
        self.label_control_model.setAlignment(QtCore.Qt.AlignCenter)
        self.label_control_model.setObjectName(_fromUtf8("label_control_model"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox_servo_speed_fast = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_servo_speed_fast.setGeometry(QtCore.QRect(860, 345, 85, 31))
        self.checkBox_servo_speed_fast.setObjectName(_fromUtf8("checkBox_servo_speed_fast"))
        self.checkBox_servo_speed_Medium = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_servo_speed_Medium.setGeometry(QtCore.QRect(860, 375, 85, 31))
        self.checkBox_servo_speed_Medium.setChecked(True)
        self.checkBox_servo_speed_Medium.setObjectName(_fromUtf8("checkBox_servo_speed_Medium"))
        self.checkBox_servo_speed_Slow = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_servo_speed_Slow.setGeometry(QtCore.QRect(860, 410, 85, 21))
        self.checkBox_servo_speed_Slow.setObjectName(_fromUtf8("checkBox_servo_speed_Slow"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(500, 29, 481, 31))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(490, 100, 501, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(820, 381, 31, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(820, 360, 21, 61))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(830, 350, 21, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(830, 410, 21, 20))
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.label_tip_inverse_control = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_control.setGeometry(QtCore.QRect(570, 115, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_tip_inverse_control.setFont(font)
        self.label_tip_inverse_control.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_control.setObjectName(_fromUtf8("label_tip_inverse_control"))
        self.verticalSlider_tip_inverse_x = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_tip_inverse_x.setGeometry(QtCore.QRect(570, 170, 20, 151))
        self.verticalSlider_tip_inverse_x.setMinimum(-20)
        self.verticalSlider_tip_inverse_x.setMaximum(20)
        self.verticalSlider_tip_inverse_x.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_tip_inverse_x.setObjectName(_fromUtf8("verticalSlider_tip_inverse_x"))
        self.verticalSlider_tip_inverse_y = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_tip_inverse_y.setGeometry(QtCore.QRect(650, 170, 20, 151))
        self.verticalSlider_tip_inverse_y.setMinimum(-20)
        self.verticalSlider_tip_inverse_y.setMaximum(20)
        self.verticalSlider_tip_inverse_y.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_tip_inverse_y.setObjectName(_fromUtf8("verticalSlider_tip_inverse_y"))
        self.verticalSlider_tip_inverse_z = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_tip_inverse_z.setGeometry(QtCore.QRect(730, 170, 20, 151))
        self.verticalSlider_tip_inverse_z.setMinimum(-20)
        self.verticalSlider_tip_inverse_z.setMaximum(20)
        self.verticalSlider_tip_inverse_z.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_tip_inverse_z.setObjectName(_fromUtf8("verticalSlider_tip_inverse_z"))
        self.verticalSlider_tip_inverse_pitch = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_tip_inverse_pitch.setGeometry(QtCore.QRect(810, 170, 20, 151))
        self.verticalSlider_tip_inverse_pitch.setMinimum(0)
        self.verticalSlider_tip_inverse_pitch.setMaximum(90)
        self.verticalSlider_tip_inverse_pitch.setSliderPosition(45)
        self.verticalSlider_tip_inverse_pitch.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_tip_inverse_pitch.setObjectName(_fromUtf8("verticalSlider_tip_inverse_pitch"))
        self.verticalSlider_tip_inverse_roll = QtGui.QSlider(self.centralwidget)
        self.verticalSlider_tip_inverse_roll.setGeometry(QtCore.QRect(890, 170, 21, 151))
        self.verticalSlider_tip_inverse_roll.setMinimum(0)
        self.verticalSlider_tip_inverse_roll.setMaximum(90)
        self.verticalSlider_tip_inverse_roll.setSliderPosition(45)
        self.verticalSlider_tip_inverse_roll.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_tip_inverse_roll.setObjectName(_fromUtf8("verticalSlider_tip_inverse_roll"))
        self.label_tip_inverse_x = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_x.setGeometry(QtCore.QRect(560, 135, 41, 21))
        self.label_tip_inverse_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_x.setObjectName(_fromUtf8("label_tip_inverse_x"))
        self.label_tip_inverse_limit_x = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_limit_x.setGeometry(QtCore.QRect(550, 150, 61, 21))
        self.label_tip_inverse_limit_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_limit_x.setObjectName(_fromUtf8("label_tip_inverse_limit_x"))
        self.label_tip_inverse_y = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_y.setGeometry(QtCore.QRect(640, 136, 41, 20))
        self.label_tip_inverse_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_y.setObjectName(_fromUtf8("label_tip_inverse_y"))
        self.label_tip_inverse_z = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_z.setGeometry(QtCore.QRect(720, 136, 41, 20))
        self.label_tip_inverse_z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_z.setObjectName(_fromUtf8("label_tip_inverse_z"))
        self.label_tip_inverse_pitch = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_pitch.setGeometry(QtCore.QRect(800, 135, 41, 21))
        self.label_tip_inverse_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_pitch.setObjectName(_fromUtf8("label_tip_inverse_pitch"))
        self.label_tip_inverse_roll = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_roll.setGeometry(QtCore.QRect(880, 135, 41, 21))
        self.label_tip_inverse_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_roll.setObjectName(_fromUtf8("label_tip_inverse_roll"))
        self.label_tip_inverse_limit_x_2 = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_limit_x_2.setGeometry(QtCore.QRect(630, 150, 61, 21))
        self.label_tip_inverse_limit_x_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_limit_x_2.setObjectName(_fromUtf8("label_tip_inverse_limit_x_2"))
        self.label_tip_inverse_limit_x_3 = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_limit_x_3.setGeometry(QtCore.QRect(710, 150, 61, 21))
        self.label_tip_inverse_limit_x_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_limit_x_3.setObjectName(_fromUtf8("label_tip_inverse_limit_x_3"))
        self.label_tip_inverse_limit_x_4 = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_limit_x_4.setGeometry(QtCore.QRect(790, 150, 61, 21))
        self.label_tip_inverse_limit_x_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_limit_x_4.setObjectName(_fromUtf8("label_tip_inverse_limit_x_4"))
        self.label_tip_inverse_limit_x_5 = QtGui.QLabel(self.centralwidget)
        self.label_tip_inverse_limit_x_5.setGeometry(QtCore.QRect(870, 150, 61, 21))
        self.label_tip_inverse_limit_x_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tip_inverse_limit_x_5.setObjectName(_fromUtf8("label_tip_inverse_limit_x_5"))
        self.textlabel_tip_inverse_x = QtGui.QLabel(self.centralwidget)
        self.textlabel_tip_inverse_x.setGeometry(QtCore.QRect(560, 320, 41, 21))
        self.textlabel_tip_inverse_x.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel_tip_inverse_x.setObjectName(_fromUtf8("textlabel_tip_inverse_x"))
        self.textlabel_tip_inverse_y = QtGui.QLabel(self.centralwidget)
        self.textlabel_tip_inverse_y.setGeometry(QtCore.QRect(640, 320, 41, 21))
        self.textlabel_tip_inverse_y.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel_tip_inverse_y.setObjectName(_fromUtf8("textlabel_tip_inverse_y"))
        self.textlabel_tip_inverse_z = QtGui.QLabel(self.centralwidget)
        self.textlabel_tip_inverse_z.setGeometry(QtCore.QRect(720, 320, 41, 21))
        self.textlabel_tip_inverse_z.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel_tip_inverse_z.setObjectName(_fromUtf8("textlabel_tip_inverse_z"))
        self.textlabel_tip_inverse_pitch = QtGui.QLabel(self.centralwidget)
        self.textlabel_tip_inverse_pitch.setGeometry(QtCore.QRect(800, 320, 41, 21))
        self.textlabel_tip_inverse_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel_tip_inverse_pitch.setObjectName(_fromUtf8("textlabel_tip_inverse_pitch"))
        self.textlabel_tip_inverse_roll = QtGui.QLabel(self.centralwidget)
        self.textlabel_tip_inverse_roll.setGeometry(QtCore.QRect(880, 320, 41, 21))
        self.textlabel_tip_inverse_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel_tip_inverse_roll.setObjectName(_fromUtf8("textlabel_tip_inverse_roll"))
        
        Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)
        ######################################################
        QtCore.QObject.connect(self.button_standby,QtCore.SIGNAL("clicked()"), self.stand_by)
        QtCore.QObject.connect(self.pushButton_angle_submit,QtCore.SIGNAL("clicked()"),self.submit_angle)
        QtCore.QObject.connect(self.pushButton_angle_random, QtCore.SIGNAL("clicked()"), self.random_angle)
        self.slider_joint1.valueChanged.connect(self.joint1_value_changed)
        self.slider_joint2.valueChanged.connect(self.joint2_value_changed)
        self.slider_joint3.valueChanged.connect(self.joint3_value_changed)
        self.slider_joint4.valueChanged.connect(self.joint4_value_changed)
        self.slider_joint5.valueChanged.connect(self.joint5_value_changed)
        self.slider_joint6.valueChanged.connect(self.joint6_value_changed)
        self.slider_hand_open.valueChanged.connect(self.hand_open_value_changed)
        self.lineEdit_joint1.textChanged.connect(self.submit_joint1_changed)
        self.lineEdit_joint2.textChanged.connect(self.submit_joint2_changed)
        self.lineEdit_joint3.textChanged.connect(self.submit_joint3_changed)
        self.lineEdit_joint4.textChanged.connect(self.submit_joint4_changed)
        self.lineEdit_joint5.textChanged.connect(self.submit_joint5_changed)
        self.lineEdit_joint6.textChanged.connect(self.submit_joint6_changed)
        self.lineEdit_hand_open.textChanged.connect(self.submit_hand_open_changed)
        self.verticalSlider_tip_inverse_x.valueChanged.connect(self.tip_inversed_x_changed)
        self.verticalSlider_tip_inverse_y.valueChanged.connect(self.tip_inversed_y_changed)
        self.verticalSlider_tip_inverse_z.valueChanged.connect(self.tip_inversed_z_changed)
        self.verticalSlider_tip_inverse_pitch.valueChanged.connect(self.tip_inversed_pitch_changed)
        self.verticalSlider_tip_inverse_roll.valueChanged.connect(self.tip_inversed_roll_changed)
        self.checkBox_simulation_mode.stateChanged.connect(self.simulation_state_changed)
        self.checkBox_simulation_mode.toggle()
        self.checkBox_Leapmotion_mode.stateChanged.connect(self.leapmotion_state_changed)
        self.checkBox_joint_angle_control_mode.stateChanged.connect(self.joint_angle_control_state_changed)
        self.checkBox_tip_inverse_control_mode.stateChanged.connect(self.tip_inverse_control_state_changed)
        self.checkBox_servo_speed_fast.stateChanged.connect(self.servo_speed_fast_state_changed)
        self.checkBox_servo_speed_Medium.stateChanged.connect(self.servo_speed_medium_state_changed)
        self.checkBox_servo_speed_Slow.stateChanged.connect(self.servo_speed_slow_state_changed)
        ##################################################
    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(_translate("Mainwindow", "Arm Control  Interface", None))
        self.button_standby.setText(_translate("Mainwindow", "Standing By... ...", None))
        self.label_joint1.setText(_translate("Mainwindow", "Joint1", None))
        self.label_joint2.setText(_translate("Mainwindow", "Joint2", None))
        self.label_joint3.setText(_translate("Mainwindow", "Joint3", None))
        self.label_joint4.setText(_translate("Mainwindow", "Joint4", None))
        self.label_joint5.setText(_translate("Mainwindow", "Joint5", None))
        self.label_joint6.setText(_translate("Mainwindow", "Joint6", None))
        self.textlabel_joint1.setText(_translate("Mainwindow", "45.0", None))
        self.textlabel_joint2.setText(_translate("Mainwindow", "65.0", None))
        self.textlabel_joint3.setText(_translate("Mainwindow", "45.0", None))
        self.textlabel_joint4.setText(_translate("Mainwindow", "45.0", None))
        self.textlabel_joint5.setText(_translate("Mainwindow", "45.0", None))
        self.textlabel_joint6.setText(_translate("Mainwindow", "45.0", None))
        self.label_Joint_Angle_Control.setText(_translate("Mainwindow", "Joint Angle Control", None))
        self.label_hand_open.setText(_translate("Mainwindow", "Hand Open", None))
        self.textlabel_hand_open.setText(_translate("Mainwindow", "0.0", None))
        self.pushButton_angle_submit.setText(_translate("Mainwindow", "Submit", None))
        self.pushButton_angle_random.setText(_translate("Mainwindow", "Random", None))
        self.label_joint1_limit.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_joint2_limit.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_joint3_limit.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_joint4_limit.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_joint5_limit.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_joint6_limit.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_hand_open_limit.setText(_translate("Mainwindow", "[0     60]", None))
        self.label_version.setText(_translate("Mainwindow", "Arm Control Interface v1.5", None))
        self.label.setText(_translate("Mainwindow", "Message Box", None))
        self.checkBox_simulation_mode.setText(_translate("Mainwindow", "Simulation Mode(Data Trans Off)", None))
        self.checkBox_Leapmotion_mode.setText(_translate("Mainwindow", "Leapmotion Control Mode", None))
        self.checkBox_joint_angle_control_mode.setText(_translate("Mainwindow", "Joint Angle Control Mode", None))
        self.checkBox_tip_inverse_control_mode.setText(_translate("Mainwindow", "Tip Inverse Control Mode", None))
        self.label_control_model.setText(_translate("Mainwindow", "Control Model", None))
        self.label_2.setText(_translate("Mainwindow", "Servo Speed", None))
        self.checkBox_servo_speed_fast.setText(_translate("Mainwindow", "Fast", None))
        self.checkBox_servo_speed_Medium.setText(_translate("Mainwindow", "Medium", None))
        self.checkBox_servo_speed_Slow.setText(_translate("Mainwindow", "Slow", None))
        self.label_tip_inverse_control.setText(_translate("Mainwindow", "Tip Inverse Control", None))
        self.label_tip_inverse_x.setText(_translate("Mainwindow", "X", None))
        self.label_tip_inverse_limit_x.setText(_translate("Mainwindow", "[-0.2 0.2]", None))
        self.label_tip_inverse_y.setText(_translate("Mainwindow", "Y", None))
        self.label_tip_inverse_z.setText(_translate("Mainwindow", "Z", None))
        self.label_tip_inverse_pitch.setText(_translate("Mainwindow", "Pitch", None))
        self.label_tip_inverse_roll.setText(_translate("Mainwindow", "Roll", None))
        self.label_tip_inverse_limit_x_2.setText(_translate("Mainwindow", "[-0.2 0.2]", None))
        self.label_tip_inverse_limit_x_3.setText(_translate("Mainwindow", "[-0.2 0.2]", None))
        self.label_tip_inverse_limit_x_4.setText(_translate("Mainwindow", "[0     90]", None))
        self.label_tip_inverse_limit_x_5.setText(_translate("Mainwindow", "[0     90]", None))
        self.textlabel_tip_inverse_x.setText(_translate("Mainwindow", "0.0", None))
        self.textlabel_tip_inverse_y.setText(_translate("Mainwindow", "0.0", None))
        self.textlabel_tip_inverse_z.setText(_translate("Mainwindow", "0.0", None))
        self.textlabel_tip_inverse_pitch.setText(_translate("Mainwindow", "45", None))
        self.textlabel_tip_inverse_roll.setText(_translate("Mainwindow", "45", None))

###############################################################
    def stand_by(self):
        self.is_stand_by=True
        self.joint_values=[45.0,45.0,45.0,45.0,45.0,45.0,0.0,0.0]
        self.submit_joint_values=[45.0,45.0,45.0,45.0,45.0,45.0,0.0,0.0]
        self.tip_inverse_position=[0.0,0.0,0.0,45,45]
        self.slider_joint1.setValue(self.joint_values[0]*10)
        self.slider_joint2.setValue(self.joint_values[1]*10)
        self.slider_joint3.setValue(self.joint_values[2]*10)
        self.slider_joint4.setValue(self.joint_values[3]*10)
        self.slider_joint5.setValue(self.joint_values[4]*10)
        self.slider_joint6.setValue(self.joint_values[5]*10)
        self.slider_hand_open.setValue(self.joint_values[6]*10)
        self.verticalSlider_tip_inverse_x.setValue(self.tip_inverse_position[0])
        self.verticalSlider_tip_inverse_y.setValue(self.tip_inverse_position[1])
        self.verticalSlider_tip_inverse_z.setValue(self.tip_inverse_position[2])
        self.verticalSlider_tip_inverse_pitch.setValue(self.tip_inverse_position[3])
        self.verticalSlider_tip_inverse_roll.setValue(self.tip_inverse_position[4])
        self.textlabel_joint1.setText(str(self.joint_values[0]))
        self.textlabel_joint2.setText(str(self.joint_values[1]))
        self.textlabel_joint3.setText(str(self.joint_values[2]))
        self.textlabel_joint4.setText(str(self.joint_values[3]))
        self.textlabel_joint5.setText(str(self.joint_values[4]))
        self.textlabel_joint6.setText(str(self.joint_values[5]))
        self.textlabel_hand_open.setText(str(self.joint_values[6]))
        self.textlabel_tip_inverse_x.setText(str(self.tip_inverse_position[0]))
        self.textlabel_tip_inverse_y.setText(str(self.tip_inverse_position[1]))
        self.textlabel_tip_inverse_z.setText(str(self.tip_inverse_position[2]))
        self.textlabel_tip_inverse_pitch.setText(str(self.tip_inverse_position[3]))
        self.textlabel_tip_inverse_roll.setText(str(self.tip_inverse_position[4]))
        self.lineEdit_joint1.setText(str(self.joint_values[0]))
        self.lineEdit_joint2.setText(str(self.joint_values[1]))
        self.lineEdit_joint3.setText(str(self.joint_values[2]))
        self.lineEdit_joint4.setText(str(self.joint_values[3]))
        self.lineEdit_joint5.setText(str(self.joint_values[4]))
        self.lineEdit_joint6.setText(str(self.joint_values[5]))
        self.lineEdit_hand_open.setText(str(self.joint_values[6]))
        self.is_stand_by=False
        self.textBrowser.setText('Standing By... ... ;\n Joint Values '+str(self.joint_values))
        #print 'Standing By... ...',self.joint_values
        
    def joint1_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[0]=self.slider_joint1.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.textlabel_joint1.setText(str(self.joint_values[0]))
            #print self.joint_values
    def joint2_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[1]=self.slider_joint2.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.textlabel_joint2.setText(str(self.joint_values[1]))
            #print self.joint_values
    def joint3_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[2]=self.slider_joint3.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.textlabel_joint3.setText(str(self.joint_values[2]))
            #print self.joint_values
    def joint4_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[3]=self.slider_joint4.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.textlabel_joint4.setText(str(self.joint_values[3]))
            #print self.joint_values
    def joint5_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[4]=self.slider_joint5.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.textlabel_joint5.setText(str(self.joint_values[4]))
            #print self.joint_values
    def joint6_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[5]=self.slider_joint6.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.textlabel_joint6.setText(str(self.joint_values[5]))
            #print self.joint_values
    def hand_open_value_changed(self):
        if not self.is_stand_by and self.is_joint_angle_control_on==True:
            self.joint_values[6]=self.slider_hand_open.value()/10.0
            self.textBrowser.setText('Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.joint_values[7]=-self.slider_hand_open.value()/10.0
            self.textlabel_hand_open.setText(str(self.joint_values[6]))
    def submit_joint1_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[0][0]<=int(self.lineEdit_joint1.text())<=self.joint_value_limit[0][1]:
                    self.submit_joint_values[0]=int(self.lineEdit_joint1.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[0]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[0]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[0]=False
            pass
    def submit_joint2_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[1][0]<=int(self.lineEdit_joint2.text())<=self.joint_value_limit[1][1]:
                    self.submit_joint_values[1]=int(self.lineEdit_joint2.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[1]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[1]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[1]=False
            pass
    def submit_joint3_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[2][0]<=int(self.lineEdit_joint3.text())<=self.joint_value_limit[2][1]:
                    self.submit_joint_values[2]=int(self.lineEdit_joint3.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[2]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[2]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[2]=False
            pass
    def submit_joint4_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[3][0]<=int(self.lineEdit_joint4.text())<=self.joint_value_limit[3][1]:
                    self.submit_joint_values[3]=int(self.lineEdit_joint4.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[3]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[3]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[3]=False
            pass
    def submit_joint5_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[4][0]<=int(self.lineEdit_joint5.text())<=self.joint_value_limit[4][1]:
                    self.submit_joint_values[4]=int(self.lineEdit_joint5.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[4]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[4]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[4]=False
            pass
    def submit_joint6_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[5][0]<=int(self.lineEdit_joint6.text())<=self.joint_value_limit[5][1]:
                    self.submit_joint_values[5]=int(self.lineEdit_joint6.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[5]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[5]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[5]=False
            pass
    def submit_hand_open_changed(self):
        try:
            if not self.is_stand_by and self.is_joint_angle_control_on==True:
                if self.joint_value_limit[6][0]<=int(self.lineEdit_hand_open.text())<=self.joint_value_limit[6][1]:
                    self.submit_joint_values[6]=int(self.lineEdit_hand_open.text())
                    self.submit_joint_values[7]=-int(self.lineEdit_hand_open.text())
                    self.textBrowser.setText('Submit Joint Value Changed ;\n Setting Submit Joint values to:\n'+str(self.submit_joint_values))
                    self.is_submit_value_correct[6]=True
                else:
                    self.textBrowser.setText('Joint Value Out Of Range')
                    self.is_submit_value_correct[6]=False
        except:
            self.textBrowser.setText('Joint Value Format Incorrect')
            self.is_submit_value_correct[6]=False
            pass
    def submit_angle(self):
        bool1=True
        for i in self.is_submit_value_correct:
            bool1=bool1 and i
        if bool1==True:
            for i in range(8):
                self.joint_values[i]=self.submit_joint_values[i]
            self.textBrowser.setText('Submit Joint Value Control ;\n Joint Values '+str(self.joint_values))
            self.slider_joint1.setValue(self.joint_values[0]*10)
            self.slider_joint2.setValue(self.joint_values[1]*10)
            self.slider_joint3.setValue(self.joint_values[2]*10)
            self.slider_joint4.setValue(self.joint_values[3]*10)
            self.slider_joint5.setValue(self.joint_values[4]*10)
            self.slider_joint6.setValue(self.joint_values[5]*10)
            self.slider_hand_open.setValue(self.joint_values[6]*10)
        else:
            self.textBrowser.setText('Joint Setting Incorrect, Please Check')
    def random_angle(self):
        for i in range(6):
            self.joint_values[i]=round(random.uniform(10,80),1)
            self.slider_joint1.setValue(self.joint_values[0] * 10)
            self.slider_joint2.setValue(self.joint_values[1] * 10)
            self.slider_joint3.setValue(self.joint_values[2] * 10)
            self.slider_joint4.setValue(self.joint_values[3] * 10)
            self.slider_joint5.setValue(self.joint_values[4] * 10)
            self.slider_joint6.setValue(self.joint_values[5] * 10)
            self.textlabel_joint1.setText(str(self.joint_values[0]))
            self.textlabel_joint2.setText(str(self.joint_values[1]))
            self.textlabel_joint3.setText(str(self.joint_values[2]))
            self.textlabel_joint4.setText(str(self.joint_values[3]))
            self.textlabel_joint5.setText(str(self.joint_values[4]))
            self.textlabel_joint6.setText(str(self.joint_values[5]))
            self.lineEdit_joint1.setText(str(self.joint_values[0]))
            self.lineEdit_joint2.setText(str(self.joint_values[1]))
            self.lineEdit_joint3.setText(str(self.joint_values[2]))
            self.lineEdit_joint4.setText(str(self.joint_values[3]))
            self.lineEdit_joint5.setText(str(self.joint_values[4]))
            self.lineEdit_joint6.setText(str(self.joint_values[5]))

    def simulation_state_changed(self):
        self.is_simulation_mode_on=not self.is_simulation_mode_on
        '''
        if self.is_simulation_mode_on and self.is_leapmotion_control_mode_on==True:
            self.checkBox_Leapmotion_mode.toggle()
        '''
        self.textBrowser.setText('Simulation Mode States\n'+str(self.is_simulation_mode_on))
    def joint_angle_control_state_changed(self):
        self.is_joint_angle_control_on=not self.is_joint_angle_control_on
        if self.is_joint_angle_control_on and self.is_leapmotion_control_mode_on:
            self.checkBox_Leapmotion_mode.toggle()
        if self.is_joint_angle_control_on and self.is_tip_inverse_control_on:
            self.checkBox_tip_inverse_control_mode.toggle()
        self.textBrowser.setText('Control Mode Setting:\nJoint Angle Control Mode State: '+str(self.is_joint_angle_control_on)+'\nTip Inveser Control Mode State: '+str(self.is_tip_inverse_control_on)+'\nLeapMotion Control Mode State: '+str(self.is_leapmotion_control_mode_on))
    def leapmotion_state_changed(self):
        self.is_leapmotion_control_mode_on=not self.is_leapmotion_control_mode_on
        if self.is_leapmotion_control_mode_on and self.is_joint_angle_control_on:
            self.checkBox_joint_angle_control_mode.toggle()
        if self.is_leapmotion_control_mode_on and self.is_tip_inverse_control_on:
            self.checkBox_tip_inverse_control_mode.toggle()
        self.textBrowser.setText('Control Mode Setting:\nJoint Angle Control Mode State: '+str(self.is_joint_angle_control_on)+'\nTip Inveser Control Mode State: '+str(self.is_tip_inverse_control_on)+'\nLeapMotion Control Mode State: '+str(self.is_leapmotion_control_mode_on))
    def tip_inverse_control_state_changed(self):
        self.is_tip_inverse_control_on=not self.is_tip_inverse_control_on
        if self.is_tip_inverse_control_on and self.is_joint_angle_control_on:
            self.checkBox_joint_angle_control_mode.toggle()
        if self.is_tip_inverse_control_on and self.is_leapmotion_control_mode_on:
            self.checkBox_Leapmotion_mode.toggle()
        self.textBrowser.setText('Control Mode Setting:\nJoint Angle Control Mode State: '+str(self.is_joint_angle_control_on)+'\nTip Inveser Control Mode State: '+str(self.is_tip_inverse_control_on)+'\nLeapMotion Control Mode State: '+str(self.is_leapmotion_control_mode_on))
    def servo_speed_fast_state_changed(self):
        self.is_servo_speed_fast=not self.is_servo_speed_fast
        if self.is_servo_speed_fast and self.is_servo_speed_medium:
            self.checkBox_servo_speed_Medium.toggle()
        if self.is_servo_speed_fast and self.is_servo_speed_slow:
            self.checkBox_servo_speed_Slow.toggle()
        self.textBrowser.setText('Servo Speed Setting:\nFast : '+str(self.is_servo_speed_fast)+'\nMedium :'+str(self.is_servo_speed_medium)+'\nSlow : '+str(self.is_servo_speed_slow))
    def servo_speed_medium_state_changed(self):
        self.is_servo_speed_medium=not self.is_servo_speed_medium
        if self.is_servo_speed_medium and self.is_servo_speed_fast:
            self.checkBox_servo_speed_fast.toggle()
        if self.is_servo_speed_medium and self.is_servo_speed_slow:
            self.checkBox_servo_speed_Slow.toggle()
        self.textBrowser.setText('Servo Speed Setting:\nFast : '+str(self.is_servo_speed_fast)+'\nMedium :'+str(self.is_servo_speed_medium)+'\nSlow : '+str(self.is_servo_speed_slow))
    def servo_speed_slow_state_changed(self):
        self.is_servo_speed_slow=not self.is_servo_speed_slow
        if self.is_servo_speed_slow and self.is_servo_speed_medium:
            self.checkBox_servo_speed_Medium.toggle()
        if self.is_servo_speed_slow and self.is_servo_speed_fast:
            self.checkBox_servo_speed_fast.toggle()
        self.textBrowser.setText('Servo Speed Setting:\nFast : '+str(self.is_servo_speed_fast)+'\nMedium :'+str(self.is_servo_speed_medium)+'\nSlow : '+str(self.is_servo_speed_slow))
    def tip_inversed_x_changed(self):
        if self.is_tip_inverse_control_on==True:
            self.tip_inverse_position[0]=self.verticalSlider_tip_inverse_x.value()/100.0
            self.textlabel_tip_inverse_x.setText(str(self.tip_inverse_position[0]))
            self.textBrowser.setText('Tip Inverse Control Position: '+str(self.tip_inverse_position))
    def tip_inversed_y_changed(self):
        if self.is_tip_inverse_control_on==True:
            self.tip_inverse_position[1]=self.verticalSlider_tip_inverse_y.value()/100.0
            self.textlabel_tip_inverse_y.setText(str(self.tip_inverse_position[1]))
            self.textBrowser.setText('Tip Inverse Control Position: '+str(self.tip_inverse_position))
    def tip_inversed_z_changed(self):
        if self.is_tip_inverse_control_on==True:
            self.tip_inverse_position[2]=self.verticalSlider_tip_inverse_z.value()/100.0
            self.textlabel_tip_inverse_z.setText(str(self.tip_inverse_position[2]))
            self.textBrowser.setText('Tip Inverse Control Position: '+str(self.tip_inverse_position))
    def tip_inversed_pitch_changed(self):
        if self.is_tip_inverse_control_on==True:
            self.tip_inverse_position[3]=self.verticalSlider_tip_inverse_pitch.value()
            self.textlabel_tip_inverse_pitch.setText(str(self.tip_inverse_position[3]))
            self.textBrowser.setText('Tip Inverse Control Position: '+str(self.tip_inverse_position))
    def tip_inversed_roll_changed(self):
        if self.is_tip_inverse_control_on==True:
            self.tip_inverse_position[4]=self.verticalSlider_tip_inverse_roll.value()
            self.textlabel_tip_inverse_roll.setText(str(self.tip_inverse_position[4]))
            self.textBrowser.setText('Tip Inverse Control Position: '+str(self.tip_inverse_position))
    ###################################################################