# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for

def print_settings(config):
    print('===================================================================')
    print('settings for gpx2tcx')
    print('===================================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('===================================================================')

def not_found(error):
    return render_template('404.html'), 404

def create_app(config_filepath='resource/config.cfg'):
    gpx2tcx_app = Flask(__name__)

    from gpx2tcx.blueprint import gpx2tcx
    gpx2tcx_app.register_blueprint(gpx2tcx)

    return gpx2tcx_app