import unittest
import checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = checker.Checker()
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def test_input(self):
        self.assertEqual(True, self.checker.input_check(3, self.board, "X"))
        self.assertEqual(True, self.checker.input_check(8, self.board, "O"))
        self.assertEqual(True, self.checker.input_check(0, self.board, "X"))

    def test_wrong_input(self):
        self.assertEqual(False, self.checker.input_check("L", self.board, "X"))
        self.assertEqual(False, self.checker.input_check(9, self.board, "O"))
        self.assertEqual(False, self.checker.input_check(-1, self.board, "X"))