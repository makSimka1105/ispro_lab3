import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(6, 4), 12)

    def test_area_negative_base(self):
        with self.assertRaises(ValueError):
            area(-5, 4)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            area(5, -4)

    def test_area_zero_base(self):
        self.assertEqual(area(0, 5), 0)

    def test_area_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_area_float1(self):
        self.assertAlmostEqual(area(3.5, 2.0), 3.5, places=5)

    def test_area_float2(self):
        self.assertAlmostEqual(area(2.4, 1.5), 1.8, places=5)


    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_negative_a(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_perimeter_negative_b(self):
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)

    def test_perimeter_one_zero(self):
        self.assertEqual(perimeter(0, 4, 5), 9)

    def test_perimeter_all_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float1(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.0), 10.0, places=5)

    def test_perimeter_float2(self):
        self.assertAlmostEqual(perimeter(1.1, 2.2, 3.3), 6.6, places=5)