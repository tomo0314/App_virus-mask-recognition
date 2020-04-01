#initializer
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
import sys

import os
from os.path import join
os.chdir('./Preprocessed') 
path = os.getcwd()

from keras.models import Sequential, model_from_json
import keras
from tensorflow.python.keras.backend import set_session

sess = tf.Session()
graph = tf.get_default_graph()

#sessionの設定 //Flaskでは処理ごとにtensorflowのモデルが初期化されてしまうため、セッションを設定して回避
set_session(sess)
model = model_from_json(open(join(path, 'mask_NN.json'), 'r').read())
model.load_weights(join(path,'mask_NN_weight.h5'))
model._make_predict_function()

os.chdir('./..')