"""

Program: test_valid_input_in_functions.py

Author: Chase Van Blair

Last date modified: 6/17/20


The purpose of this program is to test validate_input_functions
to make sure it works correctly

"""
import unittest

from more_functions.validate_input_functions import score_input


class Test(unittest.TestCase):
    def test_score_input_name(self):
        """
        test score input name is a string
        """
        try:
            score_input("x")
        except TypeError:
            print("type error 1")

    def test_score_input_test_score_valid(self):
        """
        test score input is valid
        """
        try:
            score_input("x", 60, "invalid")
        except ValueError:
            print("invalid test score")

    def test_score_input_test_score_below_range(self):
        """
        test if score input is below 0
        """
        try:
            score_input("test", -3)
        except ValueError:
            print("Input less than 0")

    def test_score_input_test_score_above_range(self):
        """
        test if score input is above 100
        """
        try:
            score_input("testname", 200)
        except ValueError:
            print("Input greater than 100")

    def test_test_score_non_numeric(self):
        """
        test if score input is numeric
        """
        try:
            score_input("a", "x")
        except TypeError:
            print("test score is not numeric")

    def test_score_input_invalid_message(self):
        """
        test the invalid message input
        """
        try:
            score_input("s", 28, "invalid")
        except TypeError:
            print("type error with invalid message")


if __name__ == "__main__":
    unittest.main()
