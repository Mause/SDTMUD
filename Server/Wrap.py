#! /bin/python
"""
This program is the base server for a test mud server :)
"""


from socket import *
import thread
import os
from utils import proccess, human
import time
import logging
import platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

LOG = logging.getLogger("DTMUDS")
HDLR = logging.FileHandler('../server.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
HDLR.setFormatter(formatter)
LOG.addHandler(HDLR)
LOG.setLevel(logging.DEBUG)
#set verbosity to show all messages of severity >= DEBUG

##########################
ADMIN_PASS = 'manam'
##########################

host = 'localhost'
port = 50012


os.system('title DTMUD Server')


def debug(data):
    "a utility function for easier debug logging"
    data = str(data)
    LOG.debug(data)


def info(data):
    "a utility function for easier info logging"
    data = str(data)
    LOG.info(data)
    print '[' + str(time.ctime()) + '] ' + data


def handler(clientsocket, clientaddr):
    "base level server code"
    instance = human()
    instance.time = time.time()
    info('Accepted connection from: ' + str(clientaddr))
    data = ''
    while data != 'user' and data != 'admin':
        data = clientsocket.recv(1024)
        if data == 'user':
            info('non-admin user detected')
            clientsocket.send('non-admin user detected')
            while 1:
                data = clientsocket.recv(1024)
                if data:
                    print '[' + str(time.ctime()) + '] Recieved: %s' % data
                    status = proccess(data, clientsocket, instance)
                    try:
                        if status == 'exit':
                            break
                    except AttributeError:
                        pass
            clientsocket.close()
            break
        elif data == 'admin':
            clientsocket.send('Admin user detected!')
            console(clientsocket)
        else:
            clientsocket.send('''incorrect response
Please enter either "user" or "admin" for the appropriate mode!''')
            data = clientsocket.recv(1024)
    debug('''Well. Some bastard decided to kill me,
so goodbye cruel world''')


def console(clientsocket):
    """this is supposed to an admin interface to the server.
    no real purpose though"""
    info('Admin user detected!')
    clientsocket.send('Admin user detected!\nPlease enter password')
    cur_com = clientsocket.recv(1024)
    while cur_com != ADMIN_PASS:
        clientsocket.send('''Incorrect admin pass
Please enter /correct/ password''')
        cur_com = clientsocket.recv(1024)
    clientsocket.send('''Congratulations! Password was correct!
type "help" to receive help''')
    while 1:
        cur_com = clientsocket.recv(1024)
        if not cur_com:
            break
        else:
            info('Recieved: %s' % cur_com)
            if cur_com == 'help':
                msg = str('[' + str(time.ctime()) + '''] Alerting authorities!
Dialing 911, 121, 000 and every other emergency number known to man!
Please remain Calm!''')
            else:
                msg = str('[' + str(time.ctime()) + '''] damn.
this feature is not yet up to scratch
IE, it is useless as of yet.''')
            clientsocket.send(msg)
    clientsocket.close()


if __name__ == "__main__":

    buf = 1024

    addr = (host, port)

    serversocket = socket(AF_INET, SOCK_STREAM)

    serversocket.bind(addr)

    serversocket.listen(2)

    while 1:
        info('Server is listening for connections\n')

        try:
            clientsocket, clientaddr = serversocket.accept()
        except KeyboardInterrupt:
            break
            #log.close()
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    serversocket.close()
