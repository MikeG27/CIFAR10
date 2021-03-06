#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:33:58 2018

@author: michal
"""
# Import libraries

# 1.Keras

from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator

from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import BatchNormalization


# 2 Other librariess
import numpy as np
import pandas as pd
import myplots as myp
#import sort_images as srt
import os
import time 

# =============================================================================
#                            # DATA OVIERVIEW
# =============================================================================

(X_train,y_train),(X_test,y_test) = cifar10.load_data()
class_names = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]


# Define parameters
m_train = X_train.shape[0]
m_test = X_test.shape[0]
num_px = X_train[25].shape[0]
num_ch = X_train[25].shape[2]

batch_size = 128
epochs = 200
num_class = 10
class_names = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

#myp.plot_sample_img(X_train, y_train, names = class_names,save_fig=True)

# =============================================================================
#                           Preprocessing 
# =============================================================================

X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# =============================================================================
#                            # Define CNN model
# =============================================================================

print("\n3. Model summary : " )


tic = time.time()

model = Sequential()

model.add(Conv2D(32,(3,3),activation="relu",input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64,(3,3),activation="relu",))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(MaxPooling2D((2,2)))

model.add(Conv2D(128,(3,3),activation="relu",))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=200, batch_size=512,validation_split = 0.2)

myp.plot_training(history)
myp.plot_confusion_matrix(model,X_test,y_test,class_names)

toc = time.time()
print("Exec time",str((toc-tic)) + "s")
os.system('say "Learning done"')

model.save("CIFAR-model1")




