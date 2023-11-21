import random

def choose_random_word(word_list):
    return random.choice(word_list)

def get_user_input():
    return input("Enter a single letter: ")

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def check_guess(word, guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word.lower():
        # Print a message for a correct guess
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        # Print a message for an incorrect guess
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

def ask_for_input(word):
    while True:
        # Step 2: Move the code to check if the guess is in the word into this function
        guess = get_user_input()

        # Step 3: Call the check_guess function to check if the guess is in the word
        if is_valid_guess(guess):
            if check_guess(word, guess):
                break
        else:
            # Print an error message for an invalid guess
            print("Invalid letter. Please, enter a single alphabetical character.")

def main():
    favorite_fruits = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]
    word = choose_random_word(favorite_fruits)

    # Step 4: Call the ask_for_input function to test the code
    ask_for_input(word)

if __name__ == "__main__":
    main()