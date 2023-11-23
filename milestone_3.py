#milestone_3
import random

def choose_random_word(word_list):
    if not word_list:
        return None
    return word_list.pop(random.randrange(len(word_list)))

def get_valid_user_input():
    while True:
        guess = input("Enter a letter: ")
        if is_valid_guess(guess):
            return guess.lower()
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def check_guess(word, guess):
    if guess in word.lower():
        print(f"Good guess! '{guess}' is in the list.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the list. Please try again.")
        return False

def play_game():
    favorite_fruits = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]
    
    while True:
        word = choose_random_word(favorite_fruits)
        if word is None:
            print("There are no more words to guess. Game over.")
            break

        while True:
            guess = get_valid_user_input()
            if check_guess(word, guess):
                break

if __name__ == "__main__":
    play_game()