import random
from exceptions.letter_input_errors import LetterAlreadyGuessedError


class Word:
    words = tuple(["python", "java", "swift", "javascript"])

    def __init__(self):
        self.word = Word.words[random.randint(0, len(Word.words) - 1)]
        self.revealed_word = "-" * len(self.word)
        self.guessed_letters = set()

    def reveal_letters(self, letter):
        found = False

        if letter in self.guessed_letters:
            print(self.guessed_letters)
            raise LetterAlreadyGuessedError()

        for i, word_letter in enumerate(self.word):
            if letter == word_letter:
                revealed = list(self.revealed_word)
                revealed[i] = letter
                self.revealed_word = "".join(revealed)
                found = True

        self.guessed_letters.add(letter)

        return found
