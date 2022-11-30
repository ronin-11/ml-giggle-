##OBJECT DETECTION WEB APP

       ##MADE BY  ABEL TINOTENDA TEMBO..................R204434C
       ##         MALCOM JAYAGURU ......................R204431Y 


import streamlit as st
from charset_normalizer import detect
from numpy import object_
import shutil
import cv2
import os
from PIL import Image
import numpy as np
from mailbox import ExternalClashError
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import io
from keras.applications.vgg16 import VGG16
# load the model
model = VGG16()

from keras.preprocessing.image import load_img
# load an image from file
from keras.preprocessing.image import img_to_array
# convert the image pixels to a numpy array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions

## Function to detect object


def classifyObjects():
    #generate_frames()
    model = VGG16()
    classifications = []
    frames = 'C:/Users/USER/PycharmProjects/GeneralManager/frames'
    for i in range(len(frames)):
        img = load_img(frames[i], target_size=(224, 224))  # load an image from file
        img = img_to_array(img)  # convert the image pixels to a numpy array
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        img = preprocess_input(img)  # prepare the image for the VGG model
        img_pred = model.predict(img)
        label = decode_predictions(img_pred)
        label = label[0][0]
        result = label[1]
        classifications.append(result)
    return classifications, frames

## Function to save the uploaded file
def save_uploadedfile(uploaded_file):
    with open(os.path.join("uploadedVideos", uploaded_file.name), "wb") as f:
      f.write(uploaded_file.getbuffer())
      global filename
      filename = uploaded_file.name
      st.success("Saved File:{} to tempDir".format(uploaded_file.name))
      return filename
## Function to split video into frames
def generate_frames(video):
  vidcap = cv2.VideoCapture(video)
  success, image = vidcap.read()
  count = 0

  while success:
    cv2.imwrite("frames/frame%d.jpg" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count = 0
    st.success("Successfully split the video into frames")
  return
def searchObject(searchItem, classes, frames):
    if searchItem in classes:
        index = classes.index(searchItem)
        img = frames[index]
        img = Image.open(img)
        st.image(img, caption=searchItem)
    else:
        st.write("object not found")
def main():
    """ """

   

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:white ;padding:10px">
    <h2 style="color:blue;text-align:center;">Object Detecting WebApp</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.title("Detect and classify ")
    uploaded_file = st.file_uploader("Choose a video...of not more than 2MB", type=["mp4"])
    temporary_location = False
    if uploaded_file is not None:
        filename = 'uploadedVideos/' + str(save_uploadedfile(uploaded_file))
        ## Split video into frames
        generate_frames(filename)
        ## Detect objects in frames
        #detect_Object()
    search_item = st.text_input('search object')
    if st.button("Search"):
        classifyObjects()
        #detect_Object()




if __name__ == '__main__':
    main()
