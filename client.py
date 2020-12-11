#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
try:
    METHOD = sys.argv[1]
    address = sys.argv[2]
except IndexError:
    print("Usage: python3 client.py method receiver@IP:SIPport")

SERVER_NAME = address.split('@')[0]
SERVER_IP = address.split('@')[1].split(':')[0]
SERVER_PORT = address.split('@')[1].split(':')[1]

# Contenido que vamos a enviar
if METHOD == 'INVITE':
    LINE = 'INVITE sip:' + SERVER_NAME + '@' + SERVER_IP + ' SIP/2.0\r\n'
elif METHOD == 'BYE':
    LINE = 'BYE sip:' + SERVER_NAME + '@' + SERVER_IP + ' SIP/2.0\r\n'

ACK_LINE = 'ACK sip:' + SERVER_NAME + '@' + SERVER_IP + ' SIP/2.0\r\n'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER_IP, SERVER_PORT))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido --\r\n', data.decode('utf-8'))
    if data.decode('utf-8').split(' ')[1] == '100':
        print("Enviando: " + ACK_LINE)
        my_socket.send(bytes(ACK_LINE, 'utf-8') + b'\r\n')

    print("Terminando socket...")

print("Fin.")
