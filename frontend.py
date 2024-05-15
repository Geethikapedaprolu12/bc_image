import streamlit as st
import requests
from PIL import Image
import io

st.title("Color to Black and White Image Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    if st.button('Convert to Black and White'):
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        files = {'file': img_byte_arr}
        response = requests.post("https://bc-image-2.onrender.com/convert", files=files)
        
        if response.status_code == 200:
            bw_img = Image.open(io.BytesIO(response.content))
            st.image(bw_img, caption='Black and White Image.', use_column_width=True)
            btn = st.download_button(label="Download Image", data=response.content, file_name='bw_image.png', mime='image/png')
        else:
            st.error(response.json().get('error'))
