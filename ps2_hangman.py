# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

## Functions:
def charBank():
    array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return array

def bankDisp(array):
    print("Your remaining letters are: ")
    for i in array:
        print i,
    return
def checkGuess(word, bank, guess):
    positions = []
    if guess in bank:
        for i in word:
            if guess == i:
                positions = positions + [guess,]
    print positions
    return positions

def gameLoop(word, bank):
    bankDisp(charBank)
    print(" ")
    guess = input("Guess a letter: ") # Error here
    ## Check to see if guess is contained within the word
    checkGuess(word, bank, guess)
    
## Initiate Game
print("Welcome to Hangman!")
word = choose_word(wordlist)
wordLength = len(word)
guesses = (wordLength/3 + 5)
print("The word to guess is " + str(wordLength) + " letters long.")
charBank = charBank()

gameLoop(word, charBank)
