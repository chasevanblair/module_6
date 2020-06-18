def score_input(test_name: str, test_score=0, invalid_message="Invalid test score, try again!"):
    while 100 < test_score < 0:
        print(invalid_message)
    # return {test_name: test_score}

    return test_name, test_score


#score_input()