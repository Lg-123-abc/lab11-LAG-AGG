## https://github.com/Lg-123-abc/lab11-LAG-AGG
## Partner 1: Lillian Groudas
## Partner 2: Alexander Groudas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(7, 3), 10)
        self.assertNotEqual(add(4, 8), 3)
        self.assertIsNotNone(add(1, 2))


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 4), 1)
        self.assertNotEqual(subtract(5, 4), 2)
        self.assertIsNotNone(subtract(6, 1))
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertIsNotNone(mul(-1,1))
        self.assertNotEqual(mul(-1,-2), -2)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,6), 2)
        self.assertNotEqual(div(11, 22), 3)
        self.assertAlmostEqual(div(10, 3), 0.3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        self.assertRaises(ZeroDivisionError, div, 0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 0.5)
        self.assertNotEqual(logarithm(2, 4), 5)
        self.assertIsNotNone(logarithm(2, 4))

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        self.assertRaises(ValueError, logarithm, 0, 2)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        self.assertRaises(ValueError, logarithm, 10, -6)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertNotEqual(hypotenuse(8, 12), 2)
        self.assertGreater(hypotenuse(3, 4), 1)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        self.assertRaises(ValueError, square_root, -25)
        self.assertEqual(square_root(16), 4)
        self.assertNotEqual(square_root(25), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()