# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:33:14 2016

@author: shuixin
"""
import datetime
import parameters as para
import pyr2noa
import numpy as np
from math import *
import solve_for_theta2
import solve_for_theta3
import normalize
import solve_spherical_wrist
def inverse_solve(px,py,pz,pitch,yaw,roll):
    try:
        starttime = datetime.datetime.now()   
        #px=1.008172;py=0.11710;pz=0.99375#special test for robot rotate [0.1,0.2,0.3,0.4,0.5,0.6]
        d=para.d;a=para.a
        L1=d[0]
        L2=a[1]
        L3=d[3]
        L6=d[5]
        A1=a[0]
        #Compute the position of the wrist, being W the Z component of the end effector's system
        noa=pyr2noa.pyr2noa(pitch,yaw,roll)
        T=np.zeros((4,4))
        T=np.asmatrix(T)
        T[0:3,0:3]=noa
        T[0,3]=px;T[1,3]=py;T[2,3]=pz;T[3,3]=1.0;
        W=np.matrix([noa[0,2],noa[1,2],noa[2,2]])
        #W=np.matrix([0.53701,0.241515,-0.8082]) #special test for robot rotate [0.1,0.2,0.3,0.4,0.5,0.6]
        Pm=np.matrix([px,py,pz])-L6*W
        #print 'Pm  ',Pm
        #q1&q1+pi both are solution
        q1=atan2(Pm[0,1],Pm[0,0])
        #print 'q1 ',q1
        #for one q1,q2 have 2 solution,namely elbow up & elboow down
        #so that for q3,and q2 q3 elbow up & elbow down should coordinate
        #thus [q1,q2,q3] have 4 solutions:q1:ebbow up &down,q1+pi:elbow up&down
        q2_q10=solve_for_theta2.solve(q1,1,Pm)
        q3_q10=solve_for_theta3.solve(q1,1,Pm)
        q2_q1_pi=solve_for_theta2.solve(q1+pi,1,Pm)
        q3_q1_pi=solve_for_theta3.solve(q1+pi,1,Pm)
        q2_eblowup_q1=q2_q10[0];q2_eblowdown_q1=q2_q10[1]
        q2_eblowup_q1_pi=q2_q1_pi[0];q2_eblowdown_q1_pi=q2_q1_pi[1]
        q3_eblowup_q1=q3_q10[0];q3_eblowdown_q1=q3_q10[1]
        q3_eblowup_q1_pi=q3_q1_pi[0];q3_eblowdown_q1_pi=q3_q1_pi[1]
        q=np.matrix([[           q1,           q1,             q1,             q1,           q1+pi,           q1+pi,             q1+pi,             q1+pi],
                     [q2_eblowup_q1,q2_eblowup_q1,q2_eblowdown_q1,q2_eblowdown_q1,q2_eblowup_q1_pi,q2_eblowup_q1_pi,q2_eblowdown_q1_pi,q2_eblowdown_q1_pi],
                     [q3_eblowup_q1,q3_eblowup_q1,q3_eblowdown_q1,q3_eblowdown_q1,q3_eblowup_q1_pi,q3_eblowup_q1_pi,q3_eblowdown_q1_pi,q3_eblowdown_q1_pi],
                     [          0.0,          0.0,            0.0,            0.0,             0.0,             0.0,               0.0,               0.0],
                     [          0.0,          0.0,            0.0,            0.0,             0.0,             0.0,               0.0,               0.0],
                     [          0.0,          0.0,            0.0,            0.0,             0.0,             0.0,               0.0,               0.0]])
        q=normalize.normalize(q)
        q=solve_spherical_wrist.solve_spherical_wrist(q,T)
        q=normalize.normalize(q)
        #print q
        endtime = datetime.datetime.now()
        #print 'inverse_solve time(seconds): ',(endtime - starttime).microseconds/1000000.0
        return q
    except:
        #print 'inverse_solve error'
        pass


'''
T=np.matrix([[-0.638940 ,0.550787   ,0.53701   ,1.008172],
             [0.7420454  ,0.62533   ,0.24151   ,0.117103],
             [-0.202789 , 0.55280  ,-0.80825  ,0.99375],
             [     0      ,     0  ,      0 ,  1.0]])#special test for robot rotate [0.1,0.2,0.3,0.4,0.5,0.6]

t=0.0;
n=5000
for i in range(n):
    t+=inverse_solve()
print t/(n*1000000)
'''
#print inverse_solve(1.008172,0.117103,0.99375,0,1.57,0)
#print inverse_solve(0.94,0,1.455,0,0,0)
