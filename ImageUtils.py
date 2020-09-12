# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:19:33 2020

@author: Kinjal Dand

Commonly used image functions
Observations: cv2 saves file as numpy array

"""

import cv2
from PIL import Image
import numpy as np
import MyUtils as mu


def convert_image_to_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(type(img)) #<class 'numpy.ndarray'>
    return img
    
def conv_save_to_gray(image_name,img=None):
    if img is None:
        img = mu.get_image_as_cv2(image_name)
    img = convert_image_to_gray(img)
    dest_name = mu.save_img(img,image_name,append_text="_gray")
    return dest_name