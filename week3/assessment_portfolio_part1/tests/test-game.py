# Imports
import unittest
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()

    def test_ui(self):
        self.game.reset_game()
        self.assertEqual([[0, 1, 2], [3, 4, 5], [6, 7, 8]], self.game.board)

    def test_ui_large_grid(self, size= 5):
        self.game = game.Game(size=size)
        self.game.reset_game()
        self.assertEqual([
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24]
        ], self.game.board)

    def test_single_input(self):
        user_input = 0
        self.game.reset_game()
        self.assertEqual(self.game._input_check(user_input, self.game.board, self.game.active_player), True)

    def test_single_input_too_high(self):
        user_input = 99
        self.game.reset_game()
        self.assertEqual(self.game._input_check(user_input, self.game.board, self.game.active_player), False)


