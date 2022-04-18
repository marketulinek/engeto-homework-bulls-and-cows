import time

from game_functions import *

def main():

    welcome_player()
    time_start = time.time()

    # Let's play
    number_of_guesses = play_game()

    time_end = time.time()
    time_duration = time_end - time_start

    show_results(number_of_guesses, time_duration)

if __name__ == "__main__":
    main()