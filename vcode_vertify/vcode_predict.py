from keras.models import load_model
import cv2
import os
import sys
import numpy as np

img_shape = (64,64,3)

def get_label_num(string,n):
    
    img_shape = (64,64,3)
    
    label = []
    
    for i in range(n):
        if(string[i].isdigit()):
            label.append(int(string[i]))
            #print(i)
        else:
            label.append(int(ord(string[i])-55))
            #print(i)
    #print(label)
    return label

def add_eg_num_Labels(label_name):
    for i in range(10):
        #print(str(i)+" is added in Label !")
        label_name.append(str(i))
    for i in range(10,36):
        #print(str(i)+" is added in Label !")
        label_name.append(str(i))
        
    return label_name
    
def imread(path): #注意 cv2是gbr!
    if img_shape[2] == 1:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(path)
    img = cv2.resize(img, (img_shape[1], img_shape[0]), interpolation=cv2.INTER_CUBIC)
    img = img/255
    img = np.reshape(img,(1,img_shape[0], img_shape[1],img_shape[2]))
    return img

def get_vcode_ByNN(path):

    
    label_name = []

    label_name = add_eg_num_Labels(label_name)


    if not os.path.isfile(path):
        print("圖片不存在")
        return '0000'
    else:
        image = imread(path)
        model = load_model('my_model.h5')
        result = model.predict(image)
        vcode = label_name[np.argmax(result[0])],label_name[np.argmax(result[1])],label_name[np.argmax(result[2])],label_name[np.argmax(result[3])]
        return vcode
