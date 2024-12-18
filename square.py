import unittest


def area(a):
    """
    Returns area of square

    :param a: size of side
    :return: area of square
    """
    return a * a


def perimeter(a):
    """
    Returns area of square

    :param a: size of side
    :return: perimeter of square
    """
    return 4 * a

class SquareTestSuite(unittest.TestCase):
    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            res = area(-1)
            # print(-1,res)

    def test_area_zero_side(self):
        res = area(0)
        self.assertEqual(res, 0)
        # print(0, res)

    def test_area1(self):
        res = area(4)
        self.assertEqual(res, 16)
        # print (4, res)

    def test_area2(self):
        res = area(2)
        self.assertEqual(res, 4)
        # print(2, res)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            res = perimeter(-1)
            # print(-1, res)

    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        # print(0, res)

    def test_perimeter1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
        # print(1, res)
