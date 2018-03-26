
import cv2, os

import numpy as np

from PIL import Image

# training hình ảnh thành file yml , lưu dữ liệu nhận dạng ở dạng text

recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer=cv2.face.createLBPHFaceRecognizer()


detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]

    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:

            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
# thư viện ảnh là tập hợp những hình ảnh đã được cắt ở dạng khuôn mặt.
faces,ids = getImagesAndLabels('ThuVienAnh')

recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')
