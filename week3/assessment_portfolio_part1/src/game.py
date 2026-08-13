#Imports
from checker import Checker
import random as r

#Class Object
class Game(Checker):
    def __init__(self, size=3):
        super().__init__()
        self.p1 = "X"
        self.p2 = "〇"
        self.size = size
        self.board = []
        self.active_player = "X"

    def reset_game(self):
        self.active_player = r.choice([self.p1, self.p2])
        for i in range(self.size):
            self.board.append([])
            for j in range(self.size):
                self.board[i].append((i * self.size) + j)

    def play(self):
        # Reset game before starting.
        self.reset_game()
        print(f"Player {self.active_player} is going first.. ")
        # Game Loop
        self.toggle()
        while not self.win_check(self.board, self.active_player):
            self.toggle()
            self.print_board()
            while True:
                try:
                    num_input = int(input(f"Player {self.active_player} choose a number! : "))
                except ValueError:
                    print("Invalid Input")
                    continue
                else:
                    if self._input_check(num_input, self.board, self.active_player):
                        break
                    else:
                        print("Invalid Input")
                        continue

    def print_board(self):
        for i in self.board:
            for j in i:
                print(f"| {j}", end=" ")
            print("|\n", end="")

    def toggle(self):
        toggle = {
            self.p1: self.p2,
            self.p2: self.p1
        }
        self.active_player = toggle[self.active_player]