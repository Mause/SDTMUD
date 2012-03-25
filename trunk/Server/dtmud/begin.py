import os
os.chdir(os.getcwd()+'\dtmud')
print os.getcwd()
import time
x = 1
room = 'begin'



def run_mud(clientsocket, instance):
        print 'DTMUD Started...'
        instance.username = clientsocket.recv(1024)
        clientsocket.send('Welcome, '+instance.username+'''\nA blast of light, and you black out...
You wake in a blast of blackness, knocking the dust around in a small room.
There is a large door as black as the abyss, that looks strangely familiar.
You find that you cannot remember anything about your past, and this causes you some distress.
You can either exit, or look around some more.\nviable command(s): look, exit\n''')
        while x:
            room = 'begin'
            instance.health = 100
            cur_com = clientsocket.recv(1024)
            if cur_com == 'exit':
                clientsocket.send('''The door creaks on its hinges\nviable command(s): look\n''')
                instance.dirty = 'false'
                return 'secondroom'
                    
            elif cur_com == 'look':
                if room == 'begin':
                    clientsocket.send('''There is a lot of dust, which is partly held up on spider webs\nAs your eyes trace the webs,\na small rock falls and breaks the webs above your head,
dumping dust all over the rags that cover your body\nYou struggle out of the door\nviable command(s): look\n''')
                    instance.dirty = 'true'
                    return 'secondroom'
            else:
                clientsocket.send('''Invalid Command;\nPlease try again\n''')
            
