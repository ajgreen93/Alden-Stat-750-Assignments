import unittest
from hwk3 import makeBoW
	
class tokenizeTests(unittest.TestCase):

	def test_checksampletokens(self):
		self.assertEqual([1,1],makeBoW(['Now','is','the' ,'time','to','head','west','toward','wilder','lands'],['wilder','Now']))
	def test_checknotokens(self):
		self.assertEqual([0,0],makeBoW([],['wilder','Now']))
	def test_checknolexicon(self):
		self.assertEqual([],makeBoW(['some','stuff'],[]))
	def test_checkrepeattokens(self):
		self.assertEqual([1,2],makeBoW(['now','here','now'],['here','now']))
		
if __name__ == '__main__':
	unittest.main()
