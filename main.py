from helpful_functions import *
import time
import datetime

separator = '-' * 47

print('Hi there!')
print(separator)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(separator)

# -------------------------------
#            G A M E
# -------------------------------
generated_number = generate_number(4)
player_choice = ''
number_of_guesses = 0

player_choice = input('Enter a number: ')
print(separator)

time_start = time.time()

while player_choice != generated_number:

    # Counting guesses
    number_of_guesses += 1

    if number_of_guesses == 1:
        print('>>>', player_choice)
    else:
        player_choice = input('>>> ')


    if not player_choice.isnumeric():

        print('Entered value is not numeric, try again ...')
        continue

    elif len(player_choice) < 4:

        print('Entered number contains less than 4 digits, try again ...')
        continue

    elif len(player_choice) > 4:

        print('Entered number contains more than 4 digits, try again ...')
        continue

    elif player_choice[0] == '0':

        print('Entered number starts with zero, try again ...')
        continue

    else:

        for number in player_choice:
            if list(player_choice).count(number) > 1:

                print('Entered number contains duplicates, try again ...')
                break
        else:
        
            # -------------------------------
            #   Evaluating player's choice
            # -------------------------------
            bulls = 0
            cows = 0

            for i in range(0, 4):

                if player_choice[i] == generated_number[i]:
                    bulls += 1
                elif list(generated_number).count(player_choice[i]):
                    cows += 1
            
            word_bull = correct_word_by_frequency('bull', bulls)
            word_cow = correct_word_by_frequency('cow', cows)

            print(f'{bulls} {word_bull}, {cows} {word_cow}')
            print(separator)

else:
    # -------------------------------
    #            Victory
    # -------------------------------
    time_end = time.time()
    time_duration = time_end - time_start

    print(f"Correct, you've guessed the right number in {number_of_guesses} guesses!")
    print('Game duration:', datetime.timedelta(seconds=time_duration))
    print(separator)
    print("That's %s" % verbal_rating(number_of_guesses))