import unittest
from stacking_cubes import *
	
class tokenizeTests(unittest.TestCase):

	##autocomplete tests
	
	#making sure the order words are stored in the table doesn't matter
	def test_sample_input(self):
		self.assertEqual(output_max_stack('stack_cubes_test.txt'),'1T 3B 5b 6r 7r 9f ')

	def test_sample_input1(self):
		self.assertEqual(output_max_stack('stack_cubes_test1.txt'),'1b 2f 5b ')
		
if __name__ == '__main__':
	unittest.main()
