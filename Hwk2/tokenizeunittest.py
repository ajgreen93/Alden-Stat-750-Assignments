import unittest
from hwk2 import tokenize
	
class tokenizeTests(unittest.TestCase):

	def test_checksamplestring(self):
		self.assertEqual(tokenize('samplestring.txt'),['Now','is','the' ,'time','to','head','west','toward','wilder','lands'])
	def test_checkempty(self):
		self.assertEqual(tokenize('empty.txt'),[])
		
		
if __name__ == '__main__':
	unittest.main()

	
