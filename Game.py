from Word import Word


class Game:
    MAX_ATTEMPTS = 8
    attempt = 1
    won = False

    @staticmethod
    def update_won():
        Game.won = True if Word.word == Word.revealed_word else False

    @staticmethod
    def print_end():
        if Game.won:
            print("You guessed the word " + Word.word + "!\nYou survived!")
        else:
            print("You lost!")
