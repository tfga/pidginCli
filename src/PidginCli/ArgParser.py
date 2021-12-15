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
    pidginMsg [<account>:]<buddy>...
    
    # Reads message from stdin
    echo "My message" | pidginMsg [<account1>:]<buddy1> [<account2>:]<buddy2> ...
    
    # Opens chat windows
    pidginMsg [<account1>:]<buddy1> [<account1>:]<buddy2> ...

    # <account> is optional, if not specified first account will be used when using multiple accounts and warning will be shown.

Options:
  -h --help                     Shows this screen.
"""
    
    
    return docopt(doc, argv=args)
    
    


if __name__ == '__main__':
    main()
