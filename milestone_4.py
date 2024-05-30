import random
word_list = ["Durian", "Orange", "Apple", "Mango", "Pineapple"]

class Hangman :

    def __init__(self, word_list,num_lives = 5):
        self.word_list = word_list 
        self.word_guessed = []
        self.num_letters=0
        self.num_lives = num_lives
        self.word= random.choice(word_list)
        #ist would be ['_', '_', '_', '_', '_']
       
        
        self.num_lives= 0
        self.list_of_guesses = []

    def ask_letter(self):  
        pass

    def play_game(word_list):
        pass


def check_guess (guess):
    if guess.lower() in word.lower():
        print(f'"Good guess! {guess} is in the word."')
    else:
        print(f'"Sorry, {guess} is not in the word. Try again."')
    


def ask_for_input():
    list_of_guesses =['p']
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

            
       
      
            
   



list_of_guesses =['p']

word = "Durian"


ask_for_input()