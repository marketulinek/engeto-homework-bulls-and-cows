# 

def verbal_rating(number_of_guesses):

    if number_of_guesses < 6:
        return 'amazing'
    elif number_of_guesses < 11:
        return 'average'
    else:
        return 'not so good'