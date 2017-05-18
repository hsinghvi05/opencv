#incomplete but working

import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)
i=10

ini=False

while(1):
    ret,frame=cap.read()
    if not ini:
        img2=frame
        ini=True    
    
    #saves a frame for 20 iterations and merges it    
    i=i+1
    if i>20:
        i=0
        img2=frame

    
    img3=cv2.addWeighted(frame,0.3,img2,0.7,0) 

            
    cv2.imshow('ghost',img3)
    k=cv2.waitKey(25)
    if k==27:
        break
