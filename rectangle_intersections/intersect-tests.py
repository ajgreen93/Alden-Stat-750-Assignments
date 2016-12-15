import unittest
from rectangle_intersections import *

class tokenizeTests(unittest.TestCase):
    
    def test_not_axis_aligned_intersect(self):
        self.assertEqual(Rectangle((-5,0),(0,5),(5,0),(0,-5)).intersectCircle(Circle((-1,0.5),5)),True)
        
    def test_intersect(self):
        self.assertEqual(Rectangle((0,0),(5,5),(5,0),(0,5)).intersectCircle(Circle((-1,0.5),2)),True)
    
    def test_different_regions(self):
        self.assertEqual(Rectangle((10,10),(5,5),(5,10),(10,5)).intersectCircle(Circle((0,0),2)),False)
        
    def test_just_touching_point(self):
        self.assertEqual(Rectangle((0,0),(5,5),(5,0),(0,5)).intersectCircle(Circle((0,-2),2)),True)
        
    def test_just_touching_line(self):
        self.assertEqual(Rectangle((0,0),(5,5),(5,0),(0,5)).intersectCircle(Circle((2,-2),2)),True)
        
    def test_outside_circle(self):
        self.assertEqual(Rectangle((0,0),(5,5),(5,0),(0,5)).intersectCircle(Circle((2,2),.5)),False)
    
    def test_inside_circle(self):
        self.assertEqual(Rectangle((0,0),(5,5),(5,0),(0,5)).intersectCircle(Circle((2,2),15)),False)
                
if __name__ == '__main__':
    unittest.main()
