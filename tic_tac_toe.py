from collections import deque
from graph import *


class TicTacToe:
    """
    TicTacToe class represents all possible situations in a game of TicTacToe
    """
    def __init__(self):
        self.graph = Graph()

    def legal_moves_x(self, board):
        """
        Function that returns all the legal moves for X
        :returns: List of valid moves
        """
        retVal = []

        # If either of X or O has won we don't need to proceed further as the game is over
        if self.has_x_won(board):
            return retVal
        if self.has_o_won(board):
            return retVal

        # Otherwise go on find all the possible moves
        # Insert X at every possible position
        # Also make sure the difference between number of X's ans O's is either 0 or 1
        for i in range(len(board)):
            if board[i] == " ":
                tmp = board[0:i] + "X" + board[i+1:]
                if tmp.count("X") - tmp.count("O") == 0 or tmp.count("X") - tmp.count("O") == 1:
                    retVal.append(tmp)
        return retVal

    def legal_moves_o(self, board):
        """
        Function that returns all the legal moves for X
        :returns: List of valid moves
        """
        retVal = []

        # If either of X or O has won we don't need to proceed further as the game is over
        if self.has_x_won(board):
            return retVal
        if self.has_o_won(board):
            return retVal

        # Otherwise go on find all the possible moves
        # Insert X at every possible position
        # Also make sure the difference between number of X's ans O's is either 0 or 1
        for i in range(len(board)):
            if board[i] == " ":
                tmp = board[0:i] + "O" + board[i+1:]
                if tmp.count("X") - tmp.count("O") == 0 or tmp.count("X") - tmp.count("O") == 1:
                    retVal.append(tmp)
        return retVal

    def has_x_won(self, board):
        """
        Function that returns True if X won, otherwise False
        """
        win = False

        # Check if first row is all X's, if so return True
        f = True
        for i in range(3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if second row is all X's, if so return True
        f = True
        for i in range(3, 6):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if third row is all X's, if so return True
        f = True
        for i in range(6, 9):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if first column is all X's, if so return True
        f = True
        for i in range(0, 9, 3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if second column is all X's, if so return True
        f = True
        for i in range(1, 9, 3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if third column is all X's, if so return True
        f = True
        for i in range(2, 9, 3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if the leading diagonal is all X's, if so return True
        f = True
        for i in range(0, 9, 4):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if the trailing diagonal is all X's, if so return True
        f = True
        for i in range(2, 7, 2):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

    def has_o_won(self, board):
        """
        Function that returns True if O won, otherwise False
        """
        win = False

        # Check if first row is all X's, if so return True
        f = True
        for i in range(3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if second row is all X's, if so return True
        f = True
        for i in range(3, 6):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if third row is all X's, if so return True
        f = True
        for i in range(6, 9):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if first column is all X's, if so return True
        f = True
        for i in range(0, 9, 3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if second column is all X's, if so return True
        f = True
        for i in range(1, 9, 3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if third column is all X's, if so return True
        f = True
        for i in range(2, 9, 3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if leading diagonal is all X's, if so return True
        f = True
        for i in range(0, 9, 4):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        # Check if trailing diagonal is all X's, if so return True
        f = True
        for i in range(2, 7, 2):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

    def is_tied(self, board):
        """
        Function that returns True if board is tied, otherwise False
        """
        if not self.has_x_won(board) and not self.has_o_won(board):
            return True
        else:
            return False


def simulate():
    """
    Function that creates a TicTacToe object and simulates the game
    :return: None
    """

    # Initialization
    win_for_x = 0
    win_for_o = 0
    full_board_tie = 0
    legal_boards = 0

    # Start the game with an empty board
    game = TicTacToe()
    start_pos = "         "
    start_v = game.graph.addVertex(start_pos)

    # Create a FIFO queue and add the starting vertex to it
    queue = deque()
    queue.append(start_v)

    # While the queue in not empty visit all the vertices in the queue one by one
    while queue:
        u = queue.popleft()
        legal_boards += 1

        # Increment the appropriate value based upon whether X won/O won/tie
        if game.has_x_won(u.id):
            win_for_x += 1
        elif game.has_o_won(u.id):
            win_for_o += 1
        elif game.is_tied(u.id) and not " " in u.id:
            # If it's a tie and there's no empty space in the string, which means it's a full board, increment the value
            full_board_tie += 1

        # Get the possible moves for X from this position and append them to the queue if they are not seen before
        possible_moves = game.legal_moves_x(u.id)
        for move in possible_moves:
            if move not in game.graph:
                v = game.graph.addVertex(move)
                game.graph.addEdge(u, v, 1)
                queue.append(v)

        # Get the possible moves for X from this position and append them to the queue if they are not seen before
        possible_moves = game.legal_moves_o(u.id)
        for move in possible_moves:
            if move not in game.graph:
                v = game.graph.addVertex(move)
                game.graph.addEdge(u, v, 1)
                queue.append(v)

    # Print the results
    print("Total vertices that result in a win for X = " + str(win_for_x))
    print("Total vertices that result in a win for O = " + str(win_for_o))
    print("Total vertices that result in a tie = " + str(full_board_tie))
    print("Total number of legal boards = " + str(legal_boards))

# Call simulate function
simulate()