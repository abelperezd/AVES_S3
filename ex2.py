# -*- coding: utf-8 -*-

'''

'''


import subprocess
import os

nfiles = 4
channels = 2

# Nombre de cada uno de los archivos generados en el script 1
files = ["BBB1_720p.mkv", "BBB1_480p.mp4", "BBB1_360x240.mp4", "BBB1_160x120.mp4"]

string = "ffmpeg "

# Añadimos al string el nombre de todos los archivos
for i in files:
    string = string + "-i {} ".format(i)

string = string + "-c copy "

# Añadimos los canales para cada archivo
for i in range(nfiles):
    for j in range(channels):
        string = string + "-map {}:{} ".format(i, j)

# Añadimos el nombre final del container
string = str(string + "container.mkv")

subprocess.call(string, shell=True)
