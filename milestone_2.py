import random

word_list = ["Durian", "Orange", "Apple", "Mango", "Pineapple"]
word=random.choice(word_list)
print(word)
word_guessed = ['_' for i in range(len(word))]

print(word_guessed)
print(len(word_guessed))

num_letters = len(set(word))
print(f'unique word count {num_letters}')

print(f'unique words {set(word)}')
