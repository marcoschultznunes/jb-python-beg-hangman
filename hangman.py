from Game import Game
from Word import Word
from exceptions.letter_input_errors import *


def receive_letter():
    guess = input("Input a letter: ")

    if len(guess) != 1:
        raise NotCharError()
    if not guess.isalpha() or guess.isupper():
        raise NotLowerCaseEnglishError()
    return guess


def ask_letter():
    print(Word.revealed_word)

    try:
        guess = receive_letter()

        found = Word.reveal_letters(guess)

        if found:
            print()
            Game.update_won()
        else:
            print("That letter doesn't appear in the word.\n")
            Game.attempt += 1

    except NotCharError:
        print("Please, input a single letter.\n")
    except NotLowerCaseEnglishError:
        print("Please, enter a lowercase letter from the English alphabet.\n")
    except LetterAlreadyGuessedError:
        print("You've already guessed this letter.\n")


def main():
    print("H A N G M A N\n")

    while not Game.won and Game.attempt <= Game.MAX_ATTEMPTS:
        ask_letter()

    Game.print_end()


main()
