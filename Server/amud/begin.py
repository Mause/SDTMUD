from mud_utils import alex_open
import time
x = 1
room = 'begin'

def run_mud(clientsocket):
        print 'DTMUD Started...'
        username = clientsocket.recv(1024)
        clientsocket.send('''Welcome\n''')
        while x:
            first = clientsocket.recv(1024)
            clientsocket.send('''There is a lot of dust, which is partly held up on spider webs\nAs your eyes trace the webs,\na small rock falls and breaks the webs above your head,
dumping dust all over the rags that cover your body\nYou struggle out of the door\nviable command(s): look\n''')

            
