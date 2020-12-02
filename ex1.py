# -*- coding: utf-8 -*-
'''
Aplicamos distintos formatos al vídeo BBB1.mp4
Ref:
    https://superuser.com/questions/785528/how-to-generate-an-mp4-with-h-265-codec-using-ffmpeg
'''

import subprocess


subprocess.call('ffmpeg -i BBB1.mp4 -vf scale=1280:-1 -c:v vp8 BBB1_720p.mkv', shell=True)  # container mp4 no es compatible con vp8
subprocess.call('ffmpeg -i BBB1.mp4 -vf scale=720:480 -c:v vp9 BBB1_480p.mp4', shell=True)
subprocess.call('ffmpeg -i BBB1.mp4 -vf scale=360:240 -c:v libx265 BBB1_360x240.mp4', shell=True)
subprocess.call('ffmpeg -i BBB1.mp4 -vf scale=160:120 -c:v libaom-av1 BBB1_160x120.mp4', shell=True)

# Forzar resolucion de salida:
# ffmpeg -i $INPUT -s 720x480 $OUTPUT
