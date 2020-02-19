class Board(object):
    def __init__(self, size):
        self.__board_default = '_'
        self.__board_size = size
        self.__board = [[self.__board_default for _ in range(self.__board_size)] for _ in range(self.__board_size)]

    def mark_square(self, row, col, player):
        success = False
        inbounds = (row < self.__board_size and col < self.__board_size)

        if inbounds:
            success = self.__board[row][col] == self.__board_default

        if success:
            self.__board[row][col] = player

        return success

    def get_size(self):
        return self.__board_size

    def get_square(self, row, col):
        return self.__board[row][col]

    def get_board(self):
        return self.__board

    def get_default(self):
        return self.__board_default
