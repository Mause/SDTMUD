from socket import *
import thread
import os
from utils import proccess, human


host = 'localhost'
port = 50012


os.system('title DTMUD Server')

def handler(clientsocket, clientaddr):
	instance = human()
	print "Accepted connection from: ", clientaddr
	data = clientsocket.recv(1024)
	if data != 'admin':
		print 'non-admin user detected'
		clientsocket.send('non-admin user detected')
		while 1:
			print 'welcome to the start of the end. and goodbye'
			data = clientsocket.recv(1024)
			if data:
				print 'Recieved: %s' % data
				status=proccess(data, clientsocket, instance)
				try:
					if status == 'quit':
						break
				except AttributeError:
					pass
		clientsocket.close()
	else:
		console(clientsocket)


def console(clientsocket):
	print 'admin user detected!'
	clientsocket.send('admin user detected!')
	while 1:
		data = clientsocket.recv(1024)
		if not data:
			break
		else:
			print 'Recived: %s' % data
			msg = str('this feature is not yet up to scratch')
			clientsocket.send(msg)
	clientsocket.close()



if __name__ == "__main__":

	buf = 1024

	addr = (host, port)

	serversocket = socket(AF_INET, SOCK_STREAM)

	serversocket.bind(addr)

	serversocket.listen(2)
	
	while 1:
		print "Server is listening for connections\n"

		clientsocket, clientaddr = serversocket.accept()
		thread.start_new_thread(handler, (clientsocket, clientaddr))
	serversocket.close()

