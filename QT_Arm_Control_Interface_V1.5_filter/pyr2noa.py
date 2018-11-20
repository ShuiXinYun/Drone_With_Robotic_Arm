# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:43:19 2016

@author: shuixin

transfrom pitch\yaw\roll to dh parameters,
According to Leapmotion cooridinate system,Rotate along X,Y,Z are Pitch,Yaw,Roll
"""
import numpy as np
from math import *
def pyr2noa(pitch,yaw,roll):
    try:
        rotx=np.matrix([[1,0,0],[0,cos(pitch),-sin(pitch)],[0,sin(pitch),cos(pitch)]])
        roty=np.matrix([[cos(yaw),0,sin(yaw)],[0,1,0],[-sin(yaw),0,cos(yaw)]])
        rotz=np.matrix([[cos(roll),-sin(roll),0],[sin(roll),cos(roll),0],[0,0,1]])
        trans=np.matrix([[0,0,1],[0,1,0],[-1,0,0]])
        return rotx*roty*rotz*trans
    except:
        print 'pyr2noa error'
        pass

