import ConfigParser, os

userconfig = ConfigParser.RawConfigParser()
userconfigfh = open(os.getcwd()+"\mud\userlist.txt")
userconfig.readfp(userconfigfh)
userconfigfh.close()

cur_user_config = ConfigParser.RawConfigParser()

def get_users(dir):
    users = dict()
    for x in range(len(userconfig.get('userlist', 'list'))):
        cur_user = open(os.getcwd()+dir+"user_"+str(x+1)+".txt")
        userconfig.readfp(cur_user)
        cur_user.close()
        users.update({userconfig.get('user', 'name'):{'name':userconfig.get('user', 'name'), 'type':str(userconfig.get('user', 'type'))}})
        #foo = {'bar': 'baz'}
        #foo.update({'quux': 'blah'})
    #return foo
    return users
