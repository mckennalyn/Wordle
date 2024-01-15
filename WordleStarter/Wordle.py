# File: Wordle.py

"""
Group 3-14
Hailey Bronson, McKenna Alder, Brian Stone, Alden Transfiguracion

This module contains the logic for the World game.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        # Converts the input string to uppercase for consistency
        word = s.upper()

        # Checks if the word is in the list of valid words
        # First converts back to lowercase to validate whether it's in word list
        word = s.lower()
        if word in FIVE_LETTER_WORDS:
            gw.show_message("Correct! The word is valid.")
        else:
            gw.show_message("Not in word list")


    def display_solution_word(window, solution_word):
        for col in range(N_COLS):
            window.set_square_letter(0, col, solution_word[col].upper())

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Chooses a random word from the dictionary
    solution_word = random.choice(FIVE_LETTER_WORDS)

    # Displays the solution word in the first row of the window
    display_solution_word(gw, solution_word)

# Startup code

if __name__ == "__main__":
    wordle()

