#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            if line.decode('utf-8').split(' ')[-1] == 'SIP/2.0':
                if line.decode('utf-8').split(' ')[0] == 'INVITE':
                    self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n" +
                                     b"SIP/2.0 180 Ringing\r\n\r\n" +
                                     b"SIP/2.0 200 OK\r\n\r\n")
                elif line.decode('utf-8').split('0')[0] == 'ACK':
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                elif line.decode('utf-8').split(' ')[0] == 'BYE':
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                else:
                    self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")


            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    try:
        SERVER_IP = sys.argv[1]
        SERVER_PORT = int(sys.argv[2])
        AUDIO_FILE = open(sys.argv[3])
    except NameError:
        sys.exit('Usage: python3 server.py IP port audio_file')
    serv = socketserver.UDPServer((SERVER_IP, SERVER_PORT), EchoHandler)
    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('Server ended.')
