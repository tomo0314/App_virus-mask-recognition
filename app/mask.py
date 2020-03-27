# -*- coding: utf-8 -*-
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

classes_dict = {"no-mask_data":0,
                "mask_data":1}
classes = ["no-mask", "mask"]
img_width, img_height = 128, 128

def detect_mask(img_path):
  img=Image.open(img_path)
  img = img.resize((img_width, img_height))
  img = np.array(img)
  #検査対象画像の出力
  #plt.imshow(img)
  img=img.reshape([1,128,128,3])
  pred=model.predict(img)
  stt = f"マスクを装着している確率{pred[0][1]*100}%\n"
  if pred.argmax() == 1:
    str+="マスクを装着しています"
  else:
    str+="マスクを装着していません"
  return str


os.chdir('./Testdata')
path = os.getcwd()

path_x = join(path,sys.argv[1])
#strに結果として表示して欲しい文字列を格納しています
str=detect_mask(path_x)

