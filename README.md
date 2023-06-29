# TIC-TAC-TOE

## <center>This is my first project on python. And in this project I will be creating a Tic Tac Toe game using user-defined functions. 

## Let me walk you through the entire project.</center>



### Function that print outs the board.
```python
from IPython.display import clear_output # To clear the screen between moves.

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
```

### Function that takes in a player input and assigns their marker as 'X' or 'O'.
```python
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
```

### Function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
```python
def place_marker(board, marker, position):
    board[position] = marker
```

### Function that takes in a board and a mark (X or O) and then checks to see if that mark has won. 
```python
def win_check(board, mark):
    return board[7] == board[8] == board[9] == mark or board[7] == board[4] == board[1] == mark or board[7] == board[5] == board[3] == mark or board[8] == board[5] == board[2] == mark or board[9] == board[5] == board[1] == mark or board[9] == board[6] == board[3] == mark
```

### Function that uses the random module to randomly decide which player goes first.
```python
import random
play = ['Player 1','Player 2']
def choose_first():
    flip = random.randint(0, 1)
    return play[flip]
```

### Function that returns a boolean indicating whether a space on the board is freely available.
```python
def space_check(board, position):
    return board[position] == ' '
```

### Function that checks if the board is full and returns a boolean value. 
```python
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
```

### Function that asks for a player's next position (as a number 1-9) and then uses the function from one of the previous steps to check if it's a free position. If it is, then return the position for later use.
```python
def player_choice(board):
    position = 0
    while position not in [i for i in range(1, 10)] or not space_check(board, position):
        position = int(input("Enter the player position (1-9) :"))
    return position
```

### Function that asks the player if they want to play again and returns a boolean True if they do want to play again.
```python
def replay():
    choice = ['Y', 'N']
    while True:
        re = input("Do you want to play again ('Y' or 'N')? ").upper()
        if re not in choice:
            print("Please enter either 'Y or 'N'!")
        else:
            break
    return re == 'Y'
```

### The Game!
```python
print('Welcome to Tic Tac Toe!')
tboard = [' ']*10
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

```
