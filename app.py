from skimage import io
import streamlit as st 
import numpy as np
import cv2
import matplotlib.pyplot as plt
# from google.colab.patches import cv2_imshow
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import scipy
from scipy import stats


from keras.models import load_model
modeln = load_model('name.h5')
NAME_CLASSES = ['Abhay','Amitabh','Hemang','Jinesh','Kalpana','Manish','Neeta','Niket','Sudhanshu','Tanmay']


# Loading saved model from Drive.
from keras.models import load_model
modelv = load_model('verify.h5')
VERIFY_CLASSES = ['Forged', 'Real']
html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima University  </p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;"> Signature Detection  from Document </p></center> 
   </div>
   </div>
   </div>
   """

st.markdown(html_temp,unsafe_allow_html=True)
st.title("""
        Signature Recognition, Varification & Validation
         """
         )
file= st.file_uploader("Please upload signature here ", type=("jpeg"))

import cv2
from  PIL import Image, ImageOps
def import_and_predict_n(image_data):
  #x = cv2.resize(image_data, (48, 48)) 
  #img = image.load_img(image_data, target_size=(48, 48))
  #x = image.img_to_array(img)
  size=(224, 224)
  #image=ImageOps.fit(image_data, size, Image.ANTIALIAS)
  img=np.asarray(resized)
  img_reshape=np.expand_dims(img, axis=1)
  img_reshape=img[np.newaxis,...]
  features = modeln.predict(img_reshape)
  print(features)
  label_index=features.argmax()
  print(label_index)
  print("Model prediction :", NAME_CLASSES[label_index])  
  return NAME_CLASSES[label_index]


if file is None:
  st.text("Please upload an Image file")
else:
  image = io.imread(file)
  #image=Image.open(file)
  #image=np.array(image)
  #file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  #image = cv2.imdecode(file_bytes, 1)
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  lower = np.array([90, 38, 0])
  upper = np.array([300, 255, 255])
  mask = cv2.inRange(hsv, lower, upper)
  result = cv2.bitwise_and(image, image, mask=mask)
  result[mask==0] = (255, 255, 255)

  # Find contours on extracted mask, combine boxes, and extract ROI
  cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  cnts = np.concatenate(cnts)
  x,y,w,h = cv2.boundingRect(cnts)
  cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
  ROI = result[y:y+h, x:x+w]
  resized = cv2.resize(ROI, (224, 224))


  st.image(image,caption='Uploaded Cheque', use_container_width=True)
  st.image(ROI,caption='Extracted Signature', use_container_width=True)
    
if st.button("Reveal Name"):
  resultn=import_and_predict_n(resized)
  st.success('Model has predicted the Signature is of   {}'.format(resultn))

import cv2
from  PIL import Image, ImageOps
def import_and_predict_v(image_data):
  #x = cv2.resize(image_data, (48, 48)) 
  #img = image.load_img(image_data, target_size=(48, 48))
  #x = image.img_to_array(img)
  size=(224, 224)
  #image=ImageOps.fit(image_data, size, Image.ANTIALIAS)
  img=np.asarray(resized)
  img_reshape=np.expand_dims(img, axis=1)
  img_reshape=img[np.newaxis,...]
  features = modelv.predict(img_reshape)
  print(features)
  label_index=features.argmax()
  print(label_index)
  print("Model prediction :", VERIFY_CLASSES[label_index])
  
  return VERIFY_CLASSES[label_index]

if st.button("Validate Signarure"):
  resultv=import_and_predict_v(image)
  st.success('Model has predicted the Signarure is   {}'.format(resultv))
if st.button("About"):
  st.header(" Deepak Moud")
  st.subheader("Research scholar: 2018PUSCEPHDE07061")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Research under Guidance</p></center> 
   <center><p style="font-size:20px;color:white;margin-top:10px;">Dr. Rakesh Kumar Saxena, Professor, Poornima University</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
