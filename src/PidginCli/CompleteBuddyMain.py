# encoding: utf-8

import sys
from PidginCli.buddies import getBuddyCompletions



def main(argv):
    
    pattern = argv[0]
    
    print ' '.join(getBuddyCompletions(pattern))
    
    



def entryPoint():
    return main(sys.argv[1:])

if __name__ == '__main__':
    entryPoint()
