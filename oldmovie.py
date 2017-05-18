import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

while(1):
    ret,frame=cap.read()
    
    
    r=frame.shape[0]
    c=frame.shape[1]

    
    #creates sepia effect by altering the RGB values
    #cv2.add used to ensure value doesn't go beyond 255    
    frame[:,:,0] = np.array((cv2.add(frame[:,:,0] * 0.272 , frame[:,:,1] * 0.534 , frame[:,:,2] * 0.131)))
    frame[:,:,1] = np.array((cv2.add(frame[:,:,0] * 0.349 , frame[:,:,1] * 0.686 , frame[:,:,2] * 0.168)))
    frame[:,:,2] = np.array((cv2.add(frame[:,:,0] * 0.393 , frame[:,:,1] * 0.769 , frame[:,:,2] * 0.189)))
   

    #Below generating some random numbers for random time for line and circles

    a=random.random()           #for line
    b=random.randrange(0,10)    #for circle
    z=random.random()           #for Frame movement
    
    if z<0.05:      #Moving frame 20 pixel upwards randomly
        frame[:r-20,:,:]=frame[20:r,:,:]
        frame[r-20:,:,:]=(0,0,0)

    if a < 0.20:    #LINE
        col=int((c/8)+10*random.random())      
        cv2.line(frame,(col,0),(col,r-1),(0,0,0),1)

    if b<5:         #Circles
        for i in range(random.randrange(0,4)):
            size=b*random.randrange(1,3)
            rr=random.randrange(0,r)    #location
            rc=random.randrange(0,c)
            cv2.circle(frame,(rc,rr),size,(0,0,0),-1)
        
    cv2.imshow('old movie',frame)
    k=cv2.waitKey(25)
    if k==27:
        break

cv2.destroyAllWindows()


