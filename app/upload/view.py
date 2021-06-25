import os
from flask import request, jsonify, current_app

import cloudinary.uploader
import cloudinary
from cloudinary.utils import cloudinary_url

from . import upload_bp

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('CLOUD_API_KEY'),
    api_secret= os.getenv('CLOUD_API_SECRET')
)

@upload_bp.route('/upload', methods=['POST'])
def upload():
    current_app.logger.info('in Upload route')
    upload_result = None

    if request.method == 'POST':
        file_to_upload = request.files['file']
        
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(file_to_upload, folder='upload_flask')
            return jsonify(upload_result)

@upload_bp.route('/delete', methods=['POST'])
def delete():
    current_app.logger.info('in Delete route')
    if request.method == 'POST':
        public_id = request.form['public_id']

        if public_id:
            resp = cloudinary.uploader.destroy(public_id)
            return jsonify(resp)

@upload_bp.route('/cld_optimize', methods=['POST'])
def optimize():
    current_app.logger.info('in Optimize route')
    if request.method == 'POST':
        public_id = request.form['public_id']
        
        if public_id:
            cld_url = cloudinary_url(public_id, fetch_format='auto', quality='auto', secure=True)
            current_app.logger.info(cld_url)
            return jsonify(cld_url)