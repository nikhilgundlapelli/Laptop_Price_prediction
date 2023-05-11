import streamlit as st
import os
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('Laptop.png')

st.image(image, caption='Welocome to the world of modern tech Products :sparkles:')

st.title('Laptop price prediction app')
st.snow()

st.write(''.join(['Customize your laptop as per your requirement , ',
                  'And predict the Fare Price of the laptop.']))
st.write('Tried of search different sources to predict the laptop price this app can get you all at one place:thumbsup:')
st.markdown('This is the project build at \N{winking face}')
st.caption('Innomatics Research Labs Internship - February 2023	:tada:')
