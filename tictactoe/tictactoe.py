"""
Tic Tac Toe Player with Minimax Optimization
"""

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
    # Count X's and O's to determine the next player
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    """
    Returns a set of all possible actions (i, j) available on the board.
    """
    return {(i, j)
            for i in range(3)
            for j in range(3)
            if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action: Cell is not empty.")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game if there is one.
    """
    lines = (
        # Horizontal
        board[0], board[1], board[2],
        # Vertical
        [board[i][0] for i in range(3)],
        [board[i][1] for i in range(3)],
        [board[i][2] for i in range(3)],
        # Diagonals
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    )
    for line in lines:
        if line.count(line[0]) == 3 and line[0] is not EMPTY:
            return line[0]
    return None

def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    return winner(board) is not None or not any(EMPTY in row for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Implements alpha-beta pruning for optimization.
    """
    current_player = player(board)

    if terminal(board):
        return None

    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = float('-inf')
        best_action = None
        for action in actions(board):
            min_v, _ = min_value(result(board, action), alpha, beta)
            if min_v > v:
                v = min_v
                best_action = action
                alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v, best_action

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = float('inf')
        best_action = None
        for action in actions(board):
            max_v, _ = max_value(result(board, action), alpha, beta)
            if max_v < v:
                v = max_v
                best_action = action
                beta = min(beta, v)
            if alpha >= beta:
                break
        return v, best_action

    if current_player == X:
        _, action = max_value(board, float('-inf'), float('inf'))
    else:
        _, action = min_value(board, float('-inf'), float('inf'))
    return action

