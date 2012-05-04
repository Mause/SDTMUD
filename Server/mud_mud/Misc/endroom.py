def run_room(clientsocket, instance):
    clientsocket.send('''THIS. IS. ENDROOM!



For information purposes, this is also the end of the game...
Welcome back to the real world!
Hit enter to quit the client''')
    instance.health = 0
    return 'exit'
