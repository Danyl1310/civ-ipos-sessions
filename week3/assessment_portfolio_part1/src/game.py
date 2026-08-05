

class Game:
    def __init__(self, size=3):
        self.p1 = "X"
        self.p2 = "O"
        self.size = size
        self.board = []

    def reset_game(self):
        for i in range(self.size):
            self.board.append([])
            for j in range(self.size):
                self.board[i].append((i * self.size) + j)


    def play(self):
        while True:
            print(self.board)
            input()

    def print_board(self):
        for i in self.board:
            for j in i:
                print(f"| {j}", end=" ")
            print("|\n", end="")