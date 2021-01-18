"""
    Script for making functions for hangman game
    :file: hangman_functions.py
    :platform: Windows 10
    :synopsis:
        This script contains all the necessary functions
        and variables that make up the whole game.

    :author:
        Muhammad Faheem-ur-Rehman
        email: faheemlasani1034@gmail.com
"""

# importing required libraries
from colorama import init, Fore, Back, Style
import termcolor
from random import shuffle
import string


def check_word(user_letter, guess_list, memory_list, used_letters):
    """
       Function for getting combination of lists and judge that either user has put right alphabet or not

       :param string user_letter: This string contains the immediate alphabet that user has put into
       :param list guess_list: This list contains the alphabets of word that user is trying to guess
       :param list memory_list: This list first contains only asterisks. Later on it gets updated
       :param list used_letters : This list contains all alphabets that are already used by user

       :returns:  True or False depending on that the guessed letter is right or wrong respectively
       :return type: Boolean
    """
    check = False

    for letters in user_letter:
        if letters.islower():
            user_letter = user_letter.upper()
        else:
            pass

    print('{:>50}'.format(' '), end=' ')

    for i in range(len(guess_list)):
        if user_letter == guess_list[i]:
            memory_list[i] = user_letter
            check = 'True'
        else:
            pass

    for letters in memory_list:
        print(letters, end=' ')

    if check:
        termcolor.cprint('{:>40}'.format('YESS; YOU GOT RIGHT'), 'green', attrs=['bold', 'blink'], end=' ')
    else:
        termcolor.cprint('{:>40}'.format('OPPSSSS! YOU MISSED'), 'red', attrs=['bold'],  end=' ')

    termcolor.cprint('{:>40}'.format('USED LETTERS: '),'white', end=' ')
    for letters in used_letters:
        if letters.isupper():
            print(letters, end=' ')

    print('\n')

    return check


def greeting_function():
    """
       Function for printing a greeting message and instructions to play the game

       :param : none

       :returns:  None
       :return type: None
    """
    flag = True
    print('\n')
    termcolor.cprint('{:>100}'.format('*** WELCOME TO HANGMAN GAME ***'), 'yellow', attrs=['bold'])
    print('\n')
    termcolor.cprint('{:>110}'.format('<><><> LETS UNDERSTAND HOW TO PLAY THE GAME <><><>'), 'yellow', attrs=['bold'])
    print('\n')
    termcolor.cprint('This is a type of word guessing game. First you have the choice to choose\n'
                     'from four categories. After choosing your favourite one, a blank word will\n'
                     'appear on your screen to guess. You will have limited turns to guess the word.\n'
                     'If within allowed turns, you guess the word correctly, YOU WIN :-)\n'
                     'Otherwise you will be HANGED :-(\n', 'white')

    while flag:
        init()
        understood = input(Fore.MAGENTA + 'PLEASE PRESS LETTER (P) IF YOU WANT TO START THE GAME!\n' + Style.BRIGHT)
        if understood in ['P', 'p']:
            break
        else:
            termcolor.cprint('SORRY! YOU HAVE ENTERED WRONG LETTER. TRY AGAIN', 'red', attrs=['bold'])


def display_categories():
    """
       Function for displaying four categories to choose from

       :param : None

       :returns:  None
       :return type: None
    """
    print('\n')
    termcolor.cprint('YOU HAVE FOLLOWING FOUR CATEGORIES TO CHOOSE FROM:', 'white')
    termcolor.cprint('COUNTRIES    (Press 1)\nSCIENCE      (Press 2)\nFRUITS       (Press 3)\nPROFESSIONS  (Press 4)',
                     'yellow', attrs=['bold'])


