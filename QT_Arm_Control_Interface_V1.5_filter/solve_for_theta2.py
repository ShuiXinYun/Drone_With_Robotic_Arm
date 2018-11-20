# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:55:38 2016

@author: shuixin

solve q2 based on q1
"""
import parameters as para
from math import *
import dh
import numpy as np

def solve(q1,i,Pm):
    try:
        d=para.d
        a=para.a
        q=para.theta
        q[0]=q1
        L2=a[1];
        L3=np.sqrt(d[3]*d[3]+a[2]*a[2]);
        T01=dh.dh(q,i,0);
        Pm=np.matrix([Pm[0,0],Pm[0,1],Pm[0,2],1])
        Pm.resize((4,1))
        p1 = np.linalg.inv(T01)*Pm;
        r = np.sqrt(p1[0]*p1[0]+ p1[1]*p1[1]);
        beta = atan2(-p1[1], p1[0])
        gamma = acos((L2*L2+r*r-L3*L3)/(2*r*L2))
        q2_1 = pi/2 - beta - gamma #elbow up
        q2_2 = pi/2 - beta + gamma #elbow down
        q2=[q2_1,q2_2]
        return q2
        #print q2_1,q2_2
    except:
        print 'solve theta2 error,the point may not be reachable'
        pass
    