# -*- coding: utf-8 -*-
"""Build.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FuXQZLQKX6O3vp1z-iNvO4S1ESBU-JIK

**Bild Python code**

**Import Libraries**
"""

import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask,request, render_template

app=Flask(__name__,template_folder="templates")

@app.route('/file:///D:/Nalaiyathiran%20Project/Pre-processing%20-%20development/Flask/Templetes/home.html', methods=['GET'])
def index():
  return render_template('home.html')
@app.route('/file:///D:/Nalaiyathiran%20Project/Pre-processing%20-%20development/Flask/Templetes/home.html', methods=['GET'])
def about():
  return render_template('home.html')
@app.route('/file:///D:/Nalaiyathiran%20Project/Pre-processing%20-%20development/Flask/Templetes/upload.html', methods=['GET'])
def page():
  return render_template('upload.html')

@app.route('/y_predict', methods=['GET','POST'])
def y_predict():
  print("[INFO] loading model...")
  model = pickle.loads(open('fdemand.pkl',"rb").read())
  input_features = [float(x) for x in request.form.values()]
  features_value = [np.array(input_features)]
  print(features_value)

  features_name = ['homepage_featured', 'emailer_for_promotion','op_area','cuisine','city_code','region_code','category']
  prediction = model.predict(features_value)
  output=prediction[0]
  print(output)
  return render_template('upload.html', prediction_text=output)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8000, debug=False)
