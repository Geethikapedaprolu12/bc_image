from flask import Flask, request, send_file, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    try:
        img = Image.open(file)
        if img.mode != 'RGB':
            return jsonify({'error': 'Please choose a color image'}), 400
        bw_img = img.convert('L')
        img_byte_arr = io.BytesIO()
        bw_img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, download_name='bw_image.png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
