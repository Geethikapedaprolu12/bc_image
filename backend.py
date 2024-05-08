from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['POST'])
def convert_image():
    try:
        file = request.files['file']
        image_bytes = file.read()
        
        # Convert image bytes to PIL Image object
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert the image to black and white
        bw_image = image.convert('L')
        
        # Save the black and white image to a BytesIO object
        output_buffer = io.BytesIO()
        bw_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)
        
        # Return the black and white image file
        return send_file(output_buffer, mimetype='image/png', as_attachment=True, download_name='converted_image.png')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
