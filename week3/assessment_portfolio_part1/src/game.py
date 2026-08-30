#Imports
from checker import Checker
import random as r

#Class Object
class Game:
    def __init__(self, size=3, checker:Checker = Checker()):
        self.checker = checker
        self.p1 = "X"
        self.p2 = "〇"
        self.size = size
        self.board = []
        self.active_player = "X"
        self.turn = 1

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
        while not self.checker.win_check(self.board, self.active_player):
            # check stalemate
            if self.turn == 10:
                break
            self.next_turn()
            self.print_board()
            while True:
                try:
                    num_input = int(input(f"Player {self.active_player} choose a number! : "))
                except ValueError:
                    print("Invalid Input")
                    continue
                else:
                    if self.checker.input_check(num_input, self.board, self.active_player):
                        break
                    else:
                        print("Invalid Input")
                        continue
        self.print_board()
        if self.turn == 10:
            print("Game ended in tie...")
        else:
            print(f"Player {self.active_player} Wins!")


    def print_board(self):
        spaces = len(str(self.size ^ 2))
        for i in self.board:
            for j in i:
                if len(str(j)) != spaces:
                    print(f"| {j}", end=" ")
                else:
                    delta = spaces - (len(str(j)) - 1)
                    newspace = int(spaces - delta)
                    print("|", " "*newspace, str(j), end=" ")
            print("|\n", end="")

    def toggle(self):
        toggle = {
            self.p1: self.p2,
            self.p2: self.p1
        }
        self.active_player = toggle[self.active_player]

    #Turn counter
    def next_turn(self):
        print(f"Turn: {self.turn}")
        self.turn += 1
        self.toggle()