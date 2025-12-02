import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    
    def test_area_positive_dimensions(self):
        result = area(10, 5)
        self.assertEqual(result, 50)
    
    def test_area_unit_dimensions(self):
        result = area(1, 1)
        self.assertEqual(result, 1)
    
    def test_area_equal_sides(self):
        result = area(10, 10)
        self.assertEqual(result, 100)
    
    def test_area_zero_width(self):
        result = area(0, 10)
        self.assertEqual(result, 0)
    
    def test_area_zero_height(self):
        result = area(10, 0)
        self.assertEqual(result, 0)
    
    def test_area_fractional_dimensions(self):
        result = area(2.5, 4.0)
        self.assertEqual(result, 10.0)
    
    def test_area_large_dimensions(self):
        result = area(100, 50)
        self.assertEqual(result, 5000)
    
    def test_perimeter_positive_dimensions(self):
        result = perimeter(10, 5)
        self.assertEqual(result, 30)
    
    def test_perimeter_unit_dimensions(self):
        result = perimeter(1, 1)
        self.assertEqual(result, 4)
    
    def test_perimeter_zero_dimensions(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0)
    
    def test_perimeter_equal_sides(self):
        result = perimeter(7, 7)
        self.assertEqual(result, 28)
    
    def test_perimeter_fractional_dimensions(self):
        result = perimeter(2.5, 3.5)
        self.assertAlmostEqual(result, 12.0, places=5)
    
    def test_perimeter_large_dimensions(self):
        result = perimeter(100, 50)
        self.assertEqual(result, 300)

