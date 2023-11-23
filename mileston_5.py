#milestone_5
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self._choose_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def _choose_random_word(self):
        return random.choice(self.word_list).lower()

    def _replace_letters_in_word_guessed(self, guess):
        guess = guess.lower()
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def _print_correct_guess_message(self, guess):
        print(f"Good guess! '{guess}' is in the list.")

    def _print_incorrect_guess_message(self, guess):
        self.num_lives -= 1
        print(f"Sorry, '{guess}' is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()

    def _is_repeated_guess(self, guess):
        return guess in self.list_of_guesses

    def check_guess(self, guess):
        if guess in self.word:
            self._print_correct_guess_message(guess)
            self._replace_letters_in_word_guessed(guess)
            return True
        else:
            self._print_incorrect_guess_message(guess)
            return False

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self._is_repeated_guess(guess):
                print("You already tried that letter!")
            else:
                if self.check_guess(guess):
                    break
            self.list_of_guesses.append(guess)

    def is_game_over(self):
        if self.num_lives == 0:
            print("You lost!")
            return True
        elif self.num_letters == 0:
            print("Congratulations, you win!")
            return True
        return False

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while not game.is_game_over():
        game.ask_for_input()

if __name__ == "__main__":
    word_list_example = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]
    play_game(word_list_example)