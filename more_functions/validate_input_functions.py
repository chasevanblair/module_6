"""

Program: validate_input_functions.py

Author: Chase Van Blair

Last date modified: 6/17/20


The purpose of this program is to accept test name, test score, and a message to display if invalid
then print invalid message if needed and return test name and test score

"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """
    takes parameters, checks them, raises error if wrong, then returns test name and test score
    :param test_name:
    :param test_score:
    :param invalid_message:
    :return test_name, test_score:
    """
    if test_score < 0 or test_score > 100:
        print(invalid_message)
        raise ValueError
    if type(test_score) != int:
        raise TypeError
        print(invalid_message)
    # return {test_name: test_score}

    return test_name, test_score

