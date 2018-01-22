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
    conn= sqlite3.connect("Database.db")
    cmd="select * from Infomation where Id =" +str(id)
    cursor= conn.execute(cmd)
    profile= None
    for row in cursor:
        profile=row
    conn.close()
    return profile

font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.imread('Obama.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray_image, 1.2,5)
for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(225,0,0),2)
        Id = recognizer.predict(gray_image[y:y+h,x:x+w])

        if(str(Id).find('1,')!=-1):
            Id="cuong"

        if(str(Id).find('2,')!=-1):
            Id="Obama"
        else:
            Id="Unknow"


        cv2.putText(image, str(Id), (x,y-10), font,0.5, (0,255,255),1)

           # cv2.putText(image, Id, (x,y+h+40), font, 2, (255,0,0), 3)
            #cv2.putText(image, "age : "+str(profile[2]), (x,y+h+90), font, 2, (255,255,255), 3)
# Display the video frame with the bounded rectangle
cv2.imshow('img',image)
cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()
