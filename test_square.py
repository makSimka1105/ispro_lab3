import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    
    def test_area_positive_side(self):
        result = area(5)
        self.assertEqual(result, 25)
    
    def test_area_unit_side(self):
        result = area(1)
        self.assertEqual(result, 1)
    
    def test_area_zero_side(self):
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_area_large_side(self):
        result = area(100)
        self.assertEqual(result, 10000)
    
    def test_area_fractional_side(self):
        result = area(2.5)
        self.assertEqual(result, 6.25)
    
    def test_area_small_fractional_side(self):
        result = area(0.5)
        self.assertEqual(result, 0.25)
    
    def test_perimeter_positive_side(self):
        result = perimeter(5)
        self.assertEqual(result, 20)
    
    def test_perimeter_unit_side(self):
        result = perimeter(1)
        self.assertEqual(result, 4)
    
    def test_perimeter_zero_side(self):
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_large_side(self):
        result = perimeter(100)
        self.assertEqual(result, 400)
    
    def test_perimeter_fractional_side(self):
        result = perimeter(2.5)
        self.assertEqual(result, 10.0)
    
    def test_perimeter_small_fractional_side(self):
        result = perimeter(0.5)
        self.assertEqual(result, 2.0)


