# Hangman
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Acknowledgements](#acknowledgements)


## Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game in python, where the computer thinks of a word and the user tries to guess it. 
## Features
- Random word selection from a predefined list.
- Tracks the number of lives the player has.
- Prevents player from repeating the same guess twice.
- Notifies the player of a win or loss.
## Requirements

  * Python 3.12 (Random module built into python)



## Installation 
1. Clone this repo (for help on cloning repos see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).

[Copy this link](https://github.com/TDAYENI/hangman625.git) and paste in your terminal
```git clone < insert link> ```

1. Run the `hangman.py` file. Bash comman below.
```bash
python hangman.py
```
2. You will be prompted with a mystery word represented by underscores (_).
3. Enter a single letter as your guess.
4. If the letter is in the word, it will be revealed in its correct position(s). Otherwise, you will lose a life.
5. Keep guessing letters until you either guess the word or run out of lives.




## Acknowledgements
AiCore
