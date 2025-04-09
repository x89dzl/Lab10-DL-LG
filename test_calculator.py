import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-3, -4), -7)
        self.assertEqual(add(-3, 4), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 5), 0)
        self.assertEqual(sub(-5, -5), 0)
        self.assertEqual(sub(-5, -4), -1)
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
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()