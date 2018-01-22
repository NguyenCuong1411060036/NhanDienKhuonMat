import string
import os
import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path="dataset"

def getProfile(id):
    conn= sqlite3.connect("DataBase.db")
    cmd="select * from Information where Id =" +str(id)
    cursor= conn.execute(cmd)
    profile= None
    for row in cursor:
        profile=row
    conn.close()
    return profile


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id = recognizer.predict(gray[y:y+h,x:x+w])

           # Check the ID if exist

        if(str(Id).find('1,')!=-1):
            Id="1"
        if(str(Id).find('2,')!=-1):
            Id="2"
        if(str(Id).find('3,')!=-1):
            Id="3"
        if(str(Id).find('4,')!=-1):
            Id="4"
        profile= getProfile(Id)
        if(profile != None):
            cv2.putText(im, "Name: "+str(profile[1]), (x,y+h+40), font, 2, (255,0,0), 3)
            cv2.putText(im, "age : "+str(profile[2]), (x,y+h+90), font, 2, (255,0,100), 3)
        else :
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)




    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im)

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
