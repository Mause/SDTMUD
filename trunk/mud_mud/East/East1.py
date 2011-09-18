def run_room(clientsocket, instance):
    clientsocket.send('You are standing on a crossroads, your life depends on this')
    return 'Misc.endroom'