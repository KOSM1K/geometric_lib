import unittest
import math
r = "just a change for workflow testing"

def area(r):
    """
    Returns area of circle

    :param r: radius of a circle
    :return: area of a circle
    """
    return math.pi * r * r


def perimeter(r):
    """
    Returns perimeter of circle

    :param r: radius of circle
    :return: perimeter of circle
    """
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        print(0, res)

    def test_zero_radius_area(self):
        res = area(0)
        self.assertEqual(res, 0)
        print(0, res)

    def test_positive_radius_perimeter1(self):
        res = perimeter(1)
        self.assertEqual(res, 2*math.pi)
        print(1, res)

    def test_positive_radius_perimeter2(self):
        res = perimeter(2)
        self.assertEqual(res, 4*math.pi)
        print(2, res)

    def test_positive_radius_area1(self):
        res = area(1)
        self.assertEqual(res, math.pi)
        print(1, res)

    def test_positive_radius_area2(self):
        res = area(2)
        self.assertEqual(res, 4 * math.pi)
        print(2, res)

    def test_negative_radius_perimeter(self):
        with self.assertRaises(ValueError):
            res = perimeter(-1)
            print(-1, res)

    def test_negative_radius_area(self):
        with self.assertRaises(ValueError):
            res = area(-1)
            print(-1, res)


