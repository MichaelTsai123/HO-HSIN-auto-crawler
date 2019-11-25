# coding: utf-8



from keras.models import load_model
import cv2
import os
import sys
import numpy as np

img_shape = (64,64,3)
label_name = ["good","paper","scissors","stone"]
num_classes = len(label_name)

def imread(path): #注意 cv2是gbr!
    if img_shape[2] == 1:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(path)
    img = cv2.resize(img, (img_shape[1], img_shape[0]), interpolation=cv2.INTER_CUBIC)
    img = img/255
    img = np.reshape(img,(1,img_shape[0], img_shape[1],img_shape[2]))
    return img

if len(sys.argv) < 2:
    print("python predict.py 檔名")
    exit()
if not os.path.isfile(sys.argv[1]):
    print("圖片不存在")
    exit()
image = imread(sys.argv[1])
model = load_model('my_model.h5')
result = model.predict(image)

print("結果",label_name[np.argmax(result[0])])