# -*- coding: utf-8 -*-
#mask.py
#以下の環境で実行しています
#Python 3.7.4
#keras                     2.3.1
#tensorflow                2.0.0
#numpy                     1.17.2
#pillow                    6.2.0
#matplotlib                3.1.1
import os
from os.path import join
import sys
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import initializer

classes_dict = {"no-mask_data":0,
                "mask_data":1}
classes = ["no-mask", "mask"]
img_width, img_height = 128, 128

def detect_mask(img_path):
  model = initializer.model
  img=Image.open(img_path)
  img = img.resize((img_width, img_height))
  img = np.array(img)
  #検査対象画像の出力
  #plt.imshow(img)
  img=img.reshape([1,128,128,3])
  pred=model.predict(img)
  output = f"マスクを装着している確率{pred[0][1]*100}%\n"
  if pred.argmax() == 1:
    output+="マスクを装着しています"
  else:
    output+="マスクを装着していません"
  return output


def mask_test(file_name):
    os.chdir('./Testdata')
    path = os.getcwd()
    path_x = join(path,file_name)
    #outputに結果として表示して欲しい文字列を格納しています
    output=detect_mask(path_x)
    print(output)
    os.chdir('./..')

