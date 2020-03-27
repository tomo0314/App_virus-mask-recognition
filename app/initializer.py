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
model = model_from_json(open(join(path, 'mask_NN.json'), 'r').read())
model.load_weights(join(path,'mask_NN_weight.h5'))