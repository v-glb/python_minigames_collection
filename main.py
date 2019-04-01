# Welcome to the python minigame collection!

import game_functions
import logos
import subprocess
from time import sleep

subprocess.call(['clear'])

menu = {}
menu['     #            1    >'] = "   Roll the dice               #"
menu['     #            2    >'] = "   Guess the number            #"
menu['     #            3    >'] = "   Hangman                     #"
menu['     #            0    >'] = "   Exit                        #"


def print_menu():
    logos.logoMenu()
    options = menu.keys()
    print("Welcome to the Python minigames collection! Please choose a game:\n")
    print("     ####################################################")
    print("     #                                                  #")
    for option in options:
        print(option, menu[option])
    print("     #                                                  #")
    print("     ####################################################")


def main():
    try:
        while True:
            print('\n\n')
            sleep(2)
            print_menu()
            choice = input("\n\n>> ")
            if choice == "1":
                print('\n\n')
                logos.logoRollTheDice()
                game_functions.playRollTheDice()
            elif choice == "2":
                print('\n\n')
                logos.logoGuessTheNumber()
                game_functions.playGuessTheNumber()
            elif choice == "3":
                print('\n\n')
                logos.logoHangman()
                game_functions.playHangman()
            elif choice == "0":
                print("\n\nExiting. See you next time!")
                exit()
            else:
                input("Please enter a valid choice. Enter any key to try again"
                      "...")

    except KeyboardInterrupt:
        print("\n\nAborted.")
    except ValueError:
        print("\n\nError, please check your typing and try again.")


main()
