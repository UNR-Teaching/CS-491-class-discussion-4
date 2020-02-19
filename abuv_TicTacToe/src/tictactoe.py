class TicTacToe(object):
    def __init__(self, board, current_player):
        self.__current_player = current_player
        self.__board = board

    def verify_move(self, row, col):
        row -= 1
        col -= 1
        if row <= self.__board.get_size() and col <= self.__board.get_size():
            if self.__board.get_square(row, col) == self.__board.get_default():
                return row, col
        else:
            return None, None

    def turn(self, row, col):
        self.__board.mark_square(row, col, self.__current_player.get_token())
        return self.has_winner()

    def has_winner(self):
        for i in range(self.__board.get_size()):
            if self.has_row(i):
                return True

        for i in range(self.__board.get_size()):
            if self.has_col(i):
                return True

        if self.left_to_right_diag():
            return True
        if self.right_to_left_diag():
            return True

        return False

    def has_row(self, row):
        same = True
        for col in range(self.__board.get_size()):
            if self.__board.get_square(row, col) != self.__current_player.get_token():
                same = False

        return same

    def has_col(self, col):
        same = True
        for row in range(self.__board.get_size()):
            if self.__board.get_square(row, col) != self.__current_player.get_token():
                same = False

        return same

    def right_to_left_diag(self):
        same = True
        for i in range(self.__board.get_size()):
            if self.__board.get_square(i, i) != self.__current_player.get_token():
                same = False

        return same

    def left_to_right_diag(self):
        same = True
        col = self.__board.get_size() - 1

        for row in range(self.__board.get_size()):
            if self.__board.get_square(row, col) != self.__current_player.get_token():
                same = False
            col -= 1

        return same

    def set_current_player(self, player):
        self.__current_player = player

    def get_current_player(self):
        return self.__current_player

    def get_board(self):
        return self.__board
