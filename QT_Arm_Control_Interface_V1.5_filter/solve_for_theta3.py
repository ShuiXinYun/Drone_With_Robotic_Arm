# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:54:26 2016

@author: shuixin

solve q3 based on q1
"""
import parameters as para
from math import *
import dh
import numpy as np

def solve(q1,i,Pm):
    try:
        d=para.d
        a=para.a
        L2=a[1];
        L3=sqrt(d[3]*d[3]+a[2]*a[2]);
        q=para.theta
        q[0]=q1
        T01=dh.dh(q,i,0);
        Pm=np.matrix([Pm[0,0],Pm[0,1],Pm[0,2],1])
        Pm.resize((4,1))
        p1 = np.linalg.inv(T01)*Pm;
        r = sqrt(p1[0]*p1[0]+ p1[1]*p1[1]);
        eta=acos((L2*L2 + L3*L3 - r*r)/(2*L2*L3))
        q3_1 = -(atan(d[3]/a[2])+eta - pi) #elbow up
        q3_2 = -(pi+atan(d[3]/a[2])-eta) #elbow down
        q3=[q3_1,q3_2]
        return q3
        #print q2_1,q2_2
    except:
        print 'solve theta3 error,the point may not be reachable'
        pass