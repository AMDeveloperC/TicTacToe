from player import HumanPlayer
from player import NaivePlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(':' + ':'.join(row)+':')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(':' + ':'.join(row) + ':')

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def get_empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, cell, symbol):
        if (self.board[cell] == ' '):
            self.board[cell] = symbol
            if (self.winner(cell, symbol)):
                self.current_winner = symbol
            return True
        return False

    def winner(self, cell, symbol):
        row_index = cell // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if (all([spot == symbol for spot in row])):
            return True
        col_index = cell % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if (all([spot == symbol for spot in column])):
            return True
        if (cell % 2 == 0):
            p_diagonal = [self.board[i] for i in [0, 4, 8]]
            if (all([spot == symbol for spot in p_diagonal])):
                return True
            s_diagonal = [self.board[i] for i in [2, 4, 6]]
            if (all([spot == symbol for spot in s_diagonal])):
                return True
        return False

def play(game, x_player, o_player, verbose = False):
    if verbose:
        game.print_board_nums()
    symbol = 'X'
    while (game.get_empty_squares()):
        if (symbol == 'O'):
            cell = o_player.get_move(game)
        else:
            cell = x_player.get_move(game)
        if (game.make_move(cell, symbol)):
            if verbose:
                print(symbol + f" makes a move to square {cell}")
                game.print_board()
                print(" ")
            if (game.current_winner):
                if verbose:
                    print("The winner is " + str(symbol))
                return symbol
            symbol = 'O' if symbol == 'X' else 'X'
    if verbose:
        print("Game over")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = NaivePlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, True)