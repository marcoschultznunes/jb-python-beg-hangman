from exceptions.letter_input_errors import *
from Word import Word


class Game:
    MAX_ATTEMPTS = 8
    attempt = 1
    won = False
    times_won = 0
    times_lost = 0
    word = None

    @staticmethod
    def update_won():
        Game.won = True if Game.word.word == Game.word.revealed_word else False

    @staticmethod
    def receive_letter():
        guess = input("Input a letter: ")

        if len(guess) != 1:
            raise NotCharError()
        if not guess.isalpha() or guess.isupper():
            raise NotLowerCaseEnglishError()
        return guess

    @staticmethod
    def ask_letter():
        print(Game.word.revealed_word)

        try:
            guess = Game.receive_letter()

            found = Game.word.reveal_letters(guess)

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

    @staticmethod
    def print_end():
        if Game.won:
            Game.times_won += 1
            print("You guessed the word " + Game.word.word + "!\nYou survived!\n")
        else:
            Game.times_lost += 1
            print("You lost!\n")

    @staticmethod
    def start_game():
        Game.attempt = 1
        Game.word = Word()
        Game.won = False

        while not Game.won and Game.attempt <= Game.MAX_ATTEMPTS:
            Game.ask_letter()

        Game.print_end()

    @staticmethod
    def show_results():
        print(f"You won: {Game.times_won} times.\nYou lost: {Game.times_lost} times.")
