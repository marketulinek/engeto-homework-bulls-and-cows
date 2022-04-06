from random import randrange

def generate_number(number_of_digits):
    """Generating the number with unique digits. No leading zero."""

    # To avoid leading zero
    generated_number = str(randrange(1, 10))

    while len(generated_number) < number_of_digits:

        generated_digit = str(randrange(10))

        # Only if digit isn't used yet
        if list(generated_number).count(generated_digit) < 1:
            generated_number += generated_digit

    return generated_number

def verbal_rating(number_of_guesses):

    if number_of_guesses < 6:
        return 'amazing'
    elif number_of_guesses < 11:
        return 'average'
    else:
        return 'not so good'