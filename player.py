import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        pass

class NaivePlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        square = random.choice(game.get_available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_cell = False
        value = None
        while not valid_cell:
            cell = input(self.symbol + "\'s turn: ")
            try:
                value = int(cell)
                if value not in game.get_available_moves():
                    raise ValueError
                valid_cell = True
            except ValueError:
                print("Invalid cell, please try again")
        return value