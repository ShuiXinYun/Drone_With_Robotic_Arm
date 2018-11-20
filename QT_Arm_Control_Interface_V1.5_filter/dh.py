# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:01:23 2016

@author: shuixin

return a 4 x 4 homogeneous transformation matrix
"""
import parameters as para
from math import *
import numpy as np

def dh(q,i,flag):
    try:
        i=i-1
        theta=q
        alpha=para.alpha
        d=para.d
        a=para.a
        d=d[i]
        a=a[i]
        alpha = alpha[i]
        if flag==0:
            theta = theta[i]
        else:
            theta = theta[i]+para.theta[i]
        A=np.matrix([[cos(theta),-cos(alpha)*sin(theta),sin(alpha)*sin(theta),a*cos(theta)],
                      [sin(theta),cos(alpha)*cos(theta),-sin(alpha)*cos(theta),a*sin(theta)],
                       [0,sin(alpha),cos(alpha),d],
                        [0,0,0,1]])
        return A
    except:
        print 'dh error'