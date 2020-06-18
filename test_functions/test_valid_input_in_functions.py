import unittest

from more_functions.validate_input_functions import score_input


class Test(unittest.TestCase):
    def test_score_input_name(self):
        try:
            score_input("x")
        except TypeError:
            print("type error 1")

    def test_score_input_test_score_valid(self):
        try:
            score_input("x", 60, "invalid")
        except ValueError:
            print("invalid test score")

    def test_score_input_test_score_below_range(self):
        try:
            score_input("test", -3)
        except ValueError:
            print("Input less than 0")

    def test_score_input_test_score_above_range(self):
        try:
            score_input("testname", 200)
        except ValueError:
            print("Input greater than 100")

    def test_test_score_non_numeric(self):
        try:
            score_input("a", "x")
        except TypeError:
            print("test score is not numeric")


if __name__ == "__main__":
    unittest.main()
