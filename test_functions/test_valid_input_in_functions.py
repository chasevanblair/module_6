import unittest

from more_functions.validate_input_functions import score_input


class Test(unittest.TestCase):
    def test_score_input_name(self):
        try:
            score_input()
        except TypeError:
            print("type error 1")

    def test_score_input_test_score_below_range(self):
        try:
            self.assertLess(score_input("test", -3), 0)
        except AssertionError:
            print("assert error 1")

    def test_score_input_test_score_above_range(self):
        try:
            self.assertGreater(score_input("testname", 200), 100)
        except AssertionError:
            print("assert error 2")

    def test_test_score_non_numeric(self):
        try:
            score_input("a", "x")
        except TypeError:
            print("type error 2")


if __name__ == "__main__":
    unittest.main()
