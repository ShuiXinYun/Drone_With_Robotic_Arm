"""
This part receive data from leap Motion to move the model in rviz.
Two methods are used to recognize the movement of hand:
 1 Difference between current frame(Leap data) and previous frame are used to caculate the movement of the hand.
 2 The first position of hand are read and set as a standard to compare with, hand positions in later frames ared used
   to caculate the movement.
In order to decrese the collision of the data, gaussian filter is applied to get a filtered joint value.
@author: shuixin
"""

import rospy, math, datetime, time, serial ,sys
from PyQt4 import QtCore, QtGui
from termcolor import colored
from collections import deque
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from Arm_Soft_v1_5 import Ui_Mainwindow #this is the pyqt interface
import scipy.ndimage as fd # this method is used to smooth the movement of robotic arm
import Leap
import inverse_solve # kinematics inverse solution 
import parameters as para # parameters of the robotic arm


def talker():
    #####################################
    global orig_pos_x, orig_pos_y, orig_pos_z, maxangle, framenum, rad2deg, a, joint_info_pre
    bluetooth_count = 0
    bluetooth_count_leap = 0
    map_factor_x = 1.0 #map_factor change the direction of the movement of robotic arm 
    map_factor_y = -1.0
    map_factor_z = -1.0
    is_joint_results_smooth= True
    is_leap_data_smooth= True
    leap_data_filter_count= 0
    leap_data_filter_deque= range(7)
    is_leap_data_initial = False
    leap_x = 0.0; leap_y = 0.0; leap_z = 0.0
    leap_count = 0
    for i in xrange(7):
        leap_data_filter_deque[i]=deque(maxlen=leap_data_smooth_deque_num) #x, y, z, pitch, roll, yaw, grab strength
    maxangle = []
    bluetooth_count_max=6
    is_serial_trans_on = True # this parameter decides whether angle data is transmitted through bluetooth
    joint_deque_joint_control = []
    joint_deque_tip_control = []
    joint_deque_leap_control = []
    for i in range(10):
        joint_deque_joint_control.append(deque(maxlen=joint_deque_num))
        joint_deque_tip_control.append(deque(maxlen=joint_deque_num))
        joint_deque_leap_control.append(deque(maxlen=joint_deque_num))
    filter_work_trigger_joint_control=False
    filter_work_trigger_count_joint_control=0
    filter_work_trigger_tip_control = False
    filter_work_trigger_count_tip_control = 0
    filter_work_trigger_leap_control=False
    filter_work_trigger_count_leap_control = 0
    #####################################
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher',anonymous=False)
    rate = rospy.Rate(ros_rate) # 60hz
    
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    
    #sys.exit(app.exec_())
    
    def shutdown():
        print 'rospy shutted down'

    rospy.on_shutdown(shutdown)
    joint_info = JointState()
    joint_info.header = Header()
    joint_info.header.stamp = rospy.Time.now()
    joint_info.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6' ,'bar1_joint','bar2_joint','hand_left_tip_joint','hand_right_tip_joint']
    joint_info.velocity = []
    joint_info.effort = []
    
    while not rospy.is_shutdown():
        # different work mode
        is_simulation_mode_on=myapp.ui.is_simulation_mode_on
        is_joint_control_on=myapp.ui.is_joint_angle_control_on
        is_tip_inverse_control_on=myapp.ui.is_tip_inverse_control_on
        is_leapmotion_control_mode_on=myapp.ui.is_leapmotion_control_mode_on
        QtCore.QCoreApplication.processEvents()

        #if the simulation mode is on, serial data trans will be turned off
        if is_simulation_mode_on==True:
            is_serial_trans_on=False
            maxangle=para.maxangle_simulation
        else:
            is_serial_trans_on=True
            maxangle=para.maxangle
            
        if is_joint_control_on==True:
            leapdata_initial()
            joint_filtered = range(10)
            joint_values=myapp.ui.joint_values
            joint_info.position=q_handle(joint_values)
            if filter_work_trigger_joint_control==False and filter_work_trigger_count_joint_control< 30:
                filter_work_trigger_count_joint_control+=1
            else:
                filter_work_trigger_joint_control= True

            if is_joint_results_smooth:
                for i in range(10):
                    joint_deque_joint_control[i].append(joint_info.position[i])
                    joint_filtered[i]=list(fd.filters.gaussian_filter(list(joint_deque_joint_control[i]), joint_gaussian_filter_level_4_joint_control))[-1]
                    if filter_work_trigger_joint_control== True:
                        joint_info.position[i]=joint_filtered[i]

            joint_info.header.stamp = rospy.Time.now()
            for i in range(6):
                joint_info_bluetooth[i]=round(joint_info.position[i]*rad2deg+45.0,1)
            joint_info_bluetooth[2]+=(joint_info_bluetooth[1]-45.0)
            joint_info_bluetooth[2]=round(joint_info_bluetooth[2],1)
            joint_info_bluetooth[6]=round(joint_info.position[8]*rad2deg,1)
            
            send_info=[204]
            for i in range(6):
                send_temp=[i,int(joint_info_bluetooth[i]),int(10*(joint_info_bluetooth[i]-int(joint_info_bluetooth[i]))),i+int(joint_info_bluetooth[i])+int(10*(joint_info_bluetooth[i]-int(joint_info_bluetooth[i])))]
                send_info+=send_temp
            send_info+=[8,int(90.0-joint_info_bluetooth[6]/2.0),int(10*(90.0-joint_info_bluetooth[6]/2.0-int(90.0-joint_info_bluetooth[6]/2.0))),8+int(90.0-joint_info_bluetooth[6]/2.0)+int(10*(90.0-joint_info_bluetooth[6]/2.0-int(90.0-joint_info_bluetooth[6]/2.0)))]
            send_info.append(255)

            if is_serial_trans_on:
                if bluetooth_count==bluetooth_count_max:
                    #a=[204,7,int(joint_info_bluetooth[0]),int(joint_info_bluetooth[0])+7,255]
                    a=str(bytearray(send_info))
                    t.write(a)
                    bluetooth_count=0
                bluetooth_count+=1

            print 'joint info:',joint_info_bluetooth,bluetooth_count#'mode:simu,joint_control,tip_inverse_control,leap_control: ',is_simulation_mode_on,is_joint_control_on,is_tip_inverse_control_on,is_leapmotion_control_mode_on
            print 'send_info:',send_info
            pub.publish(joint_info)
            rate.sleep()
            
        elif is_tip_inverse_control_on==True:
            joint_filtered = range(10)
            leapdata_initial()
            delta_x=myapp.ui.tip_inverse_position[0]
            delta_y=myapp.ui.tip_inverse_position[1]
            delta_z=myapp.ui.tip_inverse_position[2]
            delta_pitch=myapp.ui.tip_inverse_position[3]
            delta_roll=myapp.ui.tip_inverse_position[4]
            orig_pos_x+=delta_x
            orig_pos_y+=delta_y
            orig_pos_z+=delta_z
            q=inverse_solve.inverse_solve(orig_pos_x,orig_pos_y,orig_pos_z,0.0,0.0,0.0)
            if q==None:
                print colored('Position Out of Range','green')
                joint_info.position=joint_info_pre
            else:
                joint_info.position = q_handle_tip(q,0)
                for i in range(6):
                    joint_info_bluetooth[i]=round(joint_info.position[i]*rad2deg)+45
                joint_info_bluetooth[6]=round(joint_info.position[8]*rad2deg)

            if filter_work_trigger_tip_control == False and filter_work_trigger_count_tip_control < 30:
                filter_work_trigger_count_tip_control += 1
            else:
                filter_work_trigger_tip_control = True

            for i in range(10):
                joint_deque_tip_control[i].append(joint_info.position[i])
                joint_filtered[i] = list(fd.filters.gaussian_filter(list(joint_deque_tip_control[i]), joint_gaussian_filter_level_4_joint_control))[-1]
                if filter_work_trigger_tip_control == True:
                    joint_info.position[i] = joint_filtered[i]
            joint_info_pre=joint_info.position

            for i in range(6):
                q_pre_solution[i]=joint_info.position[i]

            joint_info.header.stamp = rospy.Time.now()
            pub.publish(joint_info)
            rate.sleep()
            
        elif is_leapmotion_control_mode_on==True:
            starttime = datetime.datetime.now()
            roll=0.0;pitch=0.0;yaw=0.0;grab_strength=0.0
            pre_pos_x=0.0;pre_pos_y=0.0;pre_pos_z=0.0;curr_pos_x=0.0;curr_pos_y=0.0;curr_pos_z=0.0
            joint_filtered = range(10)


            if is_leap_data_smooth:
                if len(controller.frame().hands)> 0 :
                    if leap_count< 5:
                        leap_current_frame= controller.frame()
                        leap_x += controller.frame().hands[0].palm_position[2]
                        leap_y += controller.frame().hands[0].palm_position[0]
                        leap_z += controller.frame().hands[0].palm_position[1]
                        leap_count += 1
                    else:
                        is_leap_data_initial= True
                if is_leap_data_initial== True:
                    leap_current_frame= controller.frame()
                    leap_data_filter_deque[0].append(leap_current_frame.hands[0].palm_position[2])
                    leap_data_filter_deque[1].append(leap_current_frame.hands[0].palm_position[0])
                    leap_data_filter_deque[2].append(leap_current_frame.hands[0].palm_position[1])
                    normal= leap_current_frame.hands[0].palm_normal
                    direction= leap_current_frame.hands[0].direction
                    arm= controller.frame().hands[0].arm
                    arm_pitch = arm.direction.pitch
                    arm_yaw= arm.direction.yaw
                    hand_pitch= direction.pitch
                    hand_yaw= direction.yaw
                    roll += normal.roll
                    pitch += hand_pitch - arm_pitch
                    yaw += hand_yaw- arm_yaw
                    grab_strength += leap_current_frame.hands[0].grab_strength
                    leap_data_filter_deque[3].append(pitch)
                    leap_data_filter_deque[4].append(roll)
                    leap_data_filter_deque[5].append(yaw)
                    leap_data_filter_deque[6].append(grab_strength)

                    if leap_data_filter_count <= leap_data_smooth_deque_num:
                        leap_data_filter_count +=1
                    else:
                        leap_x_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[0]), leap_gaussian_filter_level))[-2]
                        leap_y_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[1]), leap_gaussian_filter_level))[-2]
                        leap_z_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[2]), leap_gaussian_filter_level))[-2]
                        leap_pitch_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[3]), leap_gaussian_filter_level))[-2]
                        leap_roll_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[4]), leap_gaussian_filter_level))[-2]
                        leap_yaw_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[5]), leap_gaussian_filter_level))[-2]
                        leap_grab_stength_curr = list(fd.filters.gaussian_filter(list(leap_data_filter_deque[6]), 1))[-2]
                        orig_pos_x = 0.2242957
                        orig_pos_y = 0.0
                        orig_pos_z = 0.335396
                        print "leap ",leap_x/5.0,leap_y/5.0,leap_z/5.0
                        print "leap_curr", leap_x_curr,leap_y_curr,leap_z_curr
                        orig_pos_x = orig_pos_x + (leap_x_curr - leap_x/5.0) * 0.0005 * map_factor_x
                        orig_pos_y = orig_pos_y + (leap_y_curr - leap_y/5.0) * 0.0005 * map_factor_y
                        orig_pos_z = orig_pos_z + (leap_z_curr - leap_z/5.0) * 0.0005 * map_factor_z
                        pitch = leap_pitch_curr
                        roll = leap_roll_curr
                        yaw = leap_yaw_curr
                        grab_strength = leap_grab_stength_curr
                        print 'Leap Data Smoothing'


            else:
                previous_frame = []
                for i in range(framenum):
                    previous_frame.append(controller.frame(i + framenum))
                current_frame = []
                for i in range(framenum):
                    current_frame.append(controller.frame(i))
                framerate = current_frame[0].current_frames_per_second
                print 'frame_rate', framerate
                for i in range(framenum):
                    hand_curr= current_frame[i].hands[0]
                    curr_pos_x+=hand_curr.palm_position[2]
                    curr_pos_y+=hand_curr.palm_position[0]
                    curr_pos_z+=hand_curr.palm_position[1]
                    normal_curr = hand_curr.palm_normal
                    direction_curr = hand_curr.direction
                    arm_curr=hand_curr.arm
                    arm_pitch_curr=arm_curr.direction.pitch
                    arm_yaw_curr=arm_curr.direction.yaw
                    hand_pitch_curr=direction_curr.pitch
                    hand_yaw_curr=direction_curr.yaw
                    roll+=normal_curr.roll
                    pitch+=hand_pitch_curr-arm_pitch_curr
                    yaw+=hand_yaw_curr-arm_yaw_curr
                    grab_strength += hand_curr.grab_strength #An open hand has a grab strength of zero. As a hand closes into a fist, its grab strength increases to one

                    hand_pre=previous_frame[i].hands[0]
                    pre_pos_x+=hand_pre.palm_position[2]
                    pre_pos_y+=hand_pre.palm_position[0]
                    pre_pos_z+=hand_pre.palm_position[1]
                    normal_pre = hand_pre.palm_normal
                    direction_pre = hand_pre.direction
                    arm_pre= hand_pre.arm
                    arm_pitch_pre= arm_pre.direction.pitch
                    arm_yaw_pre= arm_pre.direction.yaw
                    hand_pitch_pre= direction_pre.pitch
                    hand_yaw_pre= direction_pre.yaw
                    roll+= normal_pre.roll
                    pitch+= hand_pitch_pre-arm_pitch_pre
                    yaw+= hand_yaw_pre-arm_yaw_pre
                    grab_strength += hand_pre.grab_strength
                roll=roll/(2*framenum);pitch=pitch/(2*framenum);yaw=yaw/(2*framenum);grab_strength=grab_strength/(2*framenum)
                orig_pos_x=orig_pos_x+(curr_pos_x/framenum-pre_pos_x/framenum)*map_factor*map_factor_x
                orig_pos_y=orig_pos_y+(curr_pos_y/framenum-pre_pos_y/framenum)*map_factor*map_factor_y
                orig_pos_z=orig_pos_z+(curr_pos_z/framenum-pre_pos_z/framenum)*map_factor*map_factor_z


            data=data_round(orig_pos_x,orig_pos_y,orig_pos_z,roll*rad2deg,pitch*rad2deg,yaw*rad2deg)
            print 'Leap_Data:x,y,z,roll,pitch,yaw',data
            q=inverse_solve.inverse_solve(data[0],data[1],data[2],data[3]/rad2deg,data[4]/rad2deg,data[5]/rad2deg)
            if q==None:
                print colored('Position Out of Range','green')
                joint_info.position=joint_info_pre
            else:
                joint_info.position = q_handle_leap(q,0)
                joint_info.position[3]=0.3*data[3]/rad2deg#0.5roll
                joint_info.position[5]=0.3*data[3]/rad2deg#0.5roll
                joint_info.position[4]=(data[4]/rad2deg-joint_info.position[2])*0.6 #wrist pitch
                joint_info.position[8]=(30.0-30.0*grab_strength)/rad2deg
                joint_info.position[9]=-joint_info.position[8]

                if is_joint_results_smooth:
                    if filter_work_trigger_leap_control == False and filter_work_trigger_count_leap_control < 30:
                        filter_work_trigger_count_leap_control += 1
                    else:
                        filter_work_trigger_leap_control = True

                    for i in range(6):
                        joint_deque_leap_control[i].append(joint_info.position[i])
                        if filter_work_trigger_leap_control == True:
                            joint_filtered[i] = \
                            list(fd.filters.gaussian_filter(list(joint_deque_leap_control[i]), joint_gaussian_filter_level_4_leap))[-2]
                            joint_info.position[i] = joint_filtered[i]

                #joint_info.position=map(lambda x:round(x*rad2deg,1)/rad2deg,joint_info.position)

                is_in_range=joint_value_check_leap(joint_info.position, maxangle)


                if is_in_range[0]==False:
                    print colored('Joint '+str(is_in_range[1])+'  Out Of Range','green')
                    joint_info.position=joint_info_pre
                joint_info_pre=joint_info.position
                
                for i in range(6):
                    joint_info_bluetooth[i]=round(joint_info.position[i]*rad2deg+45.0,1)
                joint_info_bluetooth[3]=round(90.0-joint_info_bluetooth[3],1) #set the arm move direction same with human arm
                joint_info_bluetooth[5]=round(90.0-joint_info_bluetooth[5],1) #set the arm move direction same with human arm
                joint_info_bluetooth[6]=round(90.0-joint_info.position[8]*rad2deg,1)           
                joint_info_bluetooth[0]=round(90.0-joint_info_bluetooth[0],1)
                send_info=[204]
                for i in range(6):
                    send_temp=[i,int(joint_info_bluetooth[i]),int(10*(joint_info_bluetooth[i]-int(joint_info_bluetooth[i]))),i+int(joint_info_bluetooth[i])+int(10*(joint_info_bluetooth[i]-int(joint_info_bluetooth[i])))]
                    send_info+=send_temp
                send_info+=[8,int(joint_info_bluetooth[6]),int(10*(joint_info_bluetooth[6]-int(joint_info_bluetooth[6]))),8+int(joint_info_bluetooth[6])+int(10*(joint_info_bluetooth[6]-int(joint_info_bluetooth[6])))]
                send_info.append(255)

                if is_serial_trans_on:
                    if bluetooth_count_leap==bluetooth_count_max:
                        a=str(bytearray(send_info))
                        t.write(a)
                        bluetooth_count_leap=0
                    bluetooth_count_leap+=1

                myapp.ui.slider_joint1.setValue(joint_info_bluetooth[0]*10)
                myapp.ui.textlabel_joint1.setText(str(joint_info_bluetooth[0]))
                myapp.ui.slider_joint2.setValue(joint_info_bluetooth[1]*10)
                myapp.ui.textlabel_joint2.setText(str(joint_info_bluetooth[1]))
                myapp.ui.slider_joint3.setValue(joint_info_bluetooth[2]*10)
                myapp.ui.textlabel_joint3.setText(str(joint_info_bluetooth[2]))
                myapp.ui.slider_joint4.setValue(joint_info_bluetooth[3]*10)
                myapp.ui.textlabel_joint4.setText(str(joint_info_bluetooth[3]))
                myapp.ui.slider_joint5.setValue(joint_info_bluetooth[4]*10)
                myapp.ui.textlabel_joint5.setText(str(joint_info_bluetooth[4]))
                myapp.ui.slider_joint6.setValue(joint_info_bluetooth[5]*10)
                myapp.ui.textlabel_joint6.setText(str(joint_info_bluetooth[5]))
                myapp.ui.slider_hand_open.setValue(joint_info.position[8]*rad2deg*2*10)
                myapp.ui.textlabel_hand_open.setText(str(joint_info.position[8]*rad2deg))
                for i in range(6):
                    q_pre_solution[i]=joint_info.position[i]
                #print 'Ros Data:',joint_info.position
                print 'joint values:',joint_info_bluetooth
                print 'send_info::',send_info
                endtime = datetime.datetime.now()
                print 'solve_time:',(endtime-starttime).microseconds*1e-6
                #joint_csv_writer.writerow([(endtime-starttime).microseconds*1e-6,joint_info.position[0],joint_info.position[1],joint_info.position[2],joint_info.position[3],joint_info.position[4],joint_info.position[5]])
            joint_info.header.stamp = rospy.Time.now()
            pub.publish(joint_info)
            rate.sleep()
        else:
            leap_data_filter_count = 0
            is_leap_data_initial = False
            leap_x = 0.0; leap_y = 0.0; leap_z = 0.0
            leap_count = 0


