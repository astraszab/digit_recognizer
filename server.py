#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:34:33 2019

@author: astraszab
"""

import predict_utils
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/_predict')
def predict():
    pixels = request.args.get('pixels', type=str)
    prediction = predict_utils.predict_from_json_data(pixels)
    return jsonify(result=prediction)

if __name__=='__main__':
    app.run(debug=True)