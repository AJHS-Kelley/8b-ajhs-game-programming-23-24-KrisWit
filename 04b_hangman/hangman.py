# Hangman Game by Kristopher Cooper, v0.1

words = 'snake bird fish bat cat rat cow games flow data control man van band spring summer winter fall hang visual people react raise bell king queen apple pat fat chesse'.split()
print(words)
# VARIABLE_NAME in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
      +---+
          |           
          |      
          |
        ======''','''
      +---+
      O   |           
          |      
          |
        ======''','''
      +---+
      O   |           
      |   |      
          |
        ======''','''
      +---+
      O   |           
     /|   |      
          |
        ======''','''
      +---+
      O   |           
     /|\  |      
          |
        ======''','''
      +---+
      O   |           
     /|\  |      
     /    |
        ======''','''
      +---+
      O   |           
     /|\  |      
     / \  |
        ======''']

i = 0
while i < len(HANGMAN_BOARD):
    print (HANGMAN_BOARD[i])
    i += 1
    