def q_handle(joint_values):
    try:
        joint_info=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]#['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6' ,'bar1_joint','bar2_joint']
        joint_values=map(lambda x:x/rad2deg,joint_values)        
        joint_info[0:6]=joint_values[0:6]
        for i in range(6):
            joint_info[i]=joint_info[i]-45.0/rad2deg
        joint_info[2]=joint_info[2]-joint_info[1]
        joint_info[6]=joint_values[1]+joint_values[2]
        joint_info[7]=-joint_values[2]
        joint_info[6]=joint_info[2]+joint_info[1]
        joint_info[7]=joint_info[1]-joint_info[6]#-20.0/rad2deg
        joint_info[8]=joint_values[6]
        joint_info[9]=joint_values[7]
        return joint_info
    except:
        print 'q_handle error'
        pass

def q_handle_tip(q,col_num):
    try:
        joint_info=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        for i in range(6):
            joint_info[i]=q[i,col_num]     
        joint_info[6]=joint_info[2]
        joint_info[7]=-joint_info[2]+joint_info[1]
        if joint_info[3]+joint_info[5]>math.pi:
            joint_info[3]=(joint_info[3]+joint_info[5])%math.pi
            joint_info[5]=joint_info[3]
        elif joint_info[3]+joint_info[5]<-math.pi:
            joint_info[3]=(joint_info[3]+joint_info[5])%-math.pi
            joint_info[5]=joint_info[3]
        else:
            joint_info[3]=0.5*(joint_info[3]+joint_info[5])
            joint_info[5]=joint_info[3]
        return joint_info
    except:
        pass

