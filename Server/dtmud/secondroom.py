def run_room(clientsocket, instance):
    room = 'secondroom'
    cur_com = clientsocket.recv(1024)
    print instance.username, 'entered', room
    clientsocket.send('''You have entered into a large underground cave,\n complete with bats and an underground stream.
You notice some rope on the ground\nViable commands: look rope\n''')
    cur_com = clientsocket.recv(1024)
    while 1:
        if cur_com == 'look rope':
            clientsocket.send('The passage appears to lead into a small opening in the cave roof\nClimb Rope? y/n\n')
            cur_com = clientsocket.recv(1024)
            if cur_com == 'y':
                return 'startroom'
        else:
            clientsocket.send('The ceiling falls down, and you die.\nWell, you felt dead, but you wake blinking your eyes, feeling very much alive\n"Wierd", you think\nViable command(s): look rope')
            
#additional