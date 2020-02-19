import unittest
from tictactoe import TicTacToe
from board import Board
from player import Player


class TestHasRow(unittest.TestCase):
    # integration tests
    def test_row_set(self):
        board = Board(3)
        player = Player('X')
        board.mark_square(0, 0, player.get_token())
        board.mark_square(0, 1, player.get_token())
        board.mark_square(0, 2, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.has_row(0))

    def test_col_set(self):
        board = Board(3)
        player = Player('O')
        board.mark_square(0, 0, player.get_token())
        board.mark_square(1, 0, player.get_token())
        board.mark_square(2, 0, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.has_col(0))


class TestRightToLeftDiag(unittest.TestCase):
    def test_diag_set(self):
        board = Board(3)
        player = Player('O')
        board.mark_square(0, 0, player.get_token())
        board.mark_square(1, 1, player.get_token())
        board.mark_square(2, 2, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.right_to_left_diag())


class TestLeftToRightDiag(unittest.TestCase):
    def test_diag_set(self):
        board = Board(3)
        player = Player('O')
        board.mark_square(0, 2, player.get_token())
        board.mark_square(1, 1, player.get_token())
        board.mark_square(2, 0, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.left_to_right_diag())


class TestHasWinner(unittest.TestCase):
    def test_2nd_row(self):
        board = Board(3)
        player = Player('X')
        board.mark_square(1, 0, player.get_token())
        board.mark_square(1, 1, player.get_token())
        board.mark_square(1, 2, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.has_winner())

    def test_3rd_col(self):
        board = Board(3)
        player = Player('X')
        board.mark_square(0, 2, player.get_token())
        board.mark_square(1, 2, player.get_token())
        board.mark_square(2, 2, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.has_winner())

    def test_diag_set(self):
        board = Board(3)
        player = Player('O')
        board.mark_square(0, 2, player.get_token())
        board.mark_square(1, 1, player.get_token())
        board.mark_square(2, 0, player.get_token())

        tictactoe = TicTacToe(board, player)

        self.assertTrue(tictactoe.has_winner())


class TestVerifyMove(unittest.TestCase):
    def test_in_bounds(self):
        board = Board(3)
        player = Player('O')
        tictactoe = TicTacToe(board, player)

        test_board = Board(3)
        test_board.mark_square(1, 1, player.get_token())

        row, col = tictactoe.verify_move(2, 2)

        self.assertEqual(row, 1)
        self.assertEqual(col, 1)


class TestTurn(unittest.TestCase):
    def test_in_bounds(self):
        board = Board(3)
        player = Player('O')
        tictactoe = TicTacToe(board, player)

        test_board = Board(3)
        test_board.mark_square(1, 1, player.get_token())

        winner = tictactoe.turn(1, 1)

        self.assertEqual(board.get_square(1, 1), test_board.get_square(1, 1))
        self.assertFalse(winner)
