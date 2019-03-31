import random
import os

base_path = os.path.dirname(__file__)

# Roll the dice and see what you get!


def playRollTheDice():
    while True:
        rolling = input("Let's roll the dice, shall we? y/n ")
        if rolling == 'y':
            diceSize = input('Please specify max. number of the dice: ')
            print('You got {}!'.format(random.randint(1, int(diceSize))))
        elif rolling == 'n':
            print('Thx for playing!')
            break
        else:
            print("Sorry, I didn't get that. Please try again.")


# Try to guess a random number


def playGuessTheNumber():
    maxNumber = input("Welcome to 'Guess the Number'. Please define the"
                      " highest number: ")

    numberToGuess = random.randint(0, int(maxNumber))
    correctNumber = False
    totalGuesses = 0

    while correctNumber is False:
        totalGuesses += 1
        userGuess = input("I'm thinking of a number between 0 and {}.\n"
                          "Guess a number: ".format(maxNumber))
        if int(userGuess) < numberToGuess:
            print('Your number is too low!')
        elif int(userGuess) > numberToGuess:
            print('Your number is too high!')
        elif int(userGuess) == numberToGuess:
            print('Exactly! The number is {}'.format(userGuess))
            print('You guessed the correct number in {} guesses.'
                  .format(totalGuesses))
            correctNumber = True
            print("Thanks for playing!")
        # TODO: Ask player to play again and handle invalid literals
        else:
            print("Sorry, I didn't get that. Please try again.")


# Try to guess a random word in 10 tries


def playHangman():
    rip = []

    def draw_hangman(tries):
        if tries is 9:
            rip.append('G')
            return ''.join(rip)
        elif tries is 8:
            rip.append('A')
            return ''.join(rip)
        elif tries is 7:
            rip.append('M')
            return ''.join(rip)
        elif tries is 6:
            rip.append('E')
            return ''.join(rip)
        elif tries is 5:
            rip.append(' ')
            return ''.join(rip)
        elif tries is 4:
            rip.append('O')
            return ''.join(rip)
        elif tries is 3:
            rip.append('V')
            return ''.join(rip)
        elif tries is 2:
            rip.append('E')
            return ''.join(rip)
        elif tries is 1:
            rip.append('R')
            return ''.join(rip)
        elif tries is 0:
            rip.append('!')
            return ''.join(rip)

    wordlist = os.path.join(base_path, "wordlist/german.dic")
    with open(wordlist, encoding="ISO-8859-1") as wordfile:
        words = wordfile.read().split()

    wordToGuess = random.choice(words).lower()
    hiddenWord = '_ ' * len(wordToGuess)
    guessedChars = set()
    tries = 10
    wordFound = False

    while wordFound is False and tries > 0:
        print("I'm thinking of the word {}".format(hiddenWord))
        userGuess = input("Please enter a single character: ").lower()
        if userGuess in wordToGuess:
            guessedChars.add(userGuess)
            hiddenWord = ''.join(
                [char if char in guessedChars else '_ ' for char in wordToGuess])
            if hiddenWord == wordToGuess:
                print("Exactly! The word is {}".format(wordToGuess))
                wordFound = True
        else:
            print("Character {} is not in the word.".format(userGuess))
            tries -= 1
            print("You have {} tries left.".format(tries))
            print(draw_hangman(tries))
            if tries is 0:
                print("Game over! The word was {}".format(wordToGuess))
