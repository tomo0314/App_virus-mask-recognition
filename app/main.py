# -*- coding: utf-8 -*-
#以下の環境で実行しています
#Python 3.7.4
#keras                     2.3.1
#tensorflow                2.0.0
#numpy                     1.17.2
#pillow                    6.2.0
#matplotlib                3.1.1

import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
import sys

import pickle
def unpickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f, encoding='bytes')

import os
from os.path import join
os.chdir('./Preprocessed') 
path = os.getcwd()
print(path)

img_list = unpickle(join(path,'img_list.pickle'))
label_list = unpickle(join(path,'label_list.pickle'))

from keras.models import Sequential, model_from_json
model = model_from_json(open(join(path, 'mask_NN.json'), 'r').read())
model.load_weights(join(path,'mask_NN_weight.h5'))

from matplotlib import pyplot as plt
classes_dict = {"no-mask_data":0,
                "mask_data":1}
classes = ["no-mask", "mask"]
img_width, img_height = 128, 128

from PIL import Image
import numpy as np
def detect_mask(img_path):
  img=Image.open(img_path)
  img = img.resize((img_width, img_height))
  img = np.array(img)
  #検査対象画像の出力
  #plt.imshow(img)
  img=img.reshape([1,128,128,3])
  pred=model.predict(img)
  print(f"マスクを装着している確率{pred[0][1]*100}%")
  if pred.argmax() == 1:
    print("マスクを装着しています")
  else:
    print("マスクを装着していません")

os.chdir('./../Testdata')
path = os.getcwd()
print(path)

path_x = join(path,sys.argv[1])
detect_mask(path_x)

