import unittest
from hwk2 import tokenize
from hwk3 import makeBoW
from hwk4 import analyzeCorpus
	
class tokenizeTests(unittest.TestCase):

	def test_checksamplecorpus(self):
		self.assertEqual(analyzeCorpus(['text1.txt','text2.txt']),
		[[1,1,1,0],[0,1,0,1]])
		
		
if __name__ == '__main__':
	unittest.main()
