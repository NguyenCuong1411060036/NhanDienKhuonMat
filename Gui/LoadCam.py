from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import sqlite3
from sqlite3 import Error

vid_cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
connection= sqlite3.connect("DiemDanh.db")
# lấy Id lớn nhất có trong database để tiến hành gán id tự động cho hình ảnh chụp được/ đồng bộ hóa giữa hình ảnh và thông tin nhân viên
result = connection.execute("SELECT id FROM NhanVien ORDER BY id DESC limit 1")
values= result.fetchone()
if(values[0]>0):
    face_id= values[0] + 1
else :
    face_id=1
print("faceid "+str(face_id))
count = 0
while(True):
        _, image_frame = vid_cam.read()

        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)

            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('frame', image_frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif count>100:
            break
vid_cam.release()
cv2.destroyAllWindows()
