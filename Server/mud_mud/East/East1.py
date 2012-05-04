def run_room(clientsocket, instance):
    clientsocket.send('''You are standing on a crossroads, whether or not you continue to live depends on a desition made here!
Viable commands: north, south\n
                      ''')
    cur_com = clientsocket.recv(1024)
    #if 
    return 'Misc.endroom'