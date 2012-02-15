# This program is an attempt to write a simple interpreter for a python based
# mud system to assist creation of alternate flavours of MUD's


#from ConfigParser import RawConfigParser as Raw
#config = Raw()
#configfh = open(os.getcwd()+"\\begin.room")
#config.readfp(configfh)

import os

class Room():
    intro=''
    options={'north': {'north_room': '', 'north_info': ''},
             'south': {'south_room': '', 'south_info': ''},
             'east': {'east_room': '',  'east_info': ''},
             'west': {'west_room': '', 'west_info': ''}}

def compute_room(room_name):
    fh = open(os.getcwd()+"\\scripted\\"+room_name)
    cur_room=Room()
    options=cur_room.options
    for line in fh.readlines():
        print line
	if line.split()[0] == 'intro':
            cur_room.intro = ' '.join(line.split()[1:])
	if line.split()[0] == 'options':
	    if 'north' not in line.split()[1:]:
                options['north'] = None
	    if 'south' not in line.split()[1:]:
                options['south'] = None
            if 'east' not in line.split()[1:]:
                options['east'] = None
            if 'west' not in line.split()[1:]:
                options['west'] = None
        if line.split()[0] == 'north_room':
            print 'boring '+str(line.split()[1:][0])
            options['north']['north_room'] == 'boring '+str(line.split()[1:][0])
            print "why isn't it being set?"
        if line.split()[0] == 'north_info':
            options['north']['north_info'] == line.split()[1:]

	
		#	cur_room.options[option]
		#	cur_room.intro = ' '.join(line.split()[1:])
    print options
    cur_room.options = options
    return cur_room


if __name__ == '__main__':
    returned = compute_room('begin.room')
    print '\nComputed\n'
    print returned.intro
    for x in returned.options:#['north']#['north_room']
        print x
        print returned.options[x]
	

