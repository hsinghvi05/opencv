import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret,frame=cap.read()
    
    r=frame.shape[0]
    c=frame.shape[1]

    #flipping to get 4 opposite images
    img=np.zeros((r,c,3),np.uint8)
    img[:r/2,:c/2:]=frame[:r/2,:c/2:]
    img2=img
    img2=cv2.flip(img,1)
    img=cv2.addWeighted(img,1,img2,1,0)
    img2=img
    img2=cv2.flip(img,0)
    img=cv2.addWeighted(img,1,img2,1,0)

    cv2.imshow('asdf',img)
    k=cv2.waitKey(1)
    if k==27:
        break