def q_handle_leap(q,col_num):
    try:
        joint_info=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]#['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6' ,'bar1_joint','bar2_joint']
        for i in range(6):
            joint_info[i]=q[i,col_num]
        joint_info[6]=joint_info[2]
        joint_info[7]=-joint_info[2]+joint_info[1]
        if joint_info[3]+joint_info[5]>math.pi:
            joint_info[3]=(joint_info[3]+joint_info[5])%math.pi
            joint_info[5]=joint_info[3]
        elif joint_info[3]+joint_info[5]<-math.pi:
            joint_info[3]=(joint_info[3]+joint_info[5])%-math.pi
            joint_info[5]=joint_info[3]
        else:
            joint_info[3]=0.5*(joint_info[3]+joint_info[5])
            joint_info[5]=joint_info[3]
        return joint_info
        '''
        joint_info[3]=joint_info[3]+joint_info[5]
        if joint_info[3]>=math.pi:
            joint_info[3]=joint_info[3]%math.pi
            #joint_info[3]=math.pi
        elif joint_info[3]<=-math.pi:
            joint_info[3]=joint_info[3]%(-math.pi)
            #joint_info[3]=-math.pi/2
        joint_info[3]=0.5*joint_info[3]
        joint_info[5]=joint_info[3]
        '''
        return joint_info
    except:
        print 'q_handle error'
        pass

