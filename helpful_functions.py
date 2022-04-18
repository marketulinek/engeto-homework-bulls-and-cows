from random import randrange

def create_separator(char='-', number_of_char=47):
    """Create a separator from a certain number of chosen characters.

    Default character is hyphen.
    Default number of characters is 47.
    
    """
    return char * number_of_char

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
    """Check if number contains duplicated digits and return True/False."""

    for digit in number:
        if list(number).count(digit) > 1:
            return True

    return False

def validate_player_choice(player_choice):
    """Validate that player's input meets these conditions:

    - 4-digit number
    - unique digits
    - no leading zero

    Return alert message. If None is returned, player's input meets conditions.

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

def evaluate_player_choice(player_choice, generated_number):
    """Write number of bulls (correctly guessed number and its position)
    and cows (correctly guessed number but not its position).

    Singular and plural form is considered.
    Return message with results.

    """
    bulls = 0
    cows = 0

    for i in range(0, 4):

        if player_choice[i] == generated_number[i]:
            bulls += 1
        elif list(generated_number).count(player_choice[i]):
            cows += 1
    
    word_bull = correct_word_by_frequency('bull', bulls)
    word_cow = correct_word_by_frequency('cow', cows)

    return f'{bulls} {word_bull}, {cows} {word_cow}'

def rate_results(number_of_guesses):
    """Rate results according to the number of guesses it takes."""

    if number_of_guesses < 6:
        return 'amazing'
    elif number_of_guesses < 11:
        return 'average'
    else:
        return 'not so good'