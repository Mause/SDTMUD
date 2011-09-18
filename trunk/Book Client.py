from socket import *

HOST = 'mause'
PORT = 50012
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
print 'Send /shutdown to shutdown server'
print 'Please use /discon to exit'
while True:
    data = raw_input('>  ')
    if data == '/discon':
        tcpSerSock.close()
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()