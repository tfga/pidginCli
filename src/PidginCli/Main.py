# encoding: utf-8

import sys
from PidginCli.send import send
from tfga.launchEditor import launchEditor
from PidginCli.ArgParser import getOpts
from PidginCli.conf import domain



def readFromStdin():
    
    msg = sys.stdin.read()
    msg = msg.rstrip() # Tirando o '\n'
    
    return msg



def addDomain(u):
    
    return '{}@{}'.format(u, domain)

def main(argv):
    
    opts = getOpts(argv)
    
    users = opts['<buddy>']
    users = [addDomain(u) for u in users]
    
    if not sys.stdin.isatty():
    
        msg = readFromStdin()
        
    else:
        
        msg = ''

    

    for user in users:
    
        send(msg, user)
    
    



def entryPoint():
    return main(sys.argv[1:])

if __name__ == '__main__':
    entryPoint()
