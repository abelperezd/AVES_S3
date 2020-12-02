# -*- coding: utf-8 -*-
'''
Con este script realizamos un streaming del primer canal de vídeo y audio de container.mkv.
Ref:
    https://trac.ffmpeg.org/wiki/StreamingGuide
'''
import subprocess

# ip donde emitimos el vídeo: udp://@224.2.2.2:2222
string = 'ffmpeg -re -i container.mkv -f mpegts udp://@224.2.2.2:2222'
subprocess.call(string, shell=True)
