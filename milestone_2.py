import random
# removing a random word from a list
word_list = ["Durian", "Orange", "Apple", "Mango", "Pineapple"]
word=random.choice(word_list)
print(word)
# list comp creates list of "_" equal to word len
word_guessed = ['_' for i in range(len(word))]
guess = 'a'
print(word_guessed)
print(len(word_guessed))
#number of unique words
num_letters = len(set(word))
print(f'unique word count {num_letters}')
#unique letters in word
print(f'unique words {set(word)}')
#identfies where the guessed word is and adds is to the word_guessed list
""" for i, alpanet in range(len(word)):
     if guess == word.lower()[i]:
          word_guessed[i] = word[i] """


for i, alphabet in enumerate(word.lower()):
    if guess == alphabet:
        print(alphabet)
        word_guessed[i] = word[i]

print(word_guessed)
print(word)