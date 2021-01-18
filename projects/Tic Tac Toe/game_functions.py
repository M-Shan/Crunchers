"""
    This script involves all the functions that make up
    the tic tac toe game
    :file: game_functions.py
    :platform: windows 10
    :synopsis:
        Script containing common variables and functions
    :author:
        Muhammad Faheem ur Rehman
        email: faheemlasani1034@gmail.com
"""


def scan_result(index_1, index_2, index_3, board, first_player_symbol, second_player_symbol):
    """
       Function for getting three indices of the tic tac toe board along with player symbols

       :param string index_1 and index_2 and index_3 : Three indices that contain the user defined symbols
       :param list board: List that conatains all the indices of tic tac toe game
       :param string first_player_symbol and second_player_symbol: Contains player symbols defined at the start of game

       :returns:  True if the three indices are equal
       :return type: Boolean
    """

    if (index_1 == index_2 == index_3) and (index_1.lower() == first_player_symbol):
        print('CONGRATULATIONS PLAYER 1; YOU WON !!!')
        print('\n')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[0], board[1], board[2]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[3], board[4], board[5]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[6], board[7], board[8]))

        return True
    elif (index_1 == index_2 == index_3) and (index_1.upper() == second_player_symbol):
        print('CONGRATULATIONS PLAYER 2; YOU WON !!!')
        print('\n')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[0], board[1], board[2]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[3], board[4], board[5]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[6], board[7], board[8]))

        return True

    else:
        pass


def make_decision(board, first_player_symbol, second_player_symbol):
    """
       Function for checking the game result

       :param list board: List that contains all the indices of tic tac toe game
       :param string first_player_symbol and second_player_symbol: Contains player symbols defined at the start of game

       :returns:  Variable result in case that all indices are equal
       :return type: Boolean
    """

    combination_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (2, 5, 8), (1, 4, 7), (0, 4, 8), (2, 4, 6)]

    for combos in combination_list:
        result = scan_result(board[combos[0]], board[combos[1]], board[combos[2]], board, first_player_symbol,
                             second_player_symbol)
        if result:
            return result
        else:
            pass

    return False


def greeting_function(board):
    """
             Function for displaying the tic tac toe board

             :param list board: List that contains all the indices of tic tac toe game

             :returns:  None
             :return type: None
          """
    print('                                                             ***WELCOME TO THE TIC TOE GAME***')
    print('\n')
    print('                                                          |           |', '           |', '           |')
    print('                                                        ---------------------------------------------')
    print('                                                          |           |', '           |', '           |')
    print('                                                        ---------------------------------------------')
    print('                                                          |           |', '           |', '           |')
    print('\n')


def players_symbol():
    """
              Function for asking players to select their symbols

              :param : None

              :returns:  Player selected symbols
              :return type: string
           """
    symbol_one = str()
    symbol_two = str()
    symbol = True
    print('You are player 1. ')

    while symbol:
        symbol_one = input('Please select a symbol: {X or O}')
        if symbol_one == 'X' or symbol_one == 'x':
            symbol_two = 'O'
            symbol = False
        elif symbol_one == 'O' or symbol_one == 'o':
            symbol_two = 'X'
            symbol = False
        elif symbol_one not in ['X', 'O', 'x', 'o']:
            print('Sorry player 1. You have choosed wrong symbol. Please try again!')

    print('Player 1 : Symbol {}'.format(symbol_one.upper()))
    print('Player 2 : Symbol {}'.format(symbol_two))

    return symbol_one, symbol_two


def game_rules():
    """
    Function for displaying the game rules

    :param : None

    :returns:  None
    """
    key = False
    print('\n')
    print('                                                             ***Lets read the instructions of the game***')
    print('\n')
    print('The game will run turn by turn. Both players will mark their respective symbols \n'
          'on the Tic Tac Toe board. To mark the symbols, you will use the numpad of your \n'
          'keyboard. See the below figure to ensure how to use the board.')
    print('\n')
    print('                                                           |     7     |     8     |     9     |')
    print('                                                         -------------------------------------------')
    print('                                                           |     4     |     5     |     6     |')
    print('                                                         -------------------------------------------')
    print('                                                           |     1     |     2     |     3     |')
    print('\n')
    print('Each player has to mark his/her symbols in same row, column or cross \n'
          'in order to make a pack of three. The player who performs this task \n'
          'first will win the game. To have an example of a winning case, look \n'
          'below figure')
    print('\n')
    print('                                                           |     X     |           |           |')
    print('                                                         -------------------------------------------')
    print('                                                           |           |     X     |           |')
    print('                                                         -------------------------------------------')
    print('                                                           |           |           |      X    |')

    user_pass = input('If you have read all the instructions, Please enter letter ''p'' to start the game')

    while not key:
        if user_pass == 'p' or user_pass == 'P':
            key = True
        else:
            user_pass = input('Sorry! You have entered a wrong letter. Please enter letter p again')


