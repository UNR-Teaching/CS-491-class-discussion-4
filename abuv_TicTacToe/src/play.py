from board import Board
from player import Player
from tictactoe import TicTacToe


def display_board(game_board):
    for row in range(game_board.get_size()):
        print(game_board.get_board()[row])


def take_turn(game):
    row = int(input("Enter your row: "))
    col = int(input("Enter your col: "))

    row, col = tictactoe.verify_move(row, col)
    return game.turn(row, col)


def end_game(game):
    if game.has_winner():
        print(f'You won, Player{game.get_current_player().get_token()}')
    else:
        print("Cat's Game!")


if __name__ == '__main__':
    size = 3
    board = Board(size)
    playerX = Player('X')
    playerO = Player('O')
    tictactoe = TicTacToe(board, playerO)

    game_over = False
    moves = 1

    while not game_over:
        display_board(tictactoe.get_board())

        if tictactoe.get_current_player() == playerX:
            tictactoe.set_current_player(playerO)
        else:
            tictactoe.set_current_player(playerX)

        moves += 1
        game_over = take_turn(tictactoe) or moves > size * size

    end_game(tictactoe)
