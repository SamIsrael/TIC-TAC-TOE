from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    print("Player 1")
    while True:
        marker = input("Do you want to be 'X' or 'O' ? ").upper()
        if marker == 'X' or marker == 'O':
            break
        else:
            print("Please enter either 'X' or 'Y' ")
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print("Player 2 will be " + player2)
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return board[7] == board[8] == board[9] == mark or board[7] == board[4] == board[1] == mark or board[7] == board[
        5] == board[3] == mark or board[8] == board[5] == board[2] == mark or board[9] == board[5] == board[
        1] == mark or board[9] == board[6] == board[3] == mark


import random

play = ['Player 1', 'Player 2']


def choose_first():
    flip = random.randint(0, 1)
    return play[flip]


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [i for i in range(1, 10)] or not space_check(board, position):
        position = int(input("Enter the player position (1-9) :"))
    return position


def replay():
    choice = ['Y', 'N']
    while True:
        re = input("Do you want to play again ('Y' or 'N')? ").upper()
        if re not in choice:
            print("Please enter either 'Y or 'N'!")
        else:
            break
    return re == 'Y'


print('Welcome to Tic Tac Toe!')
tboard = [' '] * 10
while True:
    tboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    ready = input("ARE YOU READY ?? (Enter either 'y' or 'n'): ")
    game_on = ready == 'y'

    while game_on:
        if turn == 'Player 1':
            display_board(tboard)
            position = player_choice(tboard)
            place_marker(tboard, player1_marker, position)

            if win_check(tboard, player1_marker):

                display_board(tboard)
                print("PLAYER 1 HAS WONN !!!!")
                game_on = False

            else:

                if full_board_check(tboard):
                    display_board(tboard)
                    print("Uh oh!! It's a tie!!")
                    game_on = False

                else:
                    turn = 'Player 2'

        else:
            display_board(tboard)
            position = player_choice(tboard)
            place_marker(tboard, player2_marker, position)

            if win_check(tboard, player2_marker):

                display_board(tboard)
                print("PLAYER 2 HAS WONN !!!!")
                game_on = False

            else:

                if full_board_check(tboard):
                    display_board(tboard)
                    print("Uh oh!! It's a tie!!")
                    game_on = False

                else:
                    turn = 'Player 1'

    if not replay():
        print("That was fun!!")
        break
