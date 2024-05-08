import streamlit as st
import requests
from PIL import Image
import io
import base64

# Frontend HTML
st.title("Image Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to black and white
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    try:
        # Send image to backend for conversion
        response = requests.post('http://127.0.0.1:5000', files={'file': buffer.getvalue()})
        
        if response.status_code == 200:
            # Display success message
            st.success("Image converted successfully!")

            # Display download link for converted image
            bin_str = base64.b64encode(response.content).decode()
            href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="converted_image.png">Download converted image</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.error("Error converting image. Please try again.")
            st.text(response.text)  # Print the error response
    except requests.exceptions.ConnectionError as e:
        st.error(f"Error: Unable to connect to the backend server. {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
