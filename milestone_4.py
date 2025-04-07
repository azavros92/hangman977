import random
# Hangman Game Class
# This class encapsulates the game logic and state
# The class is designed to be reusable and maintainable
# It includes methods for checking guesses, asking for input, and managing game state


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        print(f"DEBUG: The secret word is '{self.word}'")  # for testing

    def check_guess(self, guess):  # ✅ Proper indentation
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(f"Current word: {' '.join(self.word_guessed)}")
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):  # ✅ Now it's a proper class method
        while True:
            guess = input("Please enter a single letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break



if __name__ == "__main__":
    words = ["banana", "apple", "grape", "peach"]
    game = Hangman(words)
    
    # Loop to keep asking until game ends
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()
    
    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print("Game over. Better luck next time.")