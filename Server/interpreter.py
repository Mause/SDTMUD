"""This program is an attempt to write a simple interpreter for a python based
mud system to assist creation of alternate flavours of MUD's"""

import os

class Room():
    def __init__(self):
        self.intro = ''
        self.options = {'north': {'north_room': '', 'north_info': ''},
                   'south': {'south_room': '', 'south_info': ''},
                   'east': {'east_room': '',  'east_info': ''},
                   'west': {'west_room': '', 'west_info': ''}}

def interpret_room(room_name):
    "Interpretes the selected room"
    fh = open(os.getcwd()+"\\scripted\\"+room_name)
    cur_room = Room()
    lines = fh.readlines()
    for line in lines:
        if line.split()[0] == 'intro':
            cur_room.intro = ' '.join(line.split()[1:])
        if line.split()[0] == 'options':
            if 'north' not in line.split()[1:]:
                cur_room.options['north'] = ''
            if 'south' not in line.split()[1:]:
                cur_room.options['south'] = ''
            if 'east' not in line.split()[1:]:
                cur_room.options['east'] = ''
            if 'west' not in line.split()[1:]:
                cur_room.options['west'] = ''
        for direction in cur_room.options:
            if line.split()[0] == str(direction)+'_room':
                cur_room.options[str(direction)][str(direction)+'_room'] = line.split()[1:]
            if line.split()[0] == str(direction)+'_info':
                cur_room.options[str(direction)][str(direction)+'_info'] = line.split()[1:]           
    return cur_room


if __name__ == '__main__':
    returned = interpret_room('begin.room')
    print '\nDone\n'
    print returned.intro
    print
    print returned.options