#Round the origin data received by leapmotion
def data_round(orig_pos_x,orig_pos_y,orig_pos_z,roll,pitch,yaw):
    global xyzaccuracy,rpyaccuracy
    '''
    if abs(roll)<5.0:
        roll=0.0
    if abs(pitch)<5.0:
        pitch=0.0
    if abs(yaw)<5.0:
        yaw=0.0
    '''
    #data=[round(xyzaccuracy*round(orig_pos_x/xyzaccuracy,4),4),round(xyzaccuracy*round(orig_pos_y/xyzaccuracy,4),4),round(xyzaccuracy*round(orig_pos_z/xyzaccuracy,4),4),
          #rpyaccuracy*round(roll/rpyaccuracy,2),rpyaccuracy*round(pitch/rpyaccuracy,2),-rpyaccuracy*round(yaw/rpyaccuracy,2)]
    data=[round(orig_pos_x,6),round(orig_pos_y,6),round(orig_pos_z,6),round(roll,3),round(pitch,3),-round(yaw,3)]
    return data

#Check if the joint values are in the limitation
def joint_value_check_leap(joint_info_position, maxangle):
    is_in_range=[True,0]
    for i in range(5):
        if joint_info_position[i]+45.0/rad2deg<maxangle[i][0]/rad2deg or joint_info_position[i]+45.0/rad2deg>maxangle[i][1]/rad2deg:
            is_in_range=[False,i]
    return is_in_range

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)
        
