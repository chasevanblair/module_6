import unittest

from more_functions.validate_input_functions import score_input


class Test(unittest.TestCase):
    def test_score_input_test_score_below_range(self):
        self.assertLess(score_input("test", -3), 0)

    def test_score_input_test_score_above_range(self):
        self.assertGreater(score_input("testname", 200), 100)

    def test_test_score_non_numeric(self):
        try:
            score_input("a", "x")
        except TypeError:
            print("type error")


if __name__ == "__main__":
    unittest.main()
