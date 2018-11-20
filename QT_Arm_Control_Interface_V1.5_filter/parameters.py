# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:24:32 2016

@author: shuixin

parameters for robotic arm like irb2400
"""
from math import *

deg2rad=pi/180
theta=[0.0,-pi/2,0.0,0.0,0.0,pi]
#d=[0.615,0,0,0.755,0,0.085]#standard
#d=[0.1313231,0,0,0.244,0,0.036]#old_model
d=[0.079396,0,0,0.1775,0,0.024]
#a=[0.1,0.705,0.135,0,0,0]#standard
#a=[0.0012832,0.28,0.031,0,0,0]#old_model
a=[0.0227957,0.22,0.036,0,0,0]
alpha=[-pi/2,0,-pi/2,pi/2,-pi/2,0]
maxangle=[[2,88],
          [5,85],
          [5,85],
          [5,85],
          [10,80],
          [5,85]]

maxangle_simulation=[[-180,180],
                     [-180,180],
                     [-180,180],
                     [-180,180],
                     [-180,180],
                     [-180,180]]