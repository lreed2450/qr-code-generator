#load libraries

import pyqrcode
import streamlit as st

st.header(body='QR Code Generator', divider='blue')

st.write("Paste your url in the below textbox to generator the QR code")

url = st.text_input(lable='paste a url into the text box', placeholder='https://www.my-sample-url.com')


st.write("the image is below.")


st.image('uca.svg')