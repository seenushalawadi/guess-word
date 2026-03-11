from words import Words

class GuessTheWord:
    def __init__(self):
        self.max_attempts = 10
        self.remaining_attempts = self.max_attempts
        self.word = Words()

    def start(self):
        print("🎮 Welcome to 'Guess the Word' game!")
        while self.remaining_attempts > 0:
            print(f"\nWord: {self.word}")
            print(f"Tries left: {self.remaining_attempts}")
            user_input = self.get_input()

            if not user_input:
                print("Invalid input. Please enter a single letter.")
                continue

            guessed_right = self.word.guess(user_input)

            if guessed_right:
                print(f"✅ Good job! '{user_input}' is correct.")
                if self.word.is_fully_guessed():
                    print(f"\n🎉 Congratulations! You guessed the word: {self.word.get_word()}")
                    break
            else:
                self.remaining_attempts -= 1
                print(f"❌ Oops! '{user_input}' is not in the word.")

        if self.remaining_attempts == 0:
            print(f"\n💀 Game Over! The correct word was: {self.word.get_word()}")

    def get_input(self) -> str:
        guess = input("Enter a letter to guess the word: ").strip().lower()
        return guess[0] if guess and guess[0].isalpha() else ''
