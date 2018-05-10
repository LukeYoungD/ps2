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
def blankWord(word, length): #returns a blank string of same length + spaces
    pos = 0
    blank = []
    while pos < length:
        blank += ['_ ',]
        pos += 1
    print("blank word is", "".join(blank))
    return blank

def charBank():
    array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return array

def bankDisp(array):
    print("Your remaining letters are: ")
    for i in array:
        print i,
    return

def checkGuess(word, bank, guess, blank):
    correct = False
    if guess in bank:
        pos = 0
        for i in word:
            if guess == i:
                correct = True
                blank[pos] = guess
            pos += 1
    global guesses
    if correct == True:
        print("Correct: " + "".join(blank))
    else:
        print("Sorry, Nope: " + "".join(blank))
        guesses -= 1
    return blank

def updateBank(guess, bank):
    pos = 0
    for i in bank:
        if i == guess:
            del(bank[pos])
            return
        pos += 1
    return

def gameLoop(word, bank, blank):
    global guesses
    bankDisp(bank)
    print(" ")
    print(str(guesses) + " guesses remaining!")
    guess = raw_input("Guess a letter: ") # Error here (fixed by changing to raw_input)
    ## Check to see if guess is contained within the word
    print(" ")
    blank = checkGuess(word, bank, guess, blank)
    updateBank(guess, bank)
    

    win = (word == "".join(blank))
    if guesses == 0:
        print("you lose, it was: " + str(word))
        playAgain()
    elif win == False:
        gameLoop(word, bank, blank)
    elif win == True:
        print("You win! Well Done")
        playAgain()

def playAgain():
    again = 'n'
    again = raw_input("Would you like to play again? y/n ")
    if again == 'y':
        startGame()
    else:
        print("Bye!")
    
## Initiate Game
word = ''
guesses = 0

def startGame():
    global word
    global guesses
    print("Welcome to Hangman!")
    word = choose_word(wordlist)
    wordLength = len(word)
    guesses = (wordLength/3 + 5)
    print("The word to guess is " + str(wordLength) + " letters long.")
    bank = charBank()
    blank = blankWord(word, wordLength)

    ## print(word)
    gameLoop(word, bank, blank)

startGame()
