from idlelib.configdialog import is_int
import math

class Checker:
    def __init__(self):
        self.__finished = False
        self.__coords = []

    def analyse_board(self, board, player):
        self.__coords = []
        for i, row in enumerate(board):
            if player in row:
                for j, value in enumerate(row):
                    if value == player:
                        self.__coords.append((j, i))

    def win_check(self, board, player):
        self.analyse_board(board, player)
        number = len(board)
        #Straight Lines
        x_count = 0
        y_count = 0
        for i, (x, y) in enumerate(self.__coords):
            if x == self.__coords[i-1][0]:
                x_count += 1
            else:
                x_count = 0
            if y == self.__coords[i-1][0]:
                y_count += 1
            else:
                y_count = 0
            if x_count == number or y_count == number:
                return True
        #Diagonals
        return False

    @staticmethod
    def _input_check(user_input, board, player):
        available_numbers = []
        for row in board:
            for value in row:
                available_numbers.append(value)

        if user_input in available_numbers:
            if user_input < len(board):
                board[0][user_input] = player
                return True
            else:
                temp_v = math.floor(user_input / len(board))
                board[temp_v][user_input - (len(board) * temp_v)] = player
                return True
        return False



