#Hangman Game
#Logan Nelson
#11/26/18
#The classic game of Hangm an. The computer picks a random word
#and the player has to guess it, one letter at a time. If the player
#can't guess the word in time, the little stick figure gets hanged.

#imports
import random
import time

#constants
HANGMAN = (
"""
   -----
   |     |
   |
   |
   |
   |
   |
   -------
   """,
"""
   -----
   |     |
   |    O
   |
   |
   |
   |
   -------
   """,
"""
   -----
   |     |
   |    O
   |     |
   |     |
   |
   |
   -------
   """,
"""
   -----
   |     |
   |    O
   |   \\|/
   |     |
   |
   |
   -------
   """,
"""
   -----
   |     |
   |    O
   |   \\|/
   |     |
   |    /
   |
   -------
   """,
"""
   -----
   |     |
   |    O
   |   \\|/
   |     |
   |    /\\
   |
   -------
   """,
"""
   -----
   |     |
   |    O
   |   \\|/
   |     |
   |  _/\\_
   |
   -------
   """,
"""
   -------
   |     |
   |    /|\\
   |  \\O /
   |   \\|/
   |     |
   |  _/\\_
   |
   -------
   """)
MAX_WRONG=len(HANGMAN)-1
WORDS = ()

for i in range(len(HANGMAN)):
    print(HANGMAN[i])
    time.sleep(5)

