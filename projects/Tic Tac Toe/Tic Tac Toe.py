"""
    Script for making Tic Tac Toe game
    :file: Tic Tac Toe.py
    :platform: Windows 10
    :synopsis:
        This script first call initial functions that takes several
        inputs from the two players e.g. their symbols to play and
        understanding of game instructions. After that the real game
        begins. Each player marks his/her symbol turn by turn on the
        tic tac toe board. When any of the player marks his three
        consecutive symbol either in a row, column or cross,
        he/she wins.

    :author:
        Muhammad Faheem-ur-Rehman
        email: faheemlasani1034@gmail.com
"""

import game_functions


def main():
    """
        main function
    """
    key = True
    again_play = True
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    game_functions.greeting_function(board)

    while again_play:

        #calling function that decides each player symbol
        first_player_symbol, second_player_symbol = game_functions.players_symbol()

        #calling function that display game instructions
        game_rule = game_functions.game_rules()

        #calling main function to start the game
        result = game_functions.game_on(board, first_player_symbol, second_player_symbol)

        print('\n')

        #asking user weather he/she wants to play again or not
        while key:
            answer = input('DO YOU WANT TO PLAY AGAIN? (y/n)')
            if answer in ['y', 'Y']:
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                break
            elif answer in ['n', 'N']:
                print('                                   ******************* GOOD BYE******************')
                again_play = False
                break
            else:
                print('\nSorry, you have put wrong input. Please try again!')


if __name__ == '__main__':
    main()
