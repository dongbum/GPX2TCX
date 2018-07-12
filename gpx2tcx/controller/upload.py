from flask import render_template, request, current_app
from werkzeug.utils import secure_filename
from gpx2tcx.blueprint import gpx2tcx
from xml.dom.minidom import *
import os, uuid

ALLOWED_EXTENSIONS = set(['gpx'])

def __allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@gpx2tcx.route('/upload')
def upload():
    return render_template('upload.html')

@gpx2tcx.route('/upload_process', methods=['POST'])
def upload_process():

    upload_gpx = request.files['gpxfile']

    try:
        if upload_gpx and __allowed_file(upload_gpx.filename):
            ext = upload_gpx.filename.rsplit('.', 1)[1]

            upload_folder = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])

            if False == os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            filename = secure_filename(upload_gpx.filename.rsplit('.', 1)[0] + '_' + str(uuid.uuid4()) + '.' + ext)
            upload_gpx.save(os.path.join(upload_folder, filename))

        return '파일 업로드 성공'

    except Exception as e:
        raise e

    return '파일 업로드 실패'
