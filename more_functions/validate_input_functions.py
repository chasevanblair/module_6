def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    if test_score < 0 or test_score > 100:
        print(invalid_message)
        raise ValueError
    if type(test_score) != int:
        raise TypeError
        print(invalid_message)
    # return {test_name: test_score}

    return test_name, test_score

