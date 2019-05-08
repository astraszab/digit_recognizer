#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:29:34 2019

@author: astraszab
"""

import numpy as np
import tensorflow as tf
import imageio
from PIL import Image
from keras.models import load_model

model = load_model('model/mnist_model.h5')
graph = tf.get_default_graph()


def load_image(path, width=28):
    '''Load an image from a file with specified path'''
    img = imageio.imread(path)
    img = np.array(Image.fromarray(img).resize((width, width)))
    img = np.mean(img, axis=-1)
    img = np.resize(img, (1, width, width, 1))
    img /= 255
    return img

def predict_from_model(data):
    '''Make a prediction from data.'''
    prediction = 0
    global graph, model
    with graph.as_default():
        prediction = model.predict(data)
    certainty = np.max(prediction)
    prediction = np.argmax(prediction)
    return prediction, certainty

def predict_from_json_data(json_data, width=28):
    '''Format json data and makes a prediction from it'''
    formatted_data = np.array([float(val) for val in json_data.split(',')])
    formatted_data = formatted_data[[i*4 for i in range(784)]]
    formatted_data = np.resize(formatted_data, (1, width, width, 1)) / 255
    prediction, certainty = predict_from_model(formatted_data)
    prediction_msg = ""
    if certainty < 0.9:
        prediction_msg = "Not sure... Maybe it's {0} or not a digit.".format(prediction)
    else:
        prediction_msg = "Prediction: {0}".format(prediction)
    return prediction_msg

def main():
    X = load_image('temp/image.jpg')
    prediction, certainty = predict_from_model('model/mnist_model.h5', X)
    if certainty < 0.99:
        print("Not sure... Maybe it's {0} or not a digit.".format(prediction))
    else:
        print("Prediction: {0}".format(prediction))
    
if __name__=='__main__':
    main()