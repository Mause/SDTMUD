import os
print os.getcwd()

from mud.user_utils import get_users
 

for chunk in get_users('/mud/users/'):
    #print 'The users name is '+get_users('/mud/users/')[chunk]['type']+' and their type is '+chunk['type']
    print get_users('/mud/users/')[chunk]
wait= raw_input()

