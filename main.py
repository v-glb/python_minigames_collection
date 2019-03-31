# Welcome to the python minigame collection!

import game_functions
import logos
import subprocess

subprocess.call(['clear'])

menu = {}
menu['1 >'] = "Roll the dice"
menu['2 >'] = "Guess the number"
menu['3 >'] = "Hangman\n"
menu['0 >'] = "Exit"


def print_menu():
    logos.logoMenu()
    options = menu.keys()
    print("Welcome to the Python minigames collection! Please choose a game:\n")
    for option in options:
        print(option, menu[option])


def main():
    while True:
        print('\n\n')
        print_menu()
        choice = input(">> ")
        try:
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
                print("Exiting.")
                exit()
            else:
                input("Please enter a valid choice. Enter any key to try again"
                      "...")

        except KeyboardInterrupt:
            print("\n\nAborted.")
            break


main()
