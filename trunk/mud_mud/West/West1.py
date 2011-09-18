def run_room(username, clientsocket, dirty, horse):
    room = 'west1'
    print username, ' entered ', room
    clientsocket.send('''You walk West.
Suddenly you find yourself falling into a pit full of bloodythirsty gummy bears.
You find that they have all jumped into your bag in their quest to
devour your food.
You gain five gummy bears!
viable command(s): eat bears''')
    cur_com = clientsocket.recv(1024)
    