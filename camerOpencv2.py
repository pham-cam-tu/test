import cv2
import numpy as np
from PIL import Image
 
def pic_face_mask(img_file,result_file):
    # 顔分類器
    cascade_file = r'C:\opencv\sources\data\haarcascades\haarcascade_frontalcatface.xml'
    cascade = cv2.CascadeClassifier(cascade_file)

    """顔を検出してマスクする"""
    img = cv2.imread(img_file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # グレースケールに変換
    face_list = cascade.detectMultiScale(img_gray, scaleFactor=1.71,minNeighbors=1,minSize=(150, 150))  # 顔検出
 
    for (x, y, w, h) in face_list:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=10)
    cv2.imwrite(result_file, img)

    """for (x,y,w,h) in face_list:
        face_img = img[y:y+h, x:x+w]
    filename = "image/face_" + str(x) + "-" + str(y) + ".jpg"
    cv2.imwrite(filename, face_img)"""
 
 
if __name__ == '__main__':
    pic_face_mask('image/images.jpeg','image/result.png')
