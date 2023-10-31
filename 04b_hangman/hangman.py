# Hangman Game by Kristopher Cooper, v0.1
import random
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

# Pick Word form List
def getRandomWord(wordList): # Return a random word from the list
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

    def displayBoard(missedLetters, correctLetters, secretWord):
        print(HANGMAN_BOARD[len(missedLetters)])
        print()

        print('Missed Letters:', end = '')
    print()
    #FINISH THURSDAY

# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1