import os
def run_room(clientsocket, instance):
    room = 'startroom'
    print instance.username, 'entered', room
    clientsocket.send('The rope sways, but you make it to the top\nviable command(s): look\n')
    x=1
    while x:
        cur_com = clientsocket.recv(1024)
        if cur_com == 'look':
            clientsocket.send('''You find yourself on a small dirt road.\nThere is a market in a small town square to the east.\nviable command(s): east\n''')
            break
        else:
            clientsocket.send('''I'm sorry, that is not a viable command\nviable command(s): east''')
        cur_com = clientsocket.recv(1024)
    if not instance.dirty:
        clientsocket.send('''You are in the town square.\nA kind looking man walks up to you and says:\n"You look like you have gone through hell; here, take my horse"\nThe man gives you a horse and walks off into the distance
You now own a horse.\nviable command(s): rest, look, west, east, south, north.\n''')
        instance.horse = 1
    if instance.dirty:
        clientsocket.send('''You are in the town square.\nAn angry man walks up to you and says\n"Stupid hobo, go die in a hole"\nThe man kicks you in the nuts before you can react, and storms off.
You now have 95% health.\nIf you get 0% health, you die.\nRest to get health back.\nviable command(s): rest, look, west, east, south, north.\n''')
        health = 95

    cur_com = clientsocket.recv(1024)
    if cur_com == 'rest':
        health = 100
        clientsocket.send('''You blink your eyes, and allow them to ajust to the light.\nYou notice that you have slept into the afternoon.\nViable command(s): look, west, east, south, north.\n''')
        cur_com = clientsocket.recv(1024)
    if cur_com == 'look':
        if room == 'startroom':
            clientsocket.send('''You can see a man walking off into the distance.\nTo the south you can see a theater.\nTo the north is a road made of stone.To the east, there is a castle with a man in a pointy hat on top of it.
To the west, darkness has fallen.\n''')


    if cur_com == 'north':
        clientsocket.send('You walk North')
        return 'North.North1'
    if cur_com == 'south':
        clientsocket.send('You walk South')
        return 'South.South1'
    if cur_com == 'east':
        clientsocket.send('You walk East\nViable command(s): look')
        return 'East.East1'
    if cur_com == 'west':
        clientsocket.send('You walk West')
        return 'West.West1'