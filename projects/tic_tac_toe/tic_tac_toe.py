# Tic Tac Toe Game

import game_functions

again_play = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

game_functions.greeting_function(board)

while again_play:
    first_player_symbol, second_player_symbol = game_functions.players_symbol()
    game_rule = game_functions.game_rules()
    result = game_functions.game_on(board, first_player_symbol, second_player_symbol)

    print('\n')
    answer = input('DO YOU WANT OT PLAY AGAIN? (y/n)')
    if answer in ['y', 'Y']:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        pass
    elif answer in ['n', 'N']:
        print('                                   ******************* GOOD BYE******************')
        again_play = False
