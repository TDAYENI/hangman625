from  milestone_2 import word
print(word)
#guess =input('Enter a single letter: ')
while True:
    guess =input('Enter a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word.lower():
    print(f'"Good guess! {guess} is in the word."')
else:
    print('failed')