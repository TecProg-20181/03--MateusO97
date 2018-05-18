import random
import string
from sets import Set
import sys
import logging

WORDLIST_FILENAME = "palavras.txt"


def logConfig(log, message):
    logging.basicConfig(filename='hang.log', level=logging.INFO)

    logger = logging.getLogger('Log Message')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)

    logger.addHandler(ch)

    if log == 'debug':
        logger.debug(message)

    elif log == 'info':
        logger.info(message)

    elif log == 'warn':
        logger.warn(message)

    elif log == 'critical':
        logger.critical(message)

    else:
        logger.error(message)

def lettersNumber(word, guesses):
    differentLetters = Set(list(word))
    lettersQuantity = len(differentLetters)
    if lettersQuantity > guesses:
        loadWords()
    print "The word has: ", lettersQuantity, "different letters."

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    try:
        inFile = open(WORDLIST_FILENAME, 'r', 0)
    except IOError:
        print "Error 404 File not found!"
        logConfig('critical', 'File not found!')
        sys.exit(0)
    line = inFile.readline()
    logConfig('debug', 'File open')
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True

def getGuessedWord():
     guessed = ''
     return guessed

def getAvailableLetters(lettersGuessed):
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    print 'Available letters', str(available)

def triedLetter(letter, lettersGuessed):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Oops! You have already guessed that letter: ', guessed

def correctLetter(letter, lettersGuessed, secretWord):
    lettersGuessed.append(letter)
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Good Guess: ', guessed

def wrongLetter(letter, lettersGuessed, secretWord):
    lettersGuessed.append(letter)
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Oops! That letter is not in my word: ',  guessed

def inputLetter(guesses, lettersGuessed, secretWord):
    print 'You have ', guesses, 'guesses left.'
    getAvailableLetters(lettersGuessed)
    letter = raw_input('Please guess a letter: ')
    while letter.isalpha() == False or len(letter) != 1:
        print 'The system only allow letters'
        letter = str(raw_input('Please guess a letter'))
    if letter in lettersGuessed:
        triedLetter(letter, lettersGuessed)
    elif letter in secretWord:
        correctLetter(letter, lettersGuessed, secretWord)
    else:
        guesses -=1
        wrongLetter(letter, lettersGuessed, secretWord)
    print '------------'
    return guesses

def menu(secretWord):
            print 'Welcome to the game, Hangam!'
            print 'I am thinking of a word that is', len(secretWord), ' letters long.'
            print '-------------'

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    menu(secretWord)
    lettersQuantity = lettersNumber(secretWord, guesses)
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
            guesses = inputLetter(guesses, lettersGuessed, secretWord)
    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

secretWord = loadWords().lower()
hangman(secretWord)
