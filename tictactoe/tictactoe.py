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
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Count X and O
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # Check if X is equal to O in order to calculate wich one will be next
    if x_count == o_count:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    # iterate on each cell in order to discover if they are empty
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    i, j = action

    # Verify if the acion is in the table
    if i not in range(3) or j not in range(3):
        raise Exception("Ação fora dos limites!")

    # Verify if the cell is in the table
    if board[i][j] != EMPTY:
        raise Exception("Ação inválida, célula já ocupada!")

    # Make a copy of the table
    new_board = copy.deepcopy(board)

    # Gets the player who is in his turn
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    # VVerify Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Verify diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # If no one wins
    return None


def terminal(board):
    # If someone wins, game is over
    if winner(board) is not None:
        return True

    # if there is a possible action, game continues
    for row in board:
        if EMPTY in row:
            return False

    # else, its a draw
    return True


def utility(board):
    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0


def minimax(board):
    # If the game is over, there is no possible actions to take
    if terminal(board):
        return None

    current_player = player(board)

    # Auxiliar funtion to maximize the value
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -float("inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    # Função auxiliar para minimizar o valor
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    # If its the "x" player turn, maximize the value
    if current_player == "X":
        best_value = -float("inf")
        best_action = None
        for action in actions(board):
            action_value = min_value(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_action = action
        return best_action

    # If its the "O" player, minimize the value
    else:
        best_value = float("inf")
        best_action = None
        for action in actions(board):
            action_value = max_value(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_action = action
        return best_action
