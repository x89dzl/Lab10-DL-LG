'''https://github.com/x89dzl/Lab10-DL-LG
Daniel Li Liam Gale'''
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-3, -4), -7)
        self.assertEqual(add(-3, 4), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(-5, -5), 0)
        self.assertEqual(subtract(-5, -4), -1)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0, 0), 0)
        self.assertEqual(mul(0, 1), 0)
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(2, -1), -2)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(-5, 10), -2)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(div(0, 5),ZeroDivisionError)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(math.e, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(logarithm(0,-1), ValueError("A must be larger than or equal to 0"))

    ##########################
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(logarithm(5, 8),ValueError("A cannot equal 0"))

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        # square_root(NUM)
        # Test basic function
        self.assertRaises(square_root(-9),ValueError("A cannot be smaller than 0"))

##########################
# Do not touch this
if __name__ == "__main__":
    unittest.main()