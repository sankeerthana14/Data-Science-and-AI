#CONCATENATING 
"""
This Python File concatenates all the images into 1 single matrix/grid.
"""
#Importing Necessary Libraries
import numpy as np
import cv2
import os

#Importing Necessary Files
import PATHS as PATHS
import detect_spots_v1 as DETECT

#Horizontally concatenating all the images in one row
rows = []
for elements in DETECT.ordered_imgs:
    print(elements)
    temp = 0
    for i in range(len(elements)):
        img = cv2.imread(os.path.join(PATHS.SIMPLE_DIR,elements[i]))
        if i == 0:
            temp = img
        else:
            concat_row = cv2.hconcat([temp, img])

    rows.append(concat_row)

#Vertically concatenating all the rows
temp = 0
for i in range(len(rows)):
    if i == 0:
        temp = rows[i]
    else:
        concat_col = cv2.vconcat([temp, rows[i]])
        temp = concat_col

cv2.imshow('final_img', concat_col)
cv2.waitKey(0)

    

    



