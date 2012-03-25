#!/usr/bin/env python
from socket import *
import os

os.system('title DTMUD CLIent')

host = 'localhost'
port = 50012

print 'DTMUD CLIent\nIs set to connect to localhost:50012.\nEnter either "user" mode or "admin" mode to continue'

if __name__ == '__main__':
    buf = 1024
    addr = (host, port)
    clientsocket = socket(AF_INET, SOCK_STREAM)
    #try:
    if True:
        clientsocket.connect(addr)
    #except:# socket.error:
     #   print "Couldn't connect to the server;\nare you have the right address and that the server is running?"
    while 1:
        data = raw_input(">> ")
        if not data:
            clientsocket.send('')
            break
        else:
            clientsocket.send(data)
            data = clientsocket.recv(buf)
            if not data or data == '':
                clientsocket.send('')
                break
            else:
                print data
    print 'No \nDisconnecting from server..'
    clientsocket.close()

