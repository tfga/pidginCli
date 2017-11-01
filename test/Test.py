# encoding: utf-8

import unittest

from PidginCli.buddies import getBuddyCompletions, extractLogin
from PidginCli.send import send


class Test(unittest.TestCase):


    def _test_send(self):
        
        send('msg', 'tfga@mpdft.gov.br')
        
    def test_getBuddyCompletions(self):
        
        # Casa pelo login
        self.assertEquals(getBuddyCompletions('rogerio'), ['rogerio.castro', 'rogerior'])
        
        # Casa pelo full name
        self.assertEquals(getBuddyCompletions('bernard'), ['thiago.almeida'])
        
    def test_extractLogin(self):
        
        self.assertEquals(extractLogin('thiago.almeida@mpdft.gov.br'), 'thiago.almeida')
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()