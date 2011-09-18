#!/usr/bin/env python
from socket import *
from utils import proccess, human

host = 'localhost'
port = 50012

if __name__ == '__main__':

    buf = 1024

    addr = (host, port)

    clientsocket = socket(AF_INET, SOCK_STREAM)

    clientsocket.connect(addr)

    while 1:
        data = raw_input(">> ")
        if not data:
            break
        else:
            clientsocket.send(data)
            data = clientsocket.recv(buf)
            if not data:
                break
            else:
                print data
    clientsocket.close()

