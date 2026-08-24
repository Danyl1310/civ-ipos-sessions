from idlelib.configdialog import is_int
import math
from operator import truediv


class Checker:
    def __init__(self):
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
        x_coords = {}
        y_coords = {}
        #debug
        print(self.__coords)
        #Counts Coords
        for i, coord in enumerate(self.__coords):
            if coord[0] not in y_coords:
                y_coords.update({coord[0]: 1})
            elif coord[0] in y_coords:
                y_coords[coord[0]] += 1
            if coord[1] not in x_coords:
                x_coords.update({coord[1]: 1})
            elif coord[1] in x_coords:
                x_coords[coord[1]] += 1
        print(f"X: {x_coords}, Y: {y_coords}")
        if 3 in x_coords.values() or 3 in y_coords.values():
            return True
        #Diagonals
        return False

    @staticmethod
    def input_check(user_input, board, player):
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



