import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 3), 15)

    def test_area_negative_width(self):
        with self.assertRaises(ValueError):
            area(-4, 3)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            area(4, -3)

    def test_area_zero_width(self):
        self.assertEqual(area(0, 5), 0)

    def test_area_zero_height(self):
        self.assertEqual(area(7, 0), 0)

    def test_area_float1(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0, places=5)

    def test_area_float2(self):
        self.assertAlmostEqual(area(1.2, 3.5), 4.2, places=5)



    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_perimeter_negative_a(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 3)

    def test_perimeter_negative_b(self):
        with self.assertRaises(ValueError):
            perimeter(5, -3)
    def test_perimeter_one_zero(self):
        self.assertEqual(perimeter(0, 6), 12)

    def test_perimeter_both_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_float1(self):
        self.assertAlmostEqual(perimeter(2.5, 1.5), 8.0, places=5)

    def test_perimeter_float2(self):
        self.assertAlmostEqual(perimeter(0.8, 1.2), 4.0, places=5)