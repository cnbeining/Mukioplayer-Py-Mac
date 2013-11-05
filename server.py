# coding=utf-8
'''
Mukioplayer_Py_Mac 2.000.05
Based on Mukioplayer
MIT licence
Beining@ACICFG
cnbeining[at]gmail.com
'''
import thread
import os
import getpass
import sys
import webbrowser
from multiprocessing import Process
import urllib
import threading
import shutil


reload(sys)
sys.setdefaultencoding('utf-8')


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
    os.system('rm -rf ./mukiocache')
    os.system('mkdir mukiocache')
    os.system('ln -s '+ real_cache_dir+' ./mukiocache ')
    os.system('cp /'+ video_relpath+'  '+ real_cache_dir)
    os.system('cp /'+ danmu_relpath+'  '+ real_cache_dir)
    os.system('mv '+real_cache_dir+'/'+danmu_filename +' '+real_cache_dir+'/danmu.xml')
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
    <load>http://localhost:8765/mukiocache/mukioplayer_py/danmu.xml</load>
    <send></send>
    <gateway></gateway>
  </server>
</conf>
    '''
    xml_to_write = xml_to_write.encode("utf8")
    os.chdir(py_path)
    f = open('./conf.xml', "w")
    f.write(xml_to_write)
    f.close()
    video_filename = video_filename.replace('\\', '')
    video_filename_url = ''
    video_filename_url = urllib.quote(video_filename)
    webpage_to_write = '''<html>

<head>
<title>'''+ video_filename + '''- Mukioplayer-Py-Mac</title>
</head>

<body>
<embed id="MukioPlayer"
src="http://localhost:8765/mukioplayerplus.swf?file=http://localhost:8765/mukiocache/mukioplayer_py/'''+video_filename_url+'''&type=video&sort=new"
width="98%" height="98%" type="application/x-shockwave-flash" allowscriptaccess="always" quality="high" allowfullscreen="true" />
</body>

</html>
'''
    #webpage_to_write = webpage_to_write.replace('\\', '').encode("utf8")
    webpage = open('./webpage.htm', "w")
    webpage.write(webpage_to_write)
    webpage.close()
    Process(target=http_server, ).start()
    os.chdir(py_path)
    os.system('cp webpage.htm  '  + real_cache_dir)
    os.system('cp favicon.ico  ' + real_cache_dir)
    webbrowser.open('http://localhost:8765/mukiocache/mukioplayer_py/webpage.htm')


v_relpath = str(input('Vid'))
#v_relpath = v_relpath.encode('utf-8')
X_relpath = str(input('XML'))
#X_relpath = X_relpath.encode('utf-8')

main(v_relpath, X_relpath)