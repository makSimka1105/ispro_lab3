import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertAlmostEqual(area(3), math.pi * 9, places=5)

    def test_area_negative_radius1(self):
        with self.assertRaises(ValueError):
            area(-2)

    def test_area_negative_radius2(self):
        with self.assertRaises(ValueError):
            area(-5.5)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_float1(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25, places=5)

    def test_area_float2(self):
        self.assertAlmostEqual(area(1.2), math.pi * 1.44, places=5)



    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(4), 2 * math.pi * 4, places=5)

    def test_perimeter_negative1(self):
        with self.assertRaises(ValueError):
            perimeter(-3)

    def test_perimeter_negative2(self):
        with self.assertRaises(ValueError):
            perimeter(-7.1)

    def test_perimeter_float1(self):
        self.assertAlmostEqual(perimeter(1.5), 2 * math.pi * 1.5, places=5)

    def test_perimeter_float2(self):
        self.assertAlmostEqual(perimeter(0.8), 2 * math.pi * 0.8, places=5)