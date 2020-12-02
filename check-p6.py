#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script de comprobación de entrega de práctica

Para ejecutarlo, desde la shell:
 $ python3 check-p6.py login_laboratorio

"""

import os
import random
import sys


files = ['README.md',
         'LICENSE',
         '.gitignore',
         'client.py',
         'server.py',
         'simplertp.py',
         'bitstring.py',
         'invite.libpcap',
         'check-p6.py',
         '.git',
         'cancion.mp3']


if len(sys.argv) != 2:
    print()
    sys.exit("Usage: $ python3 check-p6.py login_gitlab")

repo_git = "http://gitlab.etsit.urjc.es/" + sys.argv[1] + "/ptavi-p6"

aleatorio = str(int(random.random() * 1000000))

error = 0

print
print("Clonando el repositorio " + repo_git)
print()
os.system('git clone ' + repo_git + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
try:
    student_file_list = os.listdir('/tmp/' + aleatorio)
except OSError:
    error = 1
    print("Error: No se ha podido acceder al repositorio " + repo_git + ".")
    print()
    sys.exit()

if len(student_file_list) != len(files):
    error = 1
    print("Error: solamente hay que subir al repositorio los ficheros indicados en las guion de practicas, que son en total " + str(len(files)) + " (incluyendo .git y .gitignore).")
    print("Has entregado " + str(len(student_file_list)) + " ficheros")

if set(files) != set(student_file_list):
    print()
    print("Algunos ficheros no se han entregado (o llamado) correctamente")
    demenos = set(files) - set(student_file_list)
    if demenos:
        print("Fichero(s) que falta(n) por entregar:", demenos)
    demas = set(student_file_list) - set(files)
    if demas:
        print("Fichero(s) entregado(s) de más:", demas)
    print()

if not error:
    print("Parece que la entrega se ha realizado bien.")
    print()
    print("La salida de pep8 es: (si todo va bien, no ha de mostrar nada)")
    print()
    os.system('pep8 --repeat --show-source --statistics /tmp/' + aleatorio + '/client.py /tmp/' + aleatorio + '/server.py')
print()
