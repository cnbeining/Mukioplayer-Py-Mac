import random
import thread
import os
import getpass
import sys
import webbrowser
from multiprocessing import Process
import threading
import shutil


def http_server():
    py_path = sys.path[0]
    real_path = getrelpath(py_path)
    os.chdir(py_path)
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    class ThreadingServer(ThreadingMixIn,HTTPServer):
        pass
    serveraddr=('', 8765)   # http://yige.org
    srvr=ThreadingServer(serveraddr,SimpleHTTPRequestHandler)
    srvr.serve_forever()





def getrelpath(input_file):
    user = getpass.getuser()
    user_dir = '/Users/' + user
    os.chdir(user_dir)
    file_relpath = os.path.relpath(input_file)
    return file_relpath


def main(video_relpath, danmu_relpath):
    #danmu_relpath = getrelpath(danmu_relpath)
    #video_relpath = getrelpath(video_relpath)
    video_filename = video_relpath.split("/")[-1]
    danmu_filename = danmu_relpath.split("/")[-1]
    py_path = sys.path[0]
    os.chdir(py_path)
    user = getpass.getuser()
    user_dir = '/Users/' + user
    print(user_dir)
    real_cache_dir = user_dir + '/.cache/mukioplayer_py'
    os.system('rm -rf /'+real_cache_dir)
    os.system('mkdir /'+real_cache_dir)
    os.chdir(py_path)
    os.system('ln -s '+ real_cache_dir+' ./mukiocache ')
    os.system('cp /'+ video_relpath+'  '+ real_cache_dir)
    os.system('cp /'+ danmu_relpath+'  '+ real_cache_dir)
    print(danmu_filename)
    print(danmu_filename)
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
    <load>http://localhost:8765/mukiocache/mukioplayer_py/'''+ danmu_filename+'''</load>
    <send></send>
    <gateway></gateway>
  </server>
</conf>
    '''
    xml_to_write = xml_to_write.encode("utf-8")
    os.chdir(py_path)
    f = open('./conf.xml', "w")

    f.write(xml_to_write)
    f.close()
    Process(target=http_server, ).start()
    webbrowser.open('http://localhost:8765/mukioplayerplus.swf?file=http://localhost:8765/mukiocache/mukioplayer_py/' + video_filename+'&type=video&sort=new')


v_relpath = str(input('Vid'))
X_relpath = str(input('XML'))

main(v_relpath, X_relpath)