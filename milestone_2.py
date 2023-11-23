#milestone_2
import random

def choose_random_word(word_list):
    return random.choice(word_list)

def get_user_input():
    return input("Enter a letter: ")

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def main():
    favorite_fruits = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]

    word_list = favorite_fruits

    word = choose_random_word(word_list)
    print("Random Word:", word)

    guess = get_user_input()

    if is_valid_guess(guess):

        print("Good guess!")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()
