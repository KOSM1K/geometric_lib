import unittest


def area(a, h):
    """
    Returns area of triangle

    :param a: size of side
    :param h: size of height to this side
    :return: area of triangle
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Returns perimeter of triangle

    :param a: size of first side
    :param b: size of second side
    :param c: size of third side
    :return: perimeter of triangle
    """
    return a + b + c

class TriangleTestSuite(unittest.TestCase):
    def test_area_zero_height(self):
        res = area(100, 0)
        self.assertEqual(res, 0)
        # print(100, 0, " | ", res)

    def test_area_zero_side(self):
        res = area(0, 100)
        self.assertEqual(res, 0)
        # print(0, 100, " | ", res)

    def test_area1(self):
        res = area(3,4)
        self.assertEqual(res, 6)
        # print(3, 4, " | ", res)

    def test_perimeter_impossible_triangle1(self):
        with self.assertRaises(ValueError):
            res = perimeter(100, 1, 1)
            # print(100, 1, 1, " | ", res)

    def test_perimeter_impossible_triangle2(self):
        with self.assertRaises(ValueError):
            res = perimeter(1, 100, 1)
            # print(1, 100, 1, " | ",res)

    def test_perimeter_impossible_triangle3(self):
        with self.assertRaises(ValueError):
            res = perimeter(1, 1, 100)
            # print(1, 1, 100, " | ",res)

    def test_perimeter_negative_side1(self):
        with self.assertRaises(ValueError):
            res = perimeter(-1, 1, 1)
            # print(-1, 1, 1, " | ", res)

    def test_perimeter_negative_side2(self):
        with self.assertRaises(ValueError):
            res = perimeter(1, -1, 1)
            # print(1, -1, 1, " | ", res)

    def test_perimeter_negative_side3(self):
        with self.assertRaises(ValueError):
            res = perimeter(1, 1, -1)
            # print(1, 1, -1, " | ",res)





