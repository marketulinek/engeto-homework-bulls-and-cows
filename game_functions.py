"""
Core functions for the game: start, progress, end.
"""

import datetime

from helpful_functions import *

def welcome_player():

    print('Hi there!')
    print(create_separator())
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(create_separator())

def play_game():

    generated_number = generate_number(4)
    player_choice = input('Enter a number: ')
    number_of_guesses = 0
    print(create_separator())

    while player_choice != generated_number:

        number_of_guesses += 1

        if number_of_guesses == 1:
            print('>>>', player_choice)
        else:
            player_choice = input('>>> ')

        alert_message = validate_player_choice(player_choice)

        if alert_message:
            # When the validator has something to say
            print(alert_message)
            continue

        else:
            print(evaluate_player_choice(player_choice, generated_number))
            print(create_separator())
    
    return number_of_guesses

def show_results(number_of_guesses, time_duration):

    print(f"Correct, you've guessed the right number in {number_of_guesses} guesses!")
    print('Game duration:', datetime.timedelta(seconds=time_duration))
    print(create_separator())
    print("That's %s" % rate_results(number_of_guesses))