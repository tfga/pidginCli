# encoding: utf-8

import unittest
from PidginCli.Main import launchEditor


class Test(unittest.TestCase):


    def _test_launchEditor(self):
        
        print launchEditor()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()