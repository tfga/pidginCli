# encoding: utf-8

import sys
from PidginCli.send import send
from PidginCli.ArgParser import getOpts



def readFromStdin():
    
    msg = sys.stdin.read()
    msg = msg.rstrip() # Tirando o '\n'
    
    return msg


def main(argv):
    
    opts = getOpts(argv)
    
    users = opts['<buddy>']
    
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