def leapdata_initial():
    global orig_pos_x,orig_pos_y,orig_pos_z
    orig_pos_x=0.2242957;orig_pos_y=0.0;orig_pos_z=0.335396

if __name__ == '__main__':
    #######################
    rad2deg=180.0/math.pi
    q_pre_solution=[0.0,0.0,0.0,0.0,0.0,0.0]
    joint_info_pre=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    joint_info_bluetooth=[45.0,65.0,45.0,45.0,45.0,45.0,0.0]
    #a=[204,7,45,52,255]

    #xyzaccuracy=1.0 #2mm
    #rpyaccuracy=1.0 #2 degree
    is_run=True
    #t=serial.Serial('/dev/ttyUSB0',57600)
    orig_pos_x= 0.2242957; orig_pos_y= 0.0; orig_pos_z= 0.335396
    framenum = 10
    joint_deque_num = 20
    leap_data_smooth_deque_num = 100
    ros_rate= 60
    map_factor= 5e-3/ros_rate
    joint_gaussian_filter_level_4_joint_control = 50
    joint_gaussian_filter_level_4_leap = 5
    leap_gaussian_filter_level = 5
    #########################
    controller = Leap.Controller()
    time.sleep(1)
    talker()


#rostopic pub -1 /joint_states sensor_msgs/JointState '{header: auto, name: ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6'], position: [0.23436, -0.000298, 0.0, 0.0, 0.0, 0.0], velocity: [], effort: []}'


