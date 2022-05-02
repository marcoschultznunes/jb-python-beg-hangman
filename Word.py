import random
from exceptions.letter_input_errors import LetterAlreadyGuessedError

class Word:
    words = tuple(["python", "java", "swift", "javascript"])
    word = words[random.randint(0, len(words) - 1)]
    revealed_word = "-" * len(word)

    @staticmethod
    def reveal_letters(letter):
        found = False

        for i, word_letter in enumerate(Word.word):
            if letter == Word.revealed_word[i]:
                raise LetterAlreadyGuessedError()
            elif letter == word_letter:
                revealed = list(Word.revealed_word)
                revealed[i] = letter
                Word.revealed_word = "".join(revealed)
                found = True

        return found
