#import tensorflow as tf
#import matplotlib.pyplot as plt
import json
#import matplotlib.image as img
from PIL import Image, ImageFilter
import numpy as np
import os

annotation = json.load(open("hand_pose/Dataset/annotation.json"))

path = "hand_pose/Dataset/Color"
files = os.listdir(path)

save_path = "dataset/train/hand"
save_path2 = "dataset/valid/hand"
counter = 0
dl = len(annotation)
for filename, annotations in annotation.iteritems():
    picname = filename[0:-2]
    picname += ".jpg"
    pic_path = path+picname
    image = Image.open(pic_path)
    
    A = np.array(annotations)
    hand_range = (np.min(A[:,0])-10,np.min(A[:,1])-10,np.max(A[:,0])+10,np.max(A[:,1])+10)
    new_pic = image.crop(hand_range)
    if counter <= 4000:
        new_pic.save(save_path+picname)
    elif counter <= 6000:
        new_pic.save(save_path2+picname)
    else:
        break
    
    counter += 1
    print(counter,'  out of:  ',dl )