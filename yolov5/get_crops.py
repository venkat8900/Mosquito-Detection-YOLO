import os
import glob
import pandas as pd
import numpy as np
import cv2


# get all the file names in current directory

image_file_names = os.listdir('/home/venkat/Venkat/Mosquito Detection/yolov5/runs/detect/exp3/labels')

# add all the names into data frame

w = 416
h = 416

final_df = []
label_path = '/home/venkat/Venkat/Mosquito Detection/yolov5/runs/detect/exp3/labels'

for item in image_file_names:
    
    filelabel = open(os.path.join(label_path, item), "r")
    lines = filelabel.read().split('\n')
    obj = lines[:len(lines) - 1]
    row = []
    max_conf = 0
    for i in range(0, int(len(obj))):
        
        splited = obj[i].split(' ')
        
        try:
            img_name = item[:-4]
            img_name = img_name + '.jpg'
            x1 = float(splited[1])
            y1 = float(splited[2])
            w1 = float(splited[3])
            h1 = float(splited[4])
            
            cur_conf = float(splited[5])
            if cur_conf > max_conf:
                xmin = int((x1*w) - (w1*w)/2.0)
                ymin = int((y1*h) - (h1*h)/2.0)
                xmax = int((x1*w) + (w1*w)/2.0)
                ymax = int((y1*h) + (h1*h)/2.0)
        except exception as e:
            print(e)
            print("File Not in YOLO format")
            
            
    row.append(img_name)
    row.append(xmin)
    row.append(ymin)
    row.append(xmax)
    row.append(ymax)
    row.append(splited[0])
    
    final_df.append(row)

df = pd.DataFrame(final_df, columns = ['image', 'xmin', 'ymin', 'xmax', 'ymax', 'label'])

                