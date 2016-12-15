import unittest
from polygon_classes import *

def check_invalid_shape():
    try:
        Quadrilateral([(0,0),(5,0),(0,2),(4,4)]).number_of_sides()
    except ValueError:
        return True
    else:
        return False
        
class tokenizeTests(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(Triangle([(0,0),(5,0),(0,2)]).area(),5)
    
    def test_rectangle_area(self):
        self.assertEqual(Quadrilateral([(0,0),(5,0),(5,5),(0,5)]).area(),25)
    
    def test_invalid_shape(self):
        self.assertEqual(check_invalid_shape(),True)
    
    def test_pentagon_perimeter(self):
        self.assertEqual(Pentagon([(0,0),(0,1),(1,2),(2,1),(2,0)]).perimeter(),1+sqrt(2)+sqrt(2)+1+2)   
         
if __name__ == '__main__':
    unittest.main()
