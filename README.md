# :bison: BULLS & COWS :cow2:

:hammer: UNDER DEVELOPMENT - old version :hammer:

Homework 2a for Engeto Python Academy :mortar_board:

# :clipboard: Task Assignment

The goal is to create game Bulls and Cows.

The program has to contain:

1. Greeting the user and write the introductory text
2. Generate 4 digit secret number (digits has to be unique and no leading zero)
3. The player is guessing the number. The program alerts player if entered value is not numeric or does not contain 4 digits or starts with zero.
4. Evaluating the guessed number.
5. Write number of bulls (correctly guessed number and its position) and cows (correctly guessed number but not its position). Singular and plural form must be considered.


Example with number 2017:

    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    Enter a number:
    -----------------------------------------------
    >>> 1234
    0 bulls, 2 cows
    -----------------------------------------------
    >>> 6147
    1 bull, 1 cow
    -----------------------------------------------
    >>> 2417
    3 bulls, 0 cows
    -----------------------------------------------
    >>> 2017
    Correct, you've guessed the right number
    in 4 guesses!
    -----------------------------------------------
    That's {amazing, average, not so good, ...}



The program can contain more features. For example:

- counting how long it takes the user to guess the secret number
