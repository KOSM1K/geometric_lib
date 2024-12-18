import unittest

from stem.util.test_tools import assert_equal


def area(a, b):
    """
    Returns area of rectangle

    :param a: first dimension size
    :param b: second dimension size
    :return: area of rectangle
    """
    return a * b

def perimeter(a, b):
    """
    Returns perimeter of rectangle

    :param a: first dimension size
    :param b: second dimension size
    :return: perimeter of rectangle
    """
    return 2*(a + b)

class RectangleTestSuite(unittest.TestCase):
    def test_zero_sides_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        # print(0 ,0, " | ",  res)

    def test_zero_sides_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
        # print(0, 0, " | ", res)

    def test_one_side_zero_perimeter1(self):
        res = perimeter(0, 5)
        self.assertEqual(res, 10)
        # print(0, 5, " | ", res)

    def test_one_side_zero_perimeter2(self):
        res = perimeter(5, 0)
        self.assertEqual(res, 10)
        # print(5, 0, " | ", res)

    def test_one_side_zero_area1(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
        # print(0, 5, " | ", res)

    def test_one_side_zero_area2(self):
        res = area(5, 0)
        self.assertEqual(res, 0)
        # print(5, 0, " | ", res)

    def test_positive_sides_perimeter(self):
        res = perimeter(4, 5)
        self.assertEqual(res, 18)
        # print(4, 5, " | ", res)

    def test_positive_sides_area(self):
        res = area(4, 5)
        self.assertEqual(res, 20)
        # print(4, 5, " | ", res)

    def test_negative_side_perimeter1(self):
        with self.assertRaises(ValueError):
            res = perimeter(-1, 0)
            # print(-1, 0, " | ",res)

    def test_negative_side_perimeter2(self):
        with self.assertRaises(ValueError):
            res = perimeter(0, -1)
            # print(0, -1, " | ",res)

    def test_negative_side_area1(self):
        with self.assertRaises(ValueError):
            res = area(-1, 0)
            # print(-1, 0, " | ", res)

    def test_negative_side_area2(self):
        with self.assertRaises(ValueError):
            res = area(0, -1)
            # print(0, -1, " | ",res)





