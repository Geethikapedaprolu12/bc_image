import streamlit as st
import requests
from PIL import Image
import io

# Frontend HTML
st.title("Color to Black & White Image Converter")

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
        response = requests.post('http://localhost:8000', files={'file': buffer.getvalue()})
        
        if response.status_code == 200:
            # Display success message
            st.success("Image converted successfully!")

            # Display download link for converted image
            st.markdown(get_binary_file_downloader_html(response.content, 'Converted Image'), unsafe_allow_html=True)
        else:
            st.error("Error converting image. Please try again.")
            st.text(response.text)  # Print the error response
    except requests.exceptions.ConnectionError as e:
        st.error(f"Error: Unable to connect to the backend server. {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Download {file_label}</a>'
    return href
