# encoding: utf-8

from PidginCli.Util import containsInsensitive
from PidginCli.pidginCli import purple, account


def extractLogin(accountName):
    
    atIndex = accountName.find('@')
    
    return accountName[:atIndex]
    
def getBuddyLogin(b):
    return extractLogin(getAccountName(b))
    
def getAccountName(b):
    return purple.PurpleBuddyGetName(b)

def getFullName(b):
    return purple.PurpleBuddyGetAlias(b)

def getAllBuddies():
    return purple.PurpleFindBuddies(account, '')
    
def getBuddy(name):
    'name - part of login or full name'
    
    buddies = getAllBuddies()
    
    return [b for b in buddies if containsInsensitive(getBuddyLogin(b), name)
                               or containsInsensitive(getFullName(b),   name)]


def getBuddyCompletions(pattern):
    'pattern - part of login or full name'
    
    buddies = getBuddy(pattern)
    
    return [str(getAccountName(b)) for b in buddies]
