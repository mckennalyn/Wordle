# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    def display_solution_word(window, solution_word):
        for col in range(N_COLS):
            window.set_square_letter(0, col, solution_word[col])

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Choose a random word from the dictionary
    solution_word = random.choice(FIVE_LETTER_WORDS)

    # Display the solution word in the first row of the window
    display_solution_word(gw, solution_word)

# Startup code

if __name__ == "__main__":
    wordle()

