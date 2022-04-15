from random import randrange

def generate_number(number_of_digits):
    """Generating the number with unique digits and no leading zero."""

    # To avoid leading zero
    generated_number = str(randrange(1, 10))

    while len(generated_number) < number_of_digits:

        generated_digit = str(randrange(10))

        # Add only if digit isn't used yet
        if list(generated_number).count(generated_digit) < 1:
            generated_number += generated_digit

    return generated_number

def correct_word_by_frequency(word, number_of_frequency):
    """Checking if the entered word needs to be pluralize.
    
    Entered word must be in singular form.
    Return the correct form.

    """
    if number_of_frequency != 1:
        word += 's'

    return word

def verbal_rating(number_of_guesses):

    if number_of_guesses < 6:
        return 'amazing'
    elif number_of_guesses < 11:
        return 'average'
    else:
        return 'not so good'