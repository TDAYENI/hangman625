from  milestone_2 import word
print(word)

def check_guess (guess):
    while True:
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    ask_for_input(guess)


def ask_for_input(guess):
    if guess.lower() in word.lower():
        print(f'"Good guess! {guess} is in the word."')
    else:
        print(f'"Sorry, {guess} is not in the word. Try again."')


guess =input('Enter a single letter: ')
check_guess(guess)

    """
word: The word to be guessed
word_guessed:A list of the letters of the word, with _ for each letter not yet guessed.
num_letters:he number of UNIQUE letters in the word that have not been guessed yet
num_lives: int - The number of lives the player has at the start of the game.
word_list: list - A list of words
list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
    """