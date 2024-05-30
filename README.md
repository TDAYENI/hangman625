# Hangman
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game in python, where the computer thinks of a word and the user tries to guess it. 
## Features
- Random word selection from a predefined list.
- Tracks the number of lives the player has.
- Prevents player from repeating the same guess twice
- Notifies the player of a win or loss
## Requirements

  * Python 3.12 (Random module built into python)



## Installation 
1. Clone this repo (for help on cloning repos see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).

[Copy this link](https://github.com/TDAYENI/hangman625.git) and paste in your repo

1. Run the `hangman.py` file. Bash comman below.
```bash
python hangman.py
```
2. You will be prompted with a mystery word represented by underscores (_).
3. Enter a single letter as your guess.
4. If the letter is in the word, it will be revealed in its correct position(s). Otherwise, you will lose a life.
5. Keep guessing letters until you either guess the word or run out of lives.

## Features

- Randomly selects a word from a predefined list.
- Keeps track of the number of lives remaining.
- Prevents the player from guessing the same letter multiple times.
- Notifies the player of the outcome (win or lose) at the end of the game.



`__init__ `method  picks a random word from a list, sets your number of lives and keeps track of the letters the user has guessed

## Attributes

* `word` : String - stores word user needs to guess
* `word_guessed`: list - keeps track of letters guessed by user. Starts as underscores (_) replaced by correct guess.
e.g   (_ _ _) would repesent a three letter word like DOG. if the user guessed the letter D then word_guessed would be (D _ _)
* `num_letters`: int- Stores number of letters in the word
* `num_lives`: int - Tracks lives/attempts user has
* `list_letters`: list:- Remembers letters the user has guessed

## Methods
* `check_guess`: Checks if the letter the user inputs is in the word. If it is true it displays the letter in the word if it is isn't a life is removed.
* `ask_for_input`: Prompts user for 1 letter checking the condtions are met then calls `check_guess` method

## Acknowledgements
AiCore
