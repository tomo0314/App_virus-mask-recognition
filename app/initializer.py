#initializer
import tensorflow as tf
import os
import warnings
warnings.filterwarnings('ignore')

from os.path import join
os.chdir('./Preprocessed') 
path = os.getcwd()

from keras.models import Sequential, model_from_json
import keras
graph = tf.get_default_graph()

session = keras.backend.get_session()
init = tf.global_variables_initializer()
session.run(init)

model = model_from_json(open(join(path, 'mask_NN.json'), 'r').read())
model.load_weights(join(path,'mask_NN_weight.h5'))
model._make_predict_function()

os.chdir('./..')