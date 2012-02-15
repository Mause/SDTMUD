from socket import *
import thread
import os
from utils import proccess, human
import time

##########################
admin_pass = 'manam'
##########################


host = 'localhost'
port = 50012


os.system('title DTMUD Server')

def handler(clientsocket, clientaddr):
    instance = human()
    instance.time = time.time() 
    print '['str(time.ctime())+"] Accepted connection from: ", clientaddr
    data = ''
    while data != 'user' and data != 'admin':
        data = clientsocket.recv(1024)
        if data == 'user':
            print '['+str(time.ctime())+'] non-admin user detected'
            clientsocket.send('non-admin user detected')
            while 1:
                data = clientsocket.recv(1024)
                if data:
                    print '['str(time.ctime())+']Recieved: %s' % data
                    status=proccess(data, clientsocket, instance)
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
            clientsocket.send('incorrect response\nPlease enter either "user" or "admin" for the appropriate mode!')
            data = clientsocket.recv(1024)
    print '['+str(time.ctime())+'] Well. Some bastard decided to kill me, so goodbye cruel world'
        


def console(clientsocket):
    print '['+str(time.ctime())+'] Admin user detected!'
    clientsocket.send('Admin user detected!\nPlease enter password')
    cur_com = clientsocket.recv(1024)
    while cur_com != admin_pass:
        clientsocket.send('Incorrect admin pass\nPlease enter /correct/ password')
        cur_com = clientsocket.recv(1024)
    clientsocket.send('Congratulations! Password was correct!\ntype "help" to recieve help')
    while 1:
        cur_com = clientsocket.recv(1024)
        if not cur_com:
            break
        else:
            print '['+str(time.ctime())+'] Recieved: %s' % cur_com
            if cur_com == 'help':
                msg = str('['+str(time.ctime())+'] Alerting authorities!\nDialing 911, 121, 000 and every other emergency number known to man!\nPlease remain Calm!')
            else:
                msg = str('['+str(time.ctime())+'] this feature is not yet up to scratch\nIE, it is useless as of yet.')
            clientsocket.send(msg)
    clientsocket.close()



if __name__ == "__main__":

    buf = 1024

    addr = (host, port)

    serversocket = socket(AF_INET, SOCK_STREAM)

    serversocket.bind(addr)

    serversocket.listen(2)
    
    while 1:
        print '['str(time.ctime())+"] Server is listening for connections\n"

        clientsocket, clientaddr = serversocket.accept()
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    serversocket.close()

