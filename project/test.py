from fractions import Fraction
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_mix_numbers(self):
        """
        Test that it can sum integers and fractions together
        """
        data = [1, Fraction(1, 2), Fraction(5,4)]
        result = sum(data)
        self.assertEqual(result, 2.75)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()

# These tests demonstrate the sum() funciton can take integers or fractions and sum them together.