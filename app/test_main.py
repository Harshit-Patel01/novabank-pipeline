import unittest
from main import simple_interest


class TestInterest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(simple_interest(10000, 7, 2), 1400.0)

    def test_zero_years(self):
        self.assertEqual(simple_interest(5000, 5, 0), 0.0)


if __name__ == "__main__":
    unittest.main()
