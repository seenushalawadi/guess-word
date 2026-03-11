import random

class Words:
    def __init__(self):
        self._word_list = [
            "python", "coding", "programming", "list", "set", "tuple",
            "jupyter", "spyder", "dictionary", "lambda", "cobra", "numpy",
            "pandas", "class", "interpreter", "anaconda", "extensions",
            "objects", "internship", "intern", "expression", "statement"
        ]
        self._selected_word = random.choice(self._word_list)
        self._guessed_letters = ['_' for _ in self._selected_word]

    def __str__(self):
        return ' '.join(self._guessed_letters)

    def guess(self, letter: str) -> bool:
        guessed_correctly = False
        for index, char in enumerate(self._selected_word):
            if char == letter and self._guessed_letters[index] == '_':
                self._guessed_letters[index] = letter
                guessed_correctly = True
        return guessed_correctly

    def is_fully_guessed(self) -> bool:
        return '_' not in self._guessed_letters

    def get_word(self) -> str:
        return self._selected_word
