import random

def choose_random_word(word_list):

    return random.choice(word_list)

# Example usage:
word_list = ["Durian", "Orange", "Apple", "Mango", "Pineapple"]
word = choose_random_word(word_list)

print(word)

""" guess =input('Enter a single letter: ')
if len(guess) == 1 and guess.isalpha():
    print('"Good guess!"')
else:
    print("Oops! That is not a valid input.") """