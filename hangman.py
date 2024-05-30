
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
    check_guess()
        Checks if the letter the player guessed is in the word or not.
    ask_for_input()
        Asks the player to guess a letter and checks if the players input is valid.
        passing a valid guess to the check_guess method.
    '''
    def __init__(self, word_list , num_lives):
        self.word= random.choice(word_list)
        # list comp creates list of "_" equal to word len
        self.word_guessed = ['_' for i in range(len(self.word))]
        # finds number of letters in the word
        self.num_letters= len(set(self.word))
        self.num_lives = num_lives
        self.word_list= word_list
        self.list_of_guesses = []

        print(f"\nThe mistery word has {self.num_letters} characters\n")
        print(f"{self.word_guessed}\n")

    def ask_for_input(self):
        '''Ask the player to guess a letter
        then checks it is 
        1. a single character 
        2. a letter.
        If both are true, it calls the check_guess method and passes the guess.
        '''

        guess =input('Enter a single letter: \n').lower()
        # check it is one letter and alaphbetical
        if len(guess) != 1 or not guess.isalpha():
                print("\nInvalid letter. Please, enter a single alphabetical character.\n")
        # check letter has not been tried 
        elif guess in self.list_of_guesses:
                self.num_lives -= 1
                print("You already tried that letter!\n")
                #Added print to remove life for extra gueses 
                print(f'You have {self.num_lives} lives left.\n')
                # added for after submission for ease of running game
                print(f'{self.word_guessed}\n')
         #Adds the guess to the list of attempted letters and checks it       
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)      
        
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
        ## Check if the guess is in the word
        if guess.lower() in self.word.lower():
            # if in word, replace '_' in word_guessed list with guessed letter
            for i, alphabet in enumerate(self.word.lower()):
                 if guess == alphabet:
                      self.word_guessed[i] = self.word[i]
            
            self.num_letters -= 1
            print(f'Good guess! {guess} is in the word.\n')
            # added for after submission for ease of running game
            print(f'{self.word_guessed}\n')

        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.\n')
            print(f'You have {self.num_lives} lives left.\n')
            # added for after submission for ease of running game
            print(f'{self.word_guessed}\n')




def play_game(word_list):
    """Runs the Hangman game

    Parameters
    ----------
    word_list: list
        List of words to be used in the Hangman game.
    """
    game = Hangman(word_list, num_lives=5)
    

    while True:
         if game.num_lives == 0:
              print(f'\nYou lost! The word was {game.word}.\n')
              break
         elif game.num_letters > 0:
              game.ask_for_input()
         elif game.num_lives != 0 and game.num_letters <=0:
              print(f'Congratulations! You won!\n')
              break
        






     
            




if __name__ == '__main__':
    from words.list_of_words import words_to_guess as word_list
    play_game(word_list)