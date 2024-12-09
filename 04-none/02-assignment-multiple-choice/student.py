def multiple_choice(right_answer, given_answer):
    if given_answer == right_answer:
        result = 1
    elif given_answer != right_answer:
        result = -0.2
    if given_answer == None:
        result = 0
    return result