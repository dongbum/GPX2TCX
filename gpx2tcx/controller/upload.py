from flask import render_template, request, current_app
from werkzeug.utils import secure_filename
from gpx2tcx.blueprint import gpx2tcx
from xml.dom import minidom
from xml.dom.minidom import Document
import os, uuid
from gpx2tcx.controller.tcxmaker import TCXMaker

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

            # 업로드 폴더 경로를 구한다.
            upload_folder = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])

            # 업로드 폴더가 없다면 새로 생성
            if False == os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            # 파일 업로드
            filename = secure_filename(upload_gpx.filename.rsplit('.', 1)[0] + '_' + str(uuid.uuid4()) + '.' + ext)
            upload_gpx.save(os.path.join(upload_folder, filename))

            gpx_xmldoc = minidom.parse(os.path.join(upload_folder, filename))
            gpx_xmldoc = gpx_xmldoc.firstChild

            # print('---------------------------------------------------------------------')
            # print(gpx_xmldoc.toxml())

            #
            # 여기서부터 tcx 파일 생성 시작
            #

            tcx_maker = TCXMaker()


            metadata_items = gpx_xmldoc.getElementsByTagName('metadata')
            for metadata_item in metadata_items:
                print('---------------------------------------------------------------------')
                print(metadata_item.toxml())

            wpt_items = gpx_xmldoc.getElementsByTagName('wpt')
            for wpt_item in wpt_items:
                wpt_name = wpt_item.getElementsByTagName('name')
                tcx_maker.add_coursepoint(wpt_item.getAttribute('lat'), wpt_item.getAttribute('lon'), wpt_name[0].firstChild.data)

            trk_items = gpx_xmldoc.getElementsByTagName('trk')

            course_name = trk_items[0].getElementsByTagName('name')[0].firstChild.data
            tcx_maker.add_name(course_name)

            trkseg_items = trk_items[0].getElementsByTagName('trkseg')
            trkpt_items = trkseg_items[0].getElementsByTagName('trkpt')

            for trkpt_item in trkpt_items:
                ele = trkpt_item.getElementsByTagName('ele')
                tcx_maker.add_trackpoint(trkpt_item.getAttribute('lat'), trkpt_item.getAttribute('lon'), ele[0].firstChild.data)

        # return '파일 업로드 성공 : ' + os.path.join(upload_folder, filename)
        # return '파일 업로드 성공 : ' + os.path.join(upload_folder, filename) + '<br> + ' + tcx_xmldoc.toprettyxml(indent="  ")
        return tcx_maker.get_tcx()

    except Exception as e:
        raise e

    return '파일 업로드 실패'
