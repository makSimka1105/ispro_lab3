import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    
    def test_area_positive_values(self):
        result = area(10, 5)
        self.assertEqual(result, 25)
    
    def test_area_unit_values(self):
        result = area(1, 1)
        self.assertEqual(result, 0.5)
    
    def test_area_zero_base(self):
        result = area(0, 5)
        self.assertEqual(result, 0)
    
    def test_area_zero_height(self):
        result = area(10, 0)
        self.assertEqual(result, 0)
    
    def test_area_zero_both(self):
        result = area(0, 0)
        self.assertEqual(result, 0)
    
    def test_area_fractional_values(self):
        result = area(4.0, 2.5)
        self.assertEqual(result, 5.0)
    
    def test_area_large_values(self):
        result = area(100, 50)
        self.assertEqual(result, 2500)
    
    def test_area_small_fractional(self):
        result = area(0.5, 0.5)
        self.assertEqual(result, 0.125)
    
    def test_perimeter_positive_sides(self):
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)
    
    def test_perimeter_unit_sides(self):
        result = perimeter(1, 1, 1)
        self.assertEqual(result, 3)
    
    def test_perimeter_zero_sides(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0)
    
    def test_perimeter_one_zero_side(self):
        result = perimeter(0, 5, 5)
        self.assertEqual(result, 10)
    
    def test_perimeter_fractional_sides(self):
        result = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(result, 10.0, places=5)
    
    def test_perimeter_mixed_sides(self):
        result = perimeter(5, 12, 13)
        self.assertEqual(result, 30)
    
    def test_perimeter_large_sides(self):
        result = perimeter(100, 100, 100)
        self.assertEqual(result, 300)

