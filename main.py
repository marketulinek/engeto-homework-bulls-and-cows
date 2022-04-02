from random import randrange

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

print(generated_number) # debugging porpose


# -------------------------------
#           LET'S PLAY
# -------------------------------
player_choice = ''

while player_choice != generated_number:

    player_choice = input('Enter a number: ')
    print(separator)

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
            bulls = 0
            cows = 0

            print('>>>', player_choice)

            for i in range(0, 4):

                if player_choice[i] == generated_number[i]:
                    bulls += 1
                elif list(generated_number).count(player_choice[i]):
                    cows += 1
            
            print(f'{bulls} bulls, {cows} cows')

else:
    print("Correct, you've guessed the right number in X guesses!")

