import random

class Hangman:
    """
    A class to represent the Hangman game.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the game with a random word, lives, and other game state variables.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        print(f"DEBUG: The secret word is '{self.word}'")  # For testing purposes

    def _update_word_guessed(self, guess):
        """
        Update the guessed word with the correct letter.
        """
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

    def _validate_guess(self, guess):
        """
        Validate the user's guess.
        """
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        return True

    def process_guess(self, guess):
        """
        Process the user's guess and update the game state.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            # Count how many *unique* new letters were revealed by this guess
            previously_hidden = self.word_guessed.count('_')
            self._update_word_guessed(guess)
            currently_hidden = self.word_guessed.count('_')
            letters_revealed = previously_hidden - currently_hidden
            if letters_revealed > 0:
                self.num_letters -= 1
            print(f"Current word: {' '.join(self.word_guessed)}")
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def get_user_guess(self):
        """
        Prompt the user for a guess and validate it.
        """
        while True:
            guess = input("Please enter a single letter: ")
            if self._validate_guess(guess):
                self.list_of_guesses.append(guess)
                self.process_guess(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.get_user_guess()
        else:
            print("Congratulations. You won the game!")
            break

# Run the game
words = ["banana", "apple", "grape", "peach"]
play_game(words)