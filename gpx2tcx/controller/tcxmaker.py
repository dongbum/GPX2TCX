from xml.dom.minidom import Document

class TCXMaker(object):

    tcx_xmldoc = Document()

    def __init__(self):
        # 루트 노드를 만들고 설정을 한다.
        gpx_node = self.tcx_xmldoc.createElement('gpx')
        gpx_node.setAttribute('xmlns', 'http://www.topografix.com/GPX/1/1')
        gpx_node.setAttribute('creator', 'MapSource 6.16.2')
        gpx_node.setAttribute('version', '1.1')
        gpx_node.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        gpx_node.setAttribute('xsi:schemaLocation', 'http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd')
        self.tcx_xmldoc.appendChild(gpx_node)

        # Courses 노드를 만들어서 추가
        courses_node = self.tcx_xmldoc.createElement('Courses')
        gpx_node.appendChild(courses_node)

        # Course 노드를 만들어서 추가
        course_node = self.tcx_xmldoc.createElement('Course')
        courses_node.appendChild(course_node)

        # Track 노드를 만들어서 추가
        track_node = self.tcx_xmldoc.createElement('Track')
        course_node.appendChild(track_node)

        # Trackpoint 노드를 만들어서 추가
        # 루프 시작
        trackpoint_node = self.tcx_xmldoc.createElement('TrackPoint')
        track_node.appendChild(trackpoint_node)

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

        # LongitudeDegrees 노드를 만들어서 추가
        lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        position_node.appendChild(lon_node)

        # AltitudeMeters 노드를 만들어서 추가
        alt_node = self.tcx_xmldoc.createElement('AltitudeMeters')
        trackpoint_node.appendChild(alt_node)

        # DistanceMeters 노드를 만들어서 추가
        dist_node = self.tcx_xmldoc.createElement('DistanceMeters')
        trackpoint_node.appendChild(dist_node)

        # 루프 종료

    def GetTCX(self):
        return self.tcx_xmldoc.toprettyxml()
