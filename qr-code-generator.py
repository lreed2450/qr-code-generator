#load libraries

import pyqrcode
import streamlit as st

st.header(body='QR Code Generator', divider='blue')

st.write("Paste your url in the below textbox to generator the QR code")

st_url = st.text_input(label='paste a url into the text box', placeholder='https://www.my-sample-url.com')

url_gen = pyqrcode.create(st_url)

st.write("the image is below.")

# url = pyqrcode.create(url_gen) 

# url.svg('test_qr.svg', scale=4, background="white", module_color="#7D007D")

# st.image('test_qr.svg')