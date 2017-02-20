# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessed = True
    for character in secretWord:
        if character not in lettersGuessed:
            guessed = False
            break

    return guessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessWord = guessWord + str(letter)
        else:
            guessWord = guessWord + "_ "
    return guessWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLetters = string.ascii_lowercase
    if len(lettersGuessed) == 0:
        return allLetters
    else:
        for letters in lettersGuessed:
            allLetters = allLetters.replace(letters, '')

    return allLetters


def wordExistInList(lettersGuessed, letter, secretWord):
    if letter not in lettersGuessed:
        return False
    else:
        return getGuessedWord(secretWord, lettersGuessed)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    mistakesMade = 0
    count = len(secretWord)
    print("Welcome to the game, Hangman! ")
    print("I am thinking of a word that is " + str(count) + " letters long.")
    while mistakesMade < 8:
        print("-----------")
        print("You have " + str(8 - mistakesMade) + " guesses left")
        print("Available Letters: " + str(getAvailableLetters(lettersGuessed)))
        inputGuessedLetter = input("Please guess a letter: ")
        isLetterExist = wordExistInList(lettersGuessed, inputGuessedLetter, secretWord)
        if not isLetterExist:
            lettersGuessed.append(inputGuessedLetter)
            res = getGuessedWord(secretWord, lettersGuessed)
            if inputGuessedLetter not in secretWord:
                print("Oops! That letter is not in my word: " + str(res))
                mistakesMade += 1
            else:
                print("Good guess: " + str(res))
                guessed = isWordGuessed(secretWord, lettersGuessed)
                if guessed:
                    print("-----------")
                    print("Congratulations, you won!")
                    return
        else:
            print("Oops! You've already guessed that letter:" + str(isLetterExist))
    print("-----------")
    print("	Sorry, you ran out of guesses. The word was " + str(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
