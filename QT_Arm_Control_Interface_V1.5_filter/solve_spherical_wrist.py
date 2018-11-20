# -*- coding: utf-8 -*-
"""
Created on Tue May 24 23:37:55 2016

@author: shuixin

based on [q1 q2 q3],solve q4 q5 q6
"""
import dh
from math import *
import numpy as np
thresh=1e-12
def solve_spherical_wrist(q,T):
    try:
        q_return=q
        for i in [0,2,4,6]:
            q_temp=[]
            for j in range(6):
                q_temp.append(q[j,i])
            #print q_temp
            A01=dh.dh(q_temp,1,0)
            #print A01
            A12=dh.dh(q_temp,2,1)
            #print A12
            A23=dh.dh(q_temp,3,0)
            #print A23
            Q=np.linalg.inv(A23)*np.linalg.inv(A12)*np.linalg.inv(A01)*T
            #print Q
            if abs(Q[2,2]-1.0)>thresh:
                q4_wrist_up=atan2(Q[1,2],Q[0,2])
                q6_wrist_up=atan2(-Q[2,1],Q[2,0])
                q4_wrist_down=atan2(Q[1,2],Q[0,2])+pi
                q6_wrist_down=atan2(-Q[2,1],Q[2,0])+pi
                q5_wrist_up=solve_q5(q4_wrist_up,q6_wrist_up,Q)
                q5_wrist_down=solve_q5(q4_wrist_down,q6_wrist_down,Q)
            else:
                q4_wrist_up=0.0;q5_wrist_up=0.0;q6_wrist_up=atan2(Q[0,1]-Q[1,0],-Q[0,0]-Q[1,1]);
                q4_wrist_down=-pi;q5_wrist_down=0.0;q6_wrist_down=atan2(Q[0,1]-Q[1,0],-Q[0,0]-Q[1,1])+pi;
            q_return[3,i]=q4_wrist_up;q_return[3,i+1]=q4_wrist_down
            q_return[4,i]=q5_wrist_up;q_return[4,i+1]=q5_wrist_down
            q_return[5,i]=q6_wrist_up;q_return[5,i+1]=q6_wrist_down
        return q_return
    except:
        print 'solve spherical wrist error'
        pass
        
def solve_q5(q4,q6,Q):
    try:
        if abs(cos(q6+q4))>thresh:
            cq5=(-Q[0,0]-Q[1,1])/cos(q4+q6)-1
        if abs(sin(q6+q4))>thresh:
            cq5=(Q[0,1]-Q[1,0])/sin(q4+q6)-1
        if abs(sin(q6))>thresh:
            sq5=Q[2,1]/sin(q6)
        if abs(cos(q6))>thresh:
            sq5=-Q[2,0]/cos(q6)
        q5=atan2(sq5,cq5)
        return q5
    except:
        print "q5 solve error"
