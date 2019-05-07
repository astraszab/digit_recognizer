#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:29:34 2019

@author: astraszab
"""

import numpy as np
import imageio
from PIL import Image
from keras.models import load_model


def load_image(path, width=28):
    '''Load an image from a file with specified path'''
    img = imageio.imread(path)
    img = np.array(Image.fromarray(img).resize((width, width)))
    img = np.mean(img, axis=-1)
    img = np.resize(img, (1, width, width, 1))
    img /= 255
    return img

def predict_from_model(path, data):
    '''Load a model and make a prediction from data.'''
    model = load_model(path)
    prediction = model.predict(data)
    certainty = np.max(prediction)
    prediction = np.argmax(prediction)
    return prediction, certainty

def main():
    X = load_image('temp/imgNone.jpg')
    prediction, certainty = predict_from_model('model/mnist_model.h5', X)
    if certainty < 0.99:
        print("Not sure... Maybe it's {0} or not a digit.".format(prediction))
    else:
        print("Prediction: {0}".format(prediction))
    
if __name__=='__main__':
    main()