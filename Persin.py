
from colorama import *
import os
import time

init()

title =    Fore.MAGENTA + '''
            +----------------------------------------------------+
            |   ______ _______ ______     _   _____ ______       |
            |  (_____ (_______|_____ \   | | (_____)  ___ \      |
            |   _____) )____   _____) )   \ \   _  | |   | |     |
            |  |  ____/  ___) (_____ (     \ \ | | | |   | |     |
            |  | |    | |_____      | |_____) )| |_| |   | |     |
            |  |_|    |_______)     |_(______(_____)_|   |_|     |
            |                              by: Norah.C.IV        |
            +----------------------------------------------------+
    ''' + Style.RESET_ALL
print(title)

def displayMenu_1():
    print(Fore.WHITE + " \t\t\t        1. /chatRoom\n\t\t\t        2. /contactUs\n\t\t\t        3. /exit " + Style.RESET_ALL)

    tempName = 'UNSOURCED'
    print(Fore.MAGENTA + Back.WHITE + f"<<{tempName}>>" + Style.RESET_ALL, end = ' ')
    
    while True:
        userInput = input()
        if userInput == '1' or userInput == '/chatroom':
            '''CREATE A tempName LOGIN'''
            os.system('cls')
            print(title)
            
            tempName = 'UNSOURCED'
            print(Fore.MAGENTA + Back.WHITE + f"<<{tempName}>>" + Style.RESET_ALL, end = ' ')
            print(Fore.RED + Back.YELLOW + "[Create a tempName]" + Style.RESET_ALL, end = ' ')
            newName = input('x: ').upper()
            displayMenu_2(newName)
            
        elif userInput == '2' or userInput == '/contactus':
            '''PROVIDE A DOC WITH INFORMATION'''
            with open('persin.txt') as txt:
                print(txt.read())

            input("ENTER TO EXIT")
            os.system('cls')
            print(title)
            displayMenu_1()

        elif userInput == '3' or userInput == '/exit':
            sys.exit()
        else:
            print(f"Command [{userInput}] not recognized.")
            time.sleep(1)
            os.system('cls')
            print(title)
            displayMenu_1()


def displayMenu_2(newName):
    os.system('cls')
    print(title)
    print(Fore.MAGENTA + Back.WHITE + f"<<{newName}>>" + Style.RESET_ALL, end = ' ')

displayMenu_1()
