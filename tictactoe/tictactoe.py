"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0
    for i in range(len(board)):
        for j in range(0, len(board)):
            if board[i][j] == X:
                xCounter += 1
            if board[i][j] == O:
                oCounter += 1
    
    if xCounter == initial_state():
        return X
    elif xCounter != oCounter:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == None:
                moves.add((i,j))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultBoard = copy.deepcopy(board)
    resultBoard[action[0]][action[1]] = player(board)
    return resultBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
       if board[i][0] == board[i][1] == board[i][2]:
           return board[i][0]
    for j in range(len(board)):
       if board[0][j] == board[1][j] == board[2][j]:
           return board[0][j]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True
        
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = maxvalue(board)
            return move
        else:
            value, move = minvalue(board)
            return move

def minvalue(board):
    if terminal(board):
        return utility(board), None

    move = None
    value = math.inf

    for action in actions(board):
        v, mov = maxvalue(result(board,action))
        if v < value:
            value = v
            move = action
    return value, move

def maxvalue(board):
    if terminal(board):
        return utility(board), None

    move = None
    value = -math.inf

    for action in actions(board):
        v, mov = minvalue(result(board,action))
        if v > value:
            value = v
            move = action
    return value, move



