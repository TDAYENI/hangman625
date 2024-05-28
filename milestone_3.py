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