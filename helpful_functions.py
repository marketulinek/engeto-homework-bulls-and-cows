from random import randrange

def generate_number(number_of_digits):
    """Generate and return number with unique digits and no leading zero."""

    # To avoid leading zero
    generated_number = str(randrange(1, 10))

    while len(generated_number) < number_of_digits:

        generated_digit = str(randrange(10))

        # Add only if digit isn't used yet
        if list(generated_number).count(generated_digit) < 1:
            generated_number += generated_digit

    return generated_number

def check_duplicate_digits(number):
    """Check if number contains duplicate digits and return True/False."""
    for digit in number:

        if list(number).count(digit) > 1:
            return True

    return False

def validate_player_choice(player_choice):
    """Validate that player's input meets these criteria:

    - 4 digit number
    - unique digits
    - no leading zero

    Return alert message. If None is returned, player's input meets criteria.

    """
    if not player_choice.isnumeric():
        return 'Entered value is not numeric, try again ...'
    if len(player_choice) < 4:
        return 'Entered number contains less than 4 digits, try again ...'
    if len(player_choice) > 4:
        return 'Entered number contains more than 4 digits, try again ...'
    if player_choice[0] == '0':
        return 'Entered number starts with zero, try again ...'
    if check_duplicate_digits(player_choice):
        return 'Entered number contains duplicates, try again ...'

    return None

def correct_word_by_frequency(word, number_of_frequency):
    """Check if the entered word needs to be pluralize.
    
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