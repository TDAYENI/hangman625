
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a guess and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each guess not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user for a guess.
    '''
    def __init__(self, word_list , num_lives):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        self.word= random.choice(word_list)
        print(self.word)
        # list comp creates list of "_" equal to word len
        self.word_guessed = ['_' for i in range(len(self.word))]
        # finds number of letters in the word
        self.num_letters= len(set(self.word))
        print(self.num_letters)
        self.num_lives = num_lives
        self.word_list= word_list
        
        #ist would be ['_', '_', '_', '_', '_']



    def check_guess(self, guess) -> None:
        '''
        Checks if the guess is in the word.
        If it is, it replaces the '_' in the word_guessed list with the guess.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The guess to be checked

        '''
        # TODO 3: Check if the guess is in the word. TIP: You can use the lower() method to convert the guess to lowercase
        # TODO 3: If the guess is in the word, replace the '_' in the word_guessed list with the guess
        # TODO 3: If the guess is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the guess is not in the word, reduce the number of lives by 1
        # Be careful! A guess can contain the same guess more than once. TIP: Take a look at the index() method in the string class
        
        if guess.lower() in word.lower():
            print(f'"Good guess! {guess} is in the word."')
        else:
            print(f'"Sorry, {guess} is not in the word. Try again."')


    def ask_for_input(self):
        '''
        Asks the user for a guess and checks two things:
        1. If the guess has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        # TODO 1: Ask the user for a guess iteratively until the user enters a valid guess
        # TODO 1: Assign the guess to a variable called `guess`
        # TODO 1: The guess has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a guess that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{guess} was already tried".
        # TODO 3: If the guess is valid, call the check_guess method

        while True:
            guess =input('Enter a single letter: ')
            # check it is one letter and alaphbetical
            if len(guess) != 1 or not guess.isalpha():
                    print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                    print("You already tried that letter!")
                    
            else:
                print(" next")
                list_of_guesses.append(guess)
                check_guess (guess)

            
       
            
word_list = ["Durian", "Orange", "Apple", "Mango", "Pineapple"]
num_lives =6
game =Hangman(word_list,num_lives)



