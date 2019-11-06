import face_recognition as fr
import cv2
import numpy as np 
import pickle
import time 
import os
import dbms

def attend():
    start_time = time.time()
    start_time=time.ctime(start_time)
    count=0
    faceCount={} 
    exist=os.path.isfile("dataset.dat")
    if(exist==False):
        print("No Registration")
        return
    else:    
        font=cv2.FONT_HERSHEY_SIMPLEX
        #Loading dataset.dat file
        file=open("./dataset.dat",'rb')
        Ens,Names,ID=pickle.load(file)
        file.close()
        Names2=Names.tolist()
        video = cv2.VideoCapture(0)
        while(1):
            #Load test image
            check,img=video.read()
            img = cv2.resize(img, (640,480))
            #img=cv2.resize(img,(640,480))
            img=cv2.flip(img,1)
            test=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            print(img.shape)
            name="Unknown"
            faces_loc=fr.face_locations(test)
            en_faces=fr.face_encodings(test,faces_loc)
            for (top,right,bottom,left),en in zip(faces_loc,en_faces):
                name="Unknown"
                matches=fr.compare_faces(Ens,en,0.50)
                if(True in matches):
                    index=matches.index(True)
                    name=Names[index]
                    id=ID[index]
                    if(name in Names2):
                        count+=1
                        dbms.send(name,start_time[0:11]+start_time[20:],id,'0',start_time[11:20],0,'A',0)
                        Names2.remove(name)
                        Names2.remove(name)
                        faceCount[name]=count    
                cv2.putText(img,f"{name}",(left,top),font,1,(255,255,255),1)
                cv2.rectangle(img,(left,top),(right,bottom),(0,0,255),1)
                if(name=="Unknown"):
                    continue
                else:
                    cv2.rectangle(img,(left,bottom),(left+30,bottom+25),(0,0,255),cv2.FILLED)
                    cv2.putText(img,str(faceCount[name]),(left,bottom+22),font,1,(255,255,255),1)
            cv2.imshow("Capture",img)
            key=cv2.waitKey(1)
            if(key==ord(' ')):
                break
    video.release()
    cv2.destroyAllWindows()      

attend()

       