import random

favorite_fruits = ["Grapes", "Apple", "Orange", "Pineapple", "Banana"]

word_list = favorite_fruits

word = random.choice(word_list)

print("Randomly chosen word:", word)

guess = input("Enter a single letter: ")

print("User's guess:", guess)
