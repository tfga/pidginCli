#!/usr/bin/python
# coding=utf-8

import sys
from docopt import docopt


def main():
    
    args = getOpts(sys.argv[1:])
    
    print(args)
    
    
def getOpts(args):
    
    doc = """
Usage:
    pidginMsg <buddy>...
    
    # Reads message from stdin
    echo "My message" | pidginMsg <buddy1> <buddy2> ...
    
    # Opens chat windows
    pidginMsg <buddy1> <buddy2> ...
 
Options:
  -h --help                     Shows this screen.
"""
    
    
    return docopt(doc, argv=args)
    
    


if __name__ == '__main__':
    main()
