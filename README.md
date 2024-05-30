# Hangman
## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

To do list
Project Title
## Requirements

  * Python 3.12
## Table of Contents
 if the README file is long
A description of the project: what it does, the aim of the project, and what you learned
Installation instructions

## Instructions
1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).

Run milestone_2.py to choose a random word from the provided list of words.
Run milestone_3.py and enter a single letter to guess if it is in the selected word.

## Usage instructions
random module 

File structure of the project
currently 2 files 
License information


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