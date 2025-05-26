import random
from collections import Counter

class Hangman:
    def __init__(self):
        # List of possible secret words (all fruits in this case)
        self.fruits = [
            'apple', 'banana', 'mango', 'strawberry',
            'orange', 'grape', 'pineapple', 'apricot',
            'lemon', 'coconut', 'watermelon', 'cherry',
            'papaya', 'berry', 'peach', 'lychee', 'muskmelon'
        ]
        # Randomly select a secret word and convert to lowercase
        self.secret_word = random.choice(self.fruits).lower()
        # Set to store correctly guessed letters
        self.guessed_letters = set()
        # Initialize remaining attempts (word length + 2 bonus attempts)
        self.remaining_attempts = len(self.secret_word) + 2
        # Store maximum attempts for reference
        self.max_attempts = len(self.secret_word) + 2

    def display_word(self):
        """
        Generates the current state of the word to display,
        showing guessed letters and blanks for unguessed letters.
        Example: "a p p _ _" for "apple" if 'a' and 'p' were guessed
        """
        return ' '.join([letter if letter in self.guessed_letters else '_' 
                        for letter in self.secret_word])

    def get_valid_guess(self):
        """
        Handles user input validation for letter guesses.
        Ensures input is a single alphabetic character that hasn't been guessed yet.
        """
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter exactly one character.")
            elif not guess.isalpha():
                print("Please enter a letter (a-z).")
            elif guess in self.guessed_letters:
                print("You've already guessed that letter. Try another.")
            else:
                return guess

    def play(self):
        """
        Main game loop that controls the flow of the game:
        1. Displays initial information
        2. Handles each guess attempt
        3. Checks win/loss conditions
        """
        print("Welcome to Hangman!")
        print(f"Guess the fruit name. You have {self.remaining_attempts} attempts.")
        print(f"Word: {self.display_word()}")

        # Continue until player runs out of attempts
        while self.remaining_attempts > 0:
            # Get and process player's guess
            guess = self.get_valid_guess()
            self.guessed_letters.add(guess)

            # Check if guess is correct
            if guess in self.secret_word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                self.remaining_attempts -= 1
                print(f"Sorry, '{guess}' is not in the word. Attempts left: {self.remaining_attempts}")

            # Display current state of the word
            current_display = self.display_word()
            print(f"\nWord: {current_display}")

            # Check for win condition (no blanks remaining)
            if '_' not in current_display:
                print(f"\nCongratulations! You guessed the word: {self.secret_word}")
                return  # End game if won

        # If loop completes without winning
        print(f"\nGame over! The word was: {self.secret_word}")

if __name__ == "__main__":
    # Create and start a new game when script is run directly
    game = Hangman()
    game.play()