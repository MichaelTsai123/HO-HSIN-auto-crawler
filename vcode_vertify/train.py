# coding: utf-8

import numpy as np
import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.models import Model


import cv2
import os
from os import listdir
from os.path import isfile, join




img_shape = (64,64,3)
label_name = ["good","paper","scissors","stone"]
test_path = []
for label in label_name:
    test_path.append(label+"_test")
train_path = []
for label in label_name:
    train_path.append(label+"_train")
dir_path = "convert_video/"
num_classes = len(label_name)

def build_model():
    tensor_input = Input(img_shape)
    tensor_output = tensor_input
    tensor_output = Conv2D(filters=16, kernel_size=(3,3), padding="same")(tensor_output)
    tensor_output = MaxPooling2D(pool_size=(2, 2))(tensor_output)
    tensor_output = Conv2D(filters=16, kernel_size=(3,3), padding="same")(tensor_output)
    tensor_output = MaxPooling2D(pool_size=(2, 2))(tensor_output)
    tensor_output = Conv2D(filters=16, kernel_size=(3,3), padding="same")(tensor_output)
    tensor_output = MaxPooling2D(pool_size=(2, 2))(tensor_output)
    tensor_output = Conv2D(filters=16, kernel_size=(3,3), padding="same")(tensor_output)
    tensor_output = MaxPooling2D(pool_size=(2, 2))(tensor_output)
    tensor_output = Flatten()(tensor_output)
    tensor_output = Dropout(0.5)(tensor_output)
    tensor_output = Dense(num_classes, activation='softmax')(tensor_output)
    model = Model(inputs=tensor_input, outputs=tensor_output)
    print(model.summary())
    return model


def imread(path): #注意 cv2是gbr!
    if img_shape[2] == 1:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(path)
    print(path)
    img = cv2.resize(img, (img_shape[1], img_shape[0]), interpolation=cv2.INTER_CUBIC)
    img = img/255
    return img



#load train_data
train_data = []
train_label = []
for count  in range(len(train_path)):
    mypath = dir_path+train_path[count]
    train_image_path = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for path in train_image_path:
        #print(mypath+"/"+path)
        train_data.append(imread(mypath+"/"+path))
        train_label.append(count)
x_train = np.asarray(train_data)
y_train = np.asarray(train_label)
y_train = keras.utils.to_categorical(y_train)



#load test_data
test_data = []
test_label = []
for count  in range(len(test_path)):
    mypath = dir_path+test_path[count]
    test_image_path = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for path in test_image_path:
        #print(mypath+"/"+path)
        test_data.append(imread(mypath+"/"+path))
        test_label.append(count)
x_test = np.asarray(test_data)
y_test = np.asarray(test_label)
y_test = keras.utils.to_categorical(y_test)




model = build_model()
# 定義訓練方式  
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])  
  
# 開始訓練  
train_history = model.fit(x_train,y_train, validation_split=0.2,  
                          epochs=5, batch_size=32, verbose=2) 


#使用測試圖片測試
val_ = model.evaluate(x_test, y_test)
print(val_)

#殂存
model.save("my_model.h5")