def game_on(board, first_player_symbol, second_player_symbol):
    """
           Function for starting the game

           :param : None

           :returns:  Game result
           :return type: Boolean
        """
    flag = True
    player1_key = True
    player2_key = True
    key_1 = False
    key_2 = False
    key_3 = False
    key_4 = False
    key_5 = False
    key_6 = False
    key_7 = False
    key_8 = False
    key_9 = False
    count = int(1)
    player_one_number = int()
    player_two_number = int()
    print('\n')
    print('                                                             ***Lets Start!***')
    while flag:
        while player1_key:
            player_one_number = int(input('Player 1: Enter your symbol location {} from (1-9) '.format(count)))
            if player_one_number not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('PLAYER 1 You have choosed out of range location. Please try again.')
                continue

            if player_one_number == 1:
                key_1 = True
                if board[6] == ' ':
                    board[6] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 2:
                key_2 = True
                if board[7] == ' ':
                    board[7] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 3:
                key_3 = True
                if board[8] == ' ':
                    board[8] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 4:
                key_4 = True
                if board[3] == ' ':
                    board[3] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 5:
                key_5 = True
                if board[4] == ' ':
                    board[4] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 6:
                key_6 = True
                if board[5] == ' ':
                    board[5] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 7:
                key_7 = True
                if board[0] == ' ':
                    board[0] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 8:
                key_8 = True
                if board[1] == ' ':
                    board[1] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            elif player_one_number == 9:
                key_9 = True
                if board[2] == ' ':
                    board[2] = first_player_symbol.upper()
                    player1_key = False
                else:
                    print('Sorry! This location has already been occupied by Player 2')
                    continue
            else:
                pass

        player1_key = True
        if count >= 3:
            result = make_decision(board, first_player_symbol, second_player_symbol)
            if result:
                return result
            else:
                pass

        print('\n')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[0], board[1], board[2]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[3], board[4], board[5]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[6], board[7], board[8]))

        while player2_key:
            player_two_number = int(input('Player 2: Enter your symbol location {} from (1-9) '.format(count)))

            if player_two_number not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('PLAYER 2 You have choosed out of range location. Please try again.')
                continue

            if player_two_number == 1:
                if key_1:
                    print('Sorry! This location has already been occupied by Player by 1')
                    continue
                else:
                    board[6] = second_player_symbol
                    player2_key = False
            elif player_two_number == 2:
                if key_2:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[7] = second_player_symbol
                    player2_key = False
            elif player_two_number == 3:
                if key_3:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[8] = second_player_symbol
                    player2_key = False
            elif player_two_number == 4:
                if key_4:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[3] = second_player_symbol
                    player2_key = False
            elif player_two_number == 5:
                if key_5:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[4] = second_player_symbol
                    player2_key = False
            elif player_two_number == 6:
                if key_6:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[5] = second_player_symbol
                    player2_key = False
            elif player_two_number == 7:
                if key_7:
                    print('Sorry! This location has already been occupied Player 1')
                    continue
                else:
                    board[0] = second_player_symbol
                    player2_key = False
            elif player_two_number == 8:
                if key_8:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[1] = second_player_symbol
                    player2_key = False
            elif player_two_number == 9:
                if key_9:
                    print('Sorry! This location has already been occupied Player by 1')
                    continue
                else:
                    board[2] = second_player_symbol
                    player2_key = False
            else:
                pass

        player2_key = True
        if count >= 3:
            result = make_decision(board, first_player_symbol, second_player_symbol)
            if result:
                return result
            else:
                pass

        print('\n')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[0], board[1], board[2]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[3], board[4], board[5]))
        print('                                                          --------------------------------------------')
        print(
            '                                                              |     {}     |     {}     |     {}     |'.format(
                board[6], board[7], board[8]))

        count = count + 1

        if count > 4 and not result:
            print('MATCH DRAW !!!')
            return result
        else:
            pass
