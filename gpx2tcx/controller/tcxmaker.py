from xml.dom.minidom import Document

class TCXMaker(object):

    tcx_xmldoc = Document()
    tcx_root_node = None
    course_node = None
    track_node = None

    def __init__(self):
        # 루트 노드를 만들고 설정을 한다.
        tcx_node = self.tcx_xmldoc.createElement('TrainingCenterDatabase')
        tcx_node.setAttribute('xmlns', 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2')
        tcx_node.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        tcx_node.setAttribute('xsi:schemaLocation', 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd')
        self.tcx_xmldoc.appendChild(tcx_node)
        self.tcx_root_node = tcx_node

        # Courses 노드를 만들어서 추가
        courses_node = self.tcx_xmldoc.createElement('Courses')
        tcx_node.appendChild(courses_node)

        # Course 노드를 만들어서 추가
        course_node = self.tcx_xmldoc.createElement('Course')
        courses_node.appendChild(course_node)
        self.course_node = course_node

        # Track 노드를 만들어서 추가
        track_node = self.tcx_xmldoc.createElement('Track')
        course_node.appendChild(track_node)
        self.track_node = track_node

    def add_name(self, name):
        folder_node = self.tcx_xmldoc.createElement('Folders')
        self.tcx_root_node.appendChild(folder_node)

        courses_node = self.tcx_xmldoc.createElement('Courses')
        folder_node.appendChild(courses_node)

        course_folder_node = self.tcx_xmldoc.createElement('CourseFolder')
        course_folder_node.setAttribute('Name', name)
        courses_node.appendChild(course_folder_node)

        course_name_ref_node = self.tcx_xmldoc.createElement('CourseNameRef')
        course_folder_node.appendChild(course_name_ref_node)

        id_node = self.tcx_xmldoc.createElement('Id')
        course_name_ref_node.appendChild(id_node)

        id_text_node = self.tcx_xmldoc.createTextNode(name)
        id_node.appendChild(id_text_node)

    def add_trackpoint(self, lat, lon, ele):
        # Trackpoint 노드를 만들어서 추가

        trackpoint_node = self.tcx_xmldoc.createElement('TrackPoint')
        self.track_node.appendChild(trackpoint_node)

        # Time 노드를 만들어서 추가
        time_node = self.tcx_xmldoc.createElement('Time')
        trackpoint_node.appendChild(time_node)

        # Time 값 입력
        time_text_node = self.tcx_xmldoc.createTextNode('2010-01-01T00:00:00Z')
        time_node.appendChild(time_text_node)

        # position 노드를 만들어서 추가
        position_node = self.tcx_xmldoc.createElement('Position')
        trackpoint_node.appendChild(position_node)

        # LatitudeDegrees 노드를 만들어서 추가
        lat_node = self.tcx_xmldoc.createElement('LatitudeDegrees')
        position_node.appendChild(lat_node)

        lat_text_node = self.tcx_xmldoc.createTextNode(lat)
        lat_node.appendChild(lat_text_node)

        # LongitudeDegrees 노드를 만들어서 추가
        lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        position_node.appendChild(lon_node)

        lon_text_node = self.tcx_xmldoc.createTextNode(lon)
        lon_node.appendChild(lon_text_node)

        # AltitudeMeters 노드를 만들어서 추가
        alt_node = self.tcx_xmldoc.createElement('AltitudeMeters')
        trackpoint_node.appendChild(alt_node)

        alt_text_node = self.tcx_xmldoc.createTextNode(ele)
        alt_node.appendChild(alt_text_node)

        # DistanceMeters 노드를 만들어서 추가
        dist_node = self.tcx_xmldoc.createElement('DistanceMeters')
        trackpoint_node.appendChild(dist_node)

    def add_coursepoint(self, lat, lon, wpt_name):
        coursepoint_node = self.tcx_xmldoc.createElement('CoursePoint')
        self.course_node.appendChild(coursepoint_node)

        wpt_name_node = self.tcx_xmldoc.createElement('Name')
        coursepoint_node.appendChild(wpt_name_node)

        wpt_name_text_node = self.tcx_xmldoc.createTextNode(wpt_name)
        wpt_name_node.appendChild(wpt_name_text_node)

        time_node = self.tcx_xmldoc.createElement('Time')
        coursepoint_node.appendChild(time_node)

        time_text_node = self.tcx_xmldoc.createTextNode('2010-01-01T01:26:32Z')
        time_node.appendChild(time_text_node)

        # position 노드를 만들어서 추가
        position_node = self.tcx_xmldoc.createElement('Position')
        coursepoint_node.appendChild(position_node)

        # LatitudeDegrees 노드를 만들어서 추가
        lat_node = self.tcx_xmldoc.createElement('LatitudeDegrees')
        position_node.appendChild(lat_node)

        lat_text_node = self.tcx_xmldoc.createTextNode(lat)
        lat_node.appendChild(lat_text_node)

        # LongitudeDegrees 노드를 만들어서 추가
        lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        position_node.appendChild(lon_node)

        lon_text_node = self.tcx_xmldoc.createTextNode(lon)
        lon_node.appendChild(lon_text_node)

        # position 노드를 만들어서 추가
        pointtype_node = self.tcx_xmldoc.createElement('PointType')
        coursepoint_node.appendChild(pointtype_node)

        pointtype_text_node = self.tcx_xmldoc.createTextNode('Generic')
        pointtype_node.appendChild(pointtype_text_node)

    def get_tcx(self):
        return self.tcx_xmldoc.toprettyxml(encoding='UTF-8')
