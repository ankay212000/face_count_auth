import numpy as np
import cv2
import time
import os



check=os.path.isdir("Images")
if(check==False):
    os.mkdir("Images")
 
def save(rollno):
    font=cv2.FONT_HERSHEY_SIMPLEX
    video = cv2.VideoCapture(0)
    f=0
    p=-1
    while(1):
        check,frame=video.read()
        frame=cv2.flip(frame,1)
        cv2.rectangle(frame,(190,120,250,250),(0,0,0),2)
        crop=frame[120:370,190:440]
        
        frame[0:120,0:640]=50
        frame[370:480,0:640]=50
        frame[120:370,0:190]=50
        frame[120:370,440:640]=50
        
        key=cv2.waitKey(1)
        
        if(f==0):
            cv2.putText(frame,"Press Space to take image",(100,40),font,1,(255,0,0),2)
            if(key==ord(' ')):
                time.sleep(0.5)
                cv2.imwrite(f"./Images/{rollno}_1.jpg",crop)
                cv2.putText(frame,"1/2 Image Saved",(200,40),font,1,(255,0,0),2)
                f=1
        if(f>0 and f<=40):
            cv2.putText(frame,"1/2 Image Saved",(200,40),font,1,(255,0,0),2)
            f=f+1
        if(f==41):
            p=0
        if(p==0):
            cv2.putText(frame,"Tilt your head slightly and press space.",(0,40),font,1,(255,0,0),2)
            f=f+1
            if(key==ord(' ')):
                time.sleep(0.5)
                cv2.imwrite(f"./Images/{rollno}_2.jpg",crop)
                cv2.putText(frame,"2/2 Image Saved",(200,40),font,1,(255,0,0),2)
                p=1
        if(p>0):
            cv2.putText(frame,"2/2 Image Saved",(200,40),font,1,(255,0,0),2)
            p=p+1
            if(p==50):
                break
            
        cv2.imshow("Capture",frame)
        if(key==27):
            break   
        
    video.release()
    cv2.destroyAllWindows()