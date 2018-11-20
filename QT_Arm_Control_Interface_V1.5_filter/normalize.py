# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:08:27 2016

@author: shuixin

normalize q to [-pi, pi]
"""
import numpy as np
def normalize(q):
    try:
        return np.arctan2(np.sin(q),np.cos(q))
    except:
        print 'normalize error'
        pass