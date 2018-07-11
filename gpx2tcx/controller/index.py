from flask import render_template
from gpx2tcx.blueprint import gpx2tcx

@gpx2tcx.route('/')
def index():
    return render_template('index.html')