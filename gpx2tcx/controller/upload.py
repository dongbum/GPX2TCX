from flask import render_template, request
from werkzeug.utils import secure_filename
from gpx2tcx.blueprint import gpx2tcx

@gpx2tcx.route('/upload')
def upload():
    return render_template('upload.html')

@gpx2tcx.route('/upload_process', methods=['POST'])
def upload_process():
    if request.method == 'POST':
        f = request.files['gpxfile']
        f.save('D:/Work/gpx2tcx.git/uploaded/' + secure_filename(f.filename))

    return '파일 업로드 성공'