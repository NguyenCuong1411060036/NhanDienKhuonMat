import sqlite3
from sqlite3 import Error
import cv2

def InsertOrUpdate (Id, Name,Age ):
    conn= sqlite3.connect("DataBase.db")
    c=conn.cursor()
    cmd= "insert Into Information (Id,Name,Age) Values('"+Id+"','"+Name+"','"+Age+"')"
    c.execute(cmd)
    conn.commit()
    c.close()
    conn.close()
vid_cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('nhập id :')
face_name = input('nhập tên :')
face_age= input('Nhập tuổi : ')
count = 0

InsertOrUpdate(str(face_id),str(face_name),str(face_age))
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
