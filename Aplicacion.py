import pandas as pd
import streamlit as st
import numpy as np
filename = "cat.png"
img = cv2.imread(filename, 1)
image = np.array([img])

original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.image(image, channels="BGR")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.image(image, channels="BGR")
st.title("Óptica Cuántica")
