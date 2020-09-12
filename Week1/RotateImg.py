# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:29:21 2020

@author: Kinjal Dand

Description:

Image Rotate : 

"""

from PIL import Image
import numpy as np
import os
import ImageUtils as iu
import MyUtils as mu

#pix = np.array(Image.open('D:/MyGitHubWork/ImageProcessing/Data/color.png'))  
#neighbourhood =(3,3)  
def image_rotate(image_name,angle):
    img = mu.get_image_as_cv2(image_name)
    new_img = iu.rotate_img(img,angle)
    dest_name = mu.save_img(new_img,image_name,str(angle))

    
    
    
def CallMe():
    image_name = 'color.png'
    image_name = 'cat.jpg'
    angles = [45,90,180]
    #neighs = [15,25,30,40,50]
    for angle in angles:
        image_rotate(image_name,angle)
    
    
        
if __name__ == "__main__":
    CallMe()
    
    
