# -*- coding: utf-8 -*-
'''
Este es el script principal, con un menú para elegir qué deseamos hacer.
'''

import os
import sys
import subprocess


def enunciado():
    print("\nIntroduce un número para realizar una de las siguientes operaciones:")
    print("\n[1]: Obtener el vídeo BBB con distintos formatos")
    print("\n[2]: Agrupar todos los videos obtenidos en [1] en un único container")
    print("\n[3]: Hacer un streaming del vídeo obtenido en [2]")
    print("\n[0]: Exit")
    x = input()
    return x


while (True):
    x = enunciado()

    if x == "1":
        os.system("python3 ex1.py")
    elif x == "2":
        os.system("python3 ex2.py")
    elif x == "3":
        print("Streaming link: udp://@224.2.2.2:2222")
        os.system("python3 ex3.py")
    elif x == "0":
        sys.exit()
    else:
        print('Introducir opción válida')
