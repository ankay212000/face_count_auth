import face_recognition as fr
import numpy as np
from os import path
import pickle
import pandas as pd
import RegImage 

name=input("Enter your name: ")
id=input("Enter your roll_no.: ")
name=name[0].upper()+name[1:].lower()
Name=[]
exist=path.isfile('./dataset.dat')
if(exist):
    #Read data from the data.dat file and check if id already exists.
        fileobj=open("dataset.dat",'rb')
        r_ens,r_names,r_ids=pickle.load(fileobj)
        fileobj.close()
        if(name in r_names):
            lst=r_names.tolist()
            print("Already registered with id: %d"%{r_ids[lst.index(name)]})
        else:
            RegImage.save(id)

            image1=fr.load_image_file(f"./Images/{id}_1.jpg")
            enc1=fr.face_encodings(image1)[0]
            image2=fr.load_image_file(f"./Images/{id}_2.jpg")
            enc2=fr.face_encodings(image2)[0]

            Names=np.array([name,name])
            Encs=np.array([enc1,enc2])
            Ids=np.array([id,id])

            '''Name=[name]
            dict={'Name':Name}
            df=pd.DataFrame(dict)
            df.to_csv('Info.csv',mode='a',header=False)'''

            Encs=np.append(r_ens,Encs,axis=0)
            Names=np.append(r_names,Names)
            Ids=np.append(r_ids,Ids)

            #Overwriting the data file with new data.
            fileobj1=open("dataset.dat",'wb')
            pickle.dump((Encs,Names,Ids),fileobj1)
            fileobj1.close()       
else:
    RegImage.save(id)
    image1=fr.load_image_file(f"./Images/{id}_1.jpg")
    enc1=fr.face_encodings(image1)[0]
    image2=fr.load_image_file(f"./Images/{id}_2.jpg")
    enc2=fr.face_encodings(image2)[0]

    Names=np.array([name,name])
    Encs=np.array([enc1,enc2])
    Ids=np.array([id,id])

    '''Name=[name]
    dict={'Name':Name}
    df=pd.DataFrame(dict)
    df.to_csv('Info.csv')'''

    fileobj=open("dataset.dat",'wb')
    pickle.dump((Encs,Names,Ids),fileobj)
    fileobj.close()
