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

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app(config_filepath='resource/config.cfg'):
    gpx2tcx_app = Flask(__name__)

    # 뷰 함수 모듈
    from gpx2tcx.controller import index
    from gpx2tcx.controller import upload

    # 블루프린트
    from gpx2tcx.blueprint import gpx2tcx
    gpx2tcx_app.register_blueprint(gpx2tcx)

    # 페이징 처리를 위한 템플릿 함수
    gpx2tcx_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return gpx2tcx_app