def user_input():
    """
       Function for asking user to select his favourite category out of four

       :param : None

       :returns:  Selected category of user
       :return type: String
    """
    flag = True
    selected_category = str()

    while flag:
        init()
        user_category_input = input(Fore.MAGENTA + 'PLEASE SELECT YOUR CATEGORY\n' + Style.BRIGHT)
        if user_category_input == '1':
            selected_category = 'COUNTRIES'
            break
        elif user_category_input == '2':
            selected_category = 'SCIENCE'
            break
        elif user_category_input == '3':
            selected_category = 'FRUITS'
            break
        elif user_category_input == '4':
            selected_category = 'PROFESSIONS'
            break
        else:
            termcolor.cprint('\nOOPS! YOU HAVE CHOOSED OUT OF RANGE NUMBER. TRY AGAIN', 'red', attrs=['bold'])

    termcolor.cprint(f'\nGREAT! YOU HAVE CHOOSED ', 'white', end=' ')
    termcolor.cprint(f'|{selected_category}|', 'yellow', attrs=['bold'], end=' ')
    print('CATEGORY')
    return selected_category


def generate_guess_word(words_dict, category):
    """
       Function for generating the word for user to be guessed

       :param dict words_dict: This dict contains all the game data (CONFIDENTIAL)
       :param string category: This string contains the selected category of user

       :returns string guess_word: This is the word to be guessed by user
       :returns list guess_list: This list contains alphabets of word to be guessed
       :returns list memory_list: This list contains asterisks (CONFIDENTIAL)
       :return type: String and list
    """
    memory_list = []
    shuffle(words_dict[category])
    guess_word = words_dict[category].pop()
    guess_list = [letters for letters in guess_word]

    for i in range(len(guess_list)):
        memory_list.append('*')

    termcolor.cprint(f'YOUR WORD CONTAINS {len(guess_word)} ALPHABETS', 'white')
    print('{:>50}'.format(' '), end=' ')
    for i in range(len(guess_word)):
        print('*', end=' ')
    return guess_word, guess_list, memory_list


def game_starts(guess_list, memory_list):
    """
       Function where real game runs

       :param list guess_list: This list contains alphabets of word to be guessed
       :param list memory_list: This list contains asterisks (CONFIDENTIAL)


       :returns:  True or False depending on that the guessed letter is right or wrong respectively
       :return type: Boolean
    """
    total_turns = 8
    used_letters = []

    while total_turns >= 1:
        init()
        user_letter = input(Fore.MAGENTA + f'\nENTER YOUR LETTER;  {total_turns} TURN/S LEFT\n' + Style.BRIGHT)
        if (user_letter in list(string.ascii_lowercase)) or (user_letter in list(string.ascii_uppercase)):
            if user_letter in used_letters:
                termcolor.cprint('OOPS! YOU HAVE ALREADY USED THIS ALPHABET. TRY AGAIN!', 'red', attrs=['bold'])
                continue
            else:
                if user_letter.islower():
                    used_letters.append(user_letter.upper())
                    used_letters.append(user_letter)
                elif user_letter.isupper():
                    used_letters.append(user_letter.lower())
                    used_letters.append(user_letter)
        else:
            termcolor.cprint('OOPS! YOU HAVE PLACED WRONG INPUT. PLEASE ENTER AN ALPHABET!', 'red', attrs=['bold'])
            continue

        result = check_word(user_letter, guess_list, memory_list, used_letters)

        if '*' not in memory_list:
            termcolor.cprint('CONGRATULATIONS !!! YOU GUESSED THE WORD !!!', 'green', attrs=['bold', 'blink'])
            return True

        if result:
            continue
        else:
            total_turns = total_turns - 1

    if total_turns < 1:
        termcolor.cprint('OOOPS! YOU ARE OUT OF TURNS, BETTER LUCK NEXT TIME', 'red', attrs=['bold'])
        termcolor.cprint('YOUR WORD WAS:', 'white')
        print('{:>50}'.format(' '), end=' ')
        for letters in guess_list:
            termcolor.cprint(letters, 'blue', attrs=['bold'],  end=' ')
        print('\n')
        return True
