# Imports ---------------

from guizero import App, Box, PushButton, Text

# Functions -------------
def clear_board():
    new_board = [[None, None, None],
                [None, None, None],
                [None, None, None]]
    for x in range(3):
        for y in range(3):
            button = PushButton(
                board, 
                text="", 
                grid=[x, y], 
                width=3, 
                command=chooseSquare, 
                args=[x, y])
            new_board[x][y] = button
    return new_board

def chooseSquare(x, y):
    boardSquares[x][y].text = turn
    # Squares can only be chosen first
    boardSquares[x][y].disable()
    toggle_player()
    checkWin()

def toggle_player():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    message.value = "It is your turn, " + turn

def check_win():
    winner = None
    # Vertical lines
    if (
        board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text
        ) and board_squares[0][2].text in ["X", "O"]:
            winner = board_squares[0][0]
    elif (
        board_squares[1][0].text == board_squares[1][1].text ==
        board_squares[1][2].text
        ) and board_squares[1][2].text in ["X", "O"]:
            winner = board_squares[1][0]
    elif (
        board_squares[2][0].text == board_squares[2][1].text ==
        board_squares[2][2].text
        ) and board_squares[2][2].text in ["X", "O"]:
            winner = board_squares[2][0]
    # Horizontal lines
    elif (
        board_squares[0][0].text == board_squares[1][0].text ==
        board_squares[2][0].text
        ) and board_squares[2][0].text in ["X", "O"]:
            winner = board_squares[0][0]
    elif (
        board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text) and board_squares[2][1].text in ["X", "O"]:
            winner = board_squares[0][1]
    elif (
        board_squares[0][2].text == board_squares[1][2].text ==
        board_squares[2][2].text
        ) and board_squares[2][2].text in ["X", "O"]:
            winner = board_squares[0][2]
    # Diagonals
    elif (
        board_squares[0][0].text == board_squares[1][1].text ==
        board_squares[2][2].text
        ) and board_squares[2][2].text in ["X", "O"]:
            winner = board_squares[0][0]
    elif (
        board_squares[2][0].text == board_squares[1][1].text ==
        board_squares[0][2].text
        ) and board_squares[0][2].text in ["X", "O"]:
            winner = board_squares[0][2]

    if winner is not None:
        message.value = winner.text + " wins!"
    elif moves_taken() == 9:
        message.value = "It's a draw"
# Variables -------------
turn = 'X'

# App -------------------

app = App("Tic tac toe")

board = Box(app, layout='grid')
boardSquares = clear_board()
message = Text(app, text='It is your turn, ' + turn) 

app.display()
