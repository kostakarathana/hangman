# HANGMAN

## Premise 

The idea here is to play around with algorithms to build a system that can beat hangman every time with any of the ~500000 words in the english language. 

## Definitions

**Hangman** is defined as a game where a random word is selected and the 'player' must successfully guess the word within 7 attempts. 

## Ideas

Algorithmic approach: Find a recursive algorithm that just logically removes words after each guess. In hangman you are also allowed to see the length of the word, so that instantly removes a large number of words.

## Log

- I/O was incredibly slow. 

- Diagnosing with time module