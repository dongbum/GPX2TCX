from flask import render_template
from gpx2tcx.blueprint import gpx2tcx

@gpx2tcx.route('/upload')
def upload_gpx2tcx_form():
    return render_template('upload.html')

@gpx2tcx.route('/upload', methods=['POST'])
def upload_gpx2tcx():
    return render_template('upload.html')