import random

favorite_fruits = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]

word_list = favorite_fruits

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")

print("You guessed:", guess)

user_input = input("Enter a single letter: ")
