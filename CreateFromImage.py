import cv2, os
import sqlite3
from sqlite3 import Error
import numpy as np

from PIL import Image
# khai báo thư viện nhận diện khuôn mặt
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def InsertOrUpdate (Id, Name,Age ):
    conn= sqlite3.connect("DataBase.db")
    c=conn.cursor()
    cmd= "insert Into Information (Id,Name,Age) Values('"+Id+"','"+Name+"','"+Age+"')"
    c.execute(cmd)
    conn.commit()
    c.close()
    conn.close()
# khai báo đường dẫn tới thư viện ảnh có swanx
path="Image"
# nhập 1 cho user mới
face_id = input('nhập id :')
face_name = input('nhập tên :')
face_age= input('Nhập tuổi : ')
InsertOrUpdate(str(face_id),str(face_name),str(face_age))
# vòng lặp lấy tên ảnh ra


def getImagesAndLabels(path):
# lấy đường dẫn ảnh
    count = 0
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
       # đọc ảnh
        image =  cv2.imread(imagePath)
       # Convert ảnh ra mà xám
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       # Lấy khuôn mặt xuất hiện trong khung hình
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
       # ghi ảnh vào dữ liệu
        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1
            #ghi ảnh khuôn mặt vào dataset
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        print(imagePath)
        cv2.imshow('frame', image)


getImagesAndLabels(path)
