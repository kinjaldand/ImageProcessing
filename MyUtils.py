# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:29:21 2020

@author: Kinjal Dand

Commonly used python functions

"""

from PIL import Image
import numpy as np
import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR,"Data")

def get_file_extension(img_path):
    filename, file_extension = os.path.splitext(img_path)
    return filename, file_extension

def get_filename_from_path(dest_path):
    return os.path.basename(dest_path)

def get_file_size(file_name):
    file_path = get_image_path(file_name)
    size_bytes = os.path.getsize(file_path)
    #print(file_path,size_bytes)
    return size_bytes

def get_image_path(image_name):
    if image_name.startswith(DATA_FOLDER) == False:
        return os.path.join(DATA_FOLDER,image_name)
    else:
        return image_name
    
def handle_path(image_name,append_text=""):
    dest_path = get_image_path(image_name)
    append_text = str(append_text)
    if append_text.strip()!="":
        filename, file_extension = get_file_extension(dest_path)
        
        if append_text.startswith('_')==False:
            append_text = "_" +append_text
        dest_path = filename + append_text + file_extension
    return dest_path
    
def save_img(img,image_name,append_text=""):
    dest_path = handle_path(image_name,append_text)
    if isinstance(img,np.ndarray):
        cv2.imwrite(dest_path,img)
    else:
        #img = img.astype(np.uint8)
        #img = Image.fromarray(img)
        img.save(dest_path)
    return get_filename_from_path(dest_path)
    

    
def get_image_as_array(image_name):
    file_path = get_image_path(image_name)
    img = Image.open(file_path)
    pix = np.array(img)
    #print(type(img)) #<class 'PIL.JpegImagePlugin.JpegImageFile'>
    #print(type(pix)) #<class 'numpy.ndarray'>
    return pix
    
def get_image_as_cv2(image_name):
    file_path = get_image_path(image_name)
    img = cv2.imread(file_path)
    #print(type(img))  #<class 'numpy.ndarray'>
    return img
    
   
