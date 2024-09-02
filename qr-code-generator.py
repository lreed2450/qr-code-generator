#load libraries

import pyqrcode
import streamlit as st

st.header(body='QR Code Generator', divider='blue')

st.write("Paste your url in the below textbox to generator the QR code")

url = st.text_input(label='paste a url into the text box', placeholder='https://www.my-sample-url.com')

url_gen = pyqrcode.create(url)

st.write("the image is below.")


# st.image('uca.svg')