import string
import ConfigParser, os


config = ConfigParser.RawConfigParser()
configfh = open("mudlist.txt")
config.readfp(configfh)


def proccess(data, clientsocket, instance):
	print '''Beginning to proccess data with 'process("'''+str(data+'''", clientsocket, instance)' ''')
	if data != '':
		print 'Data was "iffed"'
		if (data.split()[0]) == 'help':
			print 'Quick! Someone needs help!'
			clientsocket.send('''Help Dox;
* "list": to have the server list the available mud server scripts.
* "load mud_name": to have the server load a listed mud server script.
* "exit": kills your personalised instance of the server.\n''')
							
		elif (data.split()[0]) == 'list':
			print 'Giving the menu to the user...'
			msg = ''
			for x in range((len(config.get('mudlist', 'list')))):
			   msg = msg + (config.get(('mud'+str(x)), 'name')+'\n')
			clientsocket.send(msg)
		
		elif (data.split()[0]) == 'load':
			if len(data.split()[1:]) == '' or len(data.split()) == 1:
				print 'The user forgot the mud...'
				clientsocket.send('Please specify a mud to load.\n')
			else:
				print 'Serving the dish to the user...'
				for x in range(len(config.get('mudlist', 'list'))):
					if (config.get(('mud'+str(x)), 'name')).lower() == (str(data.split()[1:][0])).lower():
						path_to_mud = config.get(('mud'+str(x)), 'dir')
						clientsocket.send('Completed loading of the MUD "'+str(data.split()[1:][0])+'''" ("'''+str(path_to_mud)+'''")
Please enter your desired username...''')
				# initiate mud code fron here on in!!!!!!!!!!!!!!!!!!!!

				for x in range(len(config.get('mudlist', 'list'))):
					if (config.get(('mud'+str(x)), 'dir')) == str(path_to_mud):
						run_script = config.get(('mud'+str(x)), 'run_script')
				print ('import '+path_to_mud[1:]+'.'+run_script+' as begin')
				exec('import '+path_to_mud[1:]+'.'+run_script+' as begin')
				run_loop(clientsocket, instance, path_to_mud, run_script)
				return 'exit'
				
		elif (data.split()[0]) == 'quit':
			print 'A user has quit...'
			return 'quit'
		else:
			clientsocket.send('Command not found\n')
	else:
		clientsocket.send('Please enter a command\n')

def run_loop(clientsocket, instance, path_to_mud, run_script):
	exec('import '+path_to_mud[1:]+'.'+run_script+' as begin')
	result = begin.run_mud(clientsocket, instance)
	print 'The beginning result was', result
	while result != '':
		if result == 'exit':
			return 'exit'
		else:
			print 'About to do these things:'
			print 'import '+str(path_to_mud[1:]+'.'+result+' as '+(result.split('.')[-1:][0]))
			print 'result = next_room.run_room(clientsocket, instance)'
			exec('import '+str(path_to_mud[1:]+'.'+result+' as next_room'))
			result = next_room.run_room(clientsocket, instance)
	clientsocket.send('MUD server script has exited. If you believe this is in error, please contact the admins.')


class human:        # Human template. saved to file on game exit
	username = ''   # Username. also the filename of the save file, however is appended with ".user"
	health = 100    # Exactly what it says, idiot
	stamina = 10    # Ditto
	max_stamina = 20# Maximum obtainable stamina
	dirty = False   # Whether or not you are dirty
	horse = False   # If you have a horse. Point unsure; does not enable faster traversing. May allow something similar to teleporting, but then i have to make a map :(
	inventory = {}  # Inventory
	time = 0        # starting time
