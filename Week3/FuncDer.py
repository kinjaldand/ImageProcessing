# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:29:21 2020

@author: Kinjal Dand

Description:

Minimum of function - Derivative of that function is Zero: 


"""

from PIL import Image
import numpy as np
import os
import ImageUtils as iu
import MyUtils as mu



    
    
def CallMe():
    numlist = [1,2,3]
    func1 = []
    func2 = []
    alist = range(-10,10)
    for a in alist:
        num =0
        for n in numlist:
            num = num + ((a-n)**2)
        func1.append(num)
        func2.append((6*a)-12)
    
    for f,d in zip(func1,func2):
        print(f,d)
    
    
    
        
if __name__ == "__main__":
    CallMe()
    
    
