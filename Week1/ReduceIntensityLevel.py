# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:29:21 2020

@author: Kinjal Dand

Description:

Quantization : 
-   Determines number of values that image pixel can take
-   More levels, more fine grained , detailed and smooth image becomes
-   Reducing levels reduces no. of unique values that pixels in image can take.
-   This reduces memory required for storing image file.
-   Hence reducing storage and transmission bytes for file
-   The trade - off between reduction in size and image quality is inversely proportional
-   Observation : reducing from 256 to (128 or 64) pixel level reduces size to half without degrading image quality significantly.

"""

from PIL import Image
import numpy as np
import os
import ImageUtils as iu
import MyUtils as mu

initial_level = 2
end_level = 256
levels = []
while (initial_level<end_level):
    levels.append(initial_level)
    initial_level = initial_level*2

levels = levels[::-1]    
print(levels)
    
def reduceIntensity(image_name,expected_level):
    pix = mu.get_image_as_array(image_name)

    before_max_pix  = np.max(pix)
    before_unique_pix  = np.unique(pix)
    
    if expected_level not in levels:
        return 'expected_level should be in '+str(levels)
    

    divisor = 256/expected_level
    pix = np.floor(np.floor(pix/divisor) * divisor)
    pix = pix.astype(np.uint8)
    
    after_max_pix  = np.max(pix)
    after_unique_pix  = np.unique(pix)

    
    im = Image.fromarray(pix)
    dest_name = mu.save_img(im,image_name,expected_level)

    #print(before_unique_pix)
    print(expected_level,len(after_unique_pix),mu.get_file_size(dest_name),mu.get_file_size(image_name))
    
    
def CallMe():
    image_name = 'pedestrian.jpg'
    dest_name = iu.conv_save_to_gray(image_name)
    for l in levels:
        reduceIntensity(image_name,l)
        reduceIntensity(dest_name,l)
        
if __name__ == "__main__":
    CallMe()
    
    
