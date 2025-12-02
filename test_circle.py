import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    
    def test_area_positive_radius(self):
        result = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_unit_radius(self):
        result = area(1)
        expected = math.pi
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_zero_radius(self):
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_area_fractional_radius(self):
        result = area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_large_radius(self):
        result = area(100)
        expected = math.pi * 10000
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_perimeter_large_radius(self):
        result = perimeter(50)
        expected = 2 * math.pi * 50
        self.assertAlmostEqual(result, expected, places=5)

