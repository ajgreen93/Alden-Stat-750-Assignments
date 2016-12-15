import unittest
from cutting_sticks import *

class tokenizeTests(unittest.TestCase):

    def test_order(self):
        self.assertEqual(best_cuts_complete(10,[4,2,7]),best_cuts_complete(10,[2,4,7]))
	
    def test_empty(self):
        self.assertEqual(best_cuts_complete(10,[]),[])
    
    def test_given_example(self):
        self.assertEqual(best_cuts_complete(10,[2,4,7]),[4,2,7])
		
if __name__ == '__main__':
	unittest.main()
