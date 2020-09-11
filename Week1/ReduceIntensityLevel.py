from PIL import Image
import numpy as np

def reduceIntensity(img_path):
  img = Image.open(img_path)
  pix = np.array(img)
  initial_level = 2
  end_level = 256
  levels = []
  while (initial_level<=end_level):
    levels.append(initial_level)
    initial_level = initial_level*2
    
  print(levels)
    
