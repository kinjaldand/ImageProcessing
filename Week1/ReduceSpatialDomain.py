# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:29:21 2020

@author: Kinjal Dand

Description:

Spatial Domain : 
-   Size reduction in memory and image dimensions

"""

from PIL import Image
import numpy as np
import os
import ImageUtils as iu
import MyUtils as mu

#pix = np.array(Image.open('D:/MyGitHubWork/ImageProcessing/Data/color.png'))  
#neighbourhood =(3,3)  
def spatial_reduction(image_name,neighbourhood):
    pix = mu.get_image_as_cv2(image_name)
    pix = pix.astype(np.uint16)
    row,col = neighbourhood
    
    
    h,w,c = pix.shape
    print(pix.shape)
    
    
    h2 = int(np.floor(h/row))
    w2 = int(np.floor(w/col))
    
    new_img = np.zeros((h2,w2,3))
    print(new_img.shape)
    for i in range(0,w,col):
        for j in range(0,h,row):
            for k in range(0,c):
                c1 = j
                c2 = i
                c3= min(j+col+1,h)
                c4 = min(i+row+1,w)

                temp = pix[c1:c3,c2:c4,k]
                
                j2 = min(int(np.floor(j/row)),new_img.shape[0]-1)
                i2 = min(int(np.floor(i/col)),new_img.shape[1]-1)
                
                new_img[j2,i2,k]   = int(np.floor(np.mean(temp)))

    dest_name = mu.save_img(new_img,image_name,"_space"+str(neighbourhood).replace(',','-'))
    print(neighbourhood,pix.shape,new_img.shape,mu.get_file_size(dest_name),mu.get_file_size(image_name))
    
    
    
def CallMe():
    image_name = 'color.png'
    image_name = 'cat.jpg'
    neighs = [3,5,7]
    #neighs = [15,25,30,40,50]
    for n in neighs:
        neighbourhood = (n,n)
        spatial_reduction(image_name,neighbourhood)
    
    
        
if __name__ == "__main__":
    CallMe()
    
    
