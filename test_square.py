import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(4), 16)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_area_negative_zero(self):
        with self.assertRaises(ValueError):
            area(-0.1)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_float1(self):
        self.assertAlmostEqual(area(2.5), 6.25, places=5)

    def test_area_float2(self):
        self.assertAlmostEqual(area(0.4), 0.16, places=5)



    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_negative1(self):
        with self.assertRaises(ValueError):
            perimeter(-4)

    def test_perimeter_negative2(self):
        with self.assertRaises(ValueError):
            perimeter(-10)

    def test_perimeter_float1(self):
        self.assertAlmostEqual(perimeter(1.5), 6.0, places=5)

    def test_perimeter_float2(self):
        self.assertAlmostEqual(perimeter(0.75), 3.0, places=5)