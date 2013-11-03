import random
import thread
import os
import getpass
import sys
import webbrowser
from multiprocessing import Process
import threading



def http_server():
    user = getpass.getuser()
    user_dir = '/Users/' + user
    os.chdir(user_dir)
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    class ThreadingServer(ThreadingMixIn,HTTPServer):
        pass
    serveraddr=('', 8765)   # http://yige.org
    srvr=ThreadingServer(serveraddr,SimpleHTTPRequestHandler)
    srvr.serve_forever()
    #pass





def getrelpath(input_file):
    user = getpass.getuser()
    user_dir = '/Users/' + user
    os.chdir(user_dir)
    file_relpath = os.path.relpath(input_file)
    return file_relpath


def main(video_relpath, danmu_relpath):
    danmu_relpath = getrelpath(danmu_relpath)
    video_relpath = getrelpath(video_relpath)
    py_path = sys.path[0]
    real_path = getrelpath(py_path)
    os.chdir(py_path)

    xml_to_write = '''<?xml version="1.0" encoding="utf-8"?>
<conf>
  <performance>
    <maxwidth>2048</maxwidth>
    <maxheight>768</maxheight>
    <maxonstage>120</maxonstage>
    <maxwitheffect>80</maxwitheffect>
  </performance>
  <server>
    <onhost>yes</onhost>
    <load>http://localhost:8765/'''+danmu_relpath+'''</load>
    <send></send>
    <gateway></gateway>
  </server>
</conf>
    '''
    xml_to_write = xml_to_write.encode("utf-8")

    f = open('./conf.xml', "w")

    f.write(xml_to_write)
    f.close()
    Process(target=http_server, ).start()
    webbrowser.open('http://localhost:8765/'+real_path+ '/mukioplayerplus.swf?file=http://localhost:8765/' + video_relpath+'&type=video&sort=new')


v_relpath = str(input('Vid'))
X_relpath = str(input('XML'))

main(v_relpath, X_relpath)