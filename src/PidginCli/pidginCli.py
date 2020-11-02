#!/usr/bin/python

from dbus import SessionBus, Interface


# Info taken from:
#    
#    http://www.mrgazz.com/computers/computers-mainmenu-138/howto/automate-instant-messages-with-pidgin-and-dbus
#

def getPurple():
    
    bus = SessionBus()
    #   purple = bus.get("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
    
    obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
    
    # Finally, we get the interface on that object that we are interested in:
    
    return Interface(obj, "im.pidgin.purple.PurpleInterface")


def getAccount(purple):
    
    # Find account
    accounts = purple.PurpleAccountsGetAllActive()
    lenAccounts = len(accounts)
    
    
    if lenAccounts == 0:
        
        raise Exception('No accounts found.')
    
    elif lenAccounts > 1:
        
        print('WARNING: More than one account found. Using the first one.')
        
        for a in accounts:
        
            print(a, purple.PurpleAccountGetUsername(a))
            
    
    return accounts[0]
    
    


# Globais
purple = getPurple()
account = getAccount(purple)
