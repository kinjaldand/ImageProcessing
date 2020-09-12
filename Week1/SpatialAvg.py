# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:29:21 2020

@author: Kinjal Dand

Description:

Spatial Avg : 
-   To sum image values where value>255, do 
    pix = pix.astype(np.uint16)   
    By default cv2 images are np.uint8 which introduces errors
-   Image blurs as we replace pixels by avg of their neighbourhood
-   We can observe sections emerge/outline highlighted at 20*20

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
    row_half = int(np.floor(row/2))
    col_half = int(np.floor(col/2))
    
    h,w,c = pix.shape
    print(pix.shape)

    new_img = pix.copy()
    max0 = lambda t: max(t,0)
    max0func = np.vectorize(max0)

    minw = lambda t: min(t,w)
    minwfunc = np.vectorize(minw)
    
    minh = lambda t: min(t,h)
    minhfunc = np.vectorize(minh)

    c1 = np.array(list(range(0,w))) - row_half
    c1 = max0func(c1)
    c2 = np.array(list(range(0,w))) + row_half
    c2 = minwfunc(c2)
    c3 = np.array(list(range(0,h))) - col_half
    c3 = max0func(c3)
    c4 = np.array(list(range(0,h))) + col_half
    c4 = minhfunc(c4)
    
    """sumbox = lambda t: np.sum(pix[t[0]:t[1]],pix[t[2]:t[3]])
    sumboxfunc = np.vectorize(sumbox)
    
    sumbox = lambda t: np.sum(pix[t[0]:t[1],t[2]:t[3],t[5]])
    sumboxfunc = np.vectorize(sumbox)"""
    
    new_img = pix.copy()
    for i in c1:
        for j in c3:
            for k in range(0,c):
              temp = pix[c3[j]:c4[j]+1,c1[i]:c2[i]+1,k]
              new_img[j,i,k]   = np.sum(temp)
                
    
    divisor = (neighbourhood[0] * neighbourhood[1]) - 1
    new_img = (new_img - pix)/divisor
    dest_name = mu.save_img(new_img,image_name,str(neighbourhood).replace(',','-'))

    
    
    
def CallMe():
    image_name = 'color.png'
    image_name = 'cat.jpg'
    neighs = [3,5,7,10,15,20,25,30,40,50]
    #neighs = [15,25,30,40,50]
    for n in neighs:
        neighbourhood = (n,n)
        spatial_reduction(image_name,neighbourhood)
    
    
        
if __name__ == "__main__":
    CallMe()
    
    
