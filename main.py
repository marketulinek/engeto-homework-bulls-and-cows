from random import randrange
import time

separator = '-' * 47

print('Hi there!')
print(separator)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(separator)

# -------------------------------
#       GENERATING NUMBER
# -------------------------------
generated_number = str(randrange(1, 10))

while len(generated_number) < 4:

    generated_digit = str(randrange(10))

    if list(generated_number).count(generated_digit) < 1:
        generated_number += generated_digit


# -------------------------------
#           LET'S PLAY
# -------------------------------
player_choice = ''
number_of_guesses = 0

player_choice = input('Enter a number: ')
print(separator)

time_start = time.time()

while player_choice != generated_number:

    if number_of_guesses > 0:
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

    else:

        for number in player_choice:
            if list(player_choice).count(number) > 1:

                print('Entered number contains duplicates, try again ...')
                break
        else:
        
            # -------------------------------
            #   Evaluating player's choice
            # -------------------------------
            number_of_guesses += 1
            word_bull = 'bull'
            word_cow = 'cow'
            bulls = 0
            cows = 0

            if number_of_guesses == 0:
                print('>>>', player_choice)

            for i in range(0, 4):

                if player_choice[i] == generated_number[i]:
                    bulls += 1
                elif list(generated_number).count(player_choice[i]):
                    cows += 1
            
            if bulls != 1:
                word_bull += 's'
            if cows != 1:
                word_cow += 's'
            
            print(f'{bulls} {word_bull}, {cows} {word_cow}')
            print(separator)

else:
    time_end = time.time()
    time_duration = time_end - time_start

    if number_of_guesses < 6:
        verbal_rating = 'amazing'
    elif number_of_guesses < 11:
        verbal_rating = 'average'
    else:
        verbal_rating = 'not so good'

    print(f"Correct, you've guessed the right number in {number_of_guesses} guesses!")
    print('Game duration in seconds:', time_duration)
    print(separator)
    print(f"That's {verbal_rating}")