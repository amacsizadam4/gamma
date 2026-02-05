"""Unit tests for the is_divisible_by_3_or_5 function."""

import unittest
from SE import is_divisible_by_3_or_5
class TestIsDivisibleBy3Or5(unittest.TestCase):
    def test_divisible_by_3(self):
        self.assertTrue(is_divisible_by_3_or_5(9))

    def test_divisible_by_5(self):
        self.assertTrue(is_divisible_by_3_or_5(10))

    def test_divisible_by_both(self):
        self.assertTrue(is_divisible_by_3_or_5(15))

    def test_not_divisible(self):
        self.assertFalse(is_divisible_by_3_or_5(7))

    def test_zero(self):
        self.assertTrue(is_divisible_by_3_or_5(0))


if __name__ == '__main__':
    unittest.main()