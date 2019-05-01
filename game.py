import sys
from board import Board
from player import Player
from bank import Bank

class Game():
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.board = Board()
        self.bank = Bank()

    def start_game(self):
        pass

    def turn(self):
        pass

    def status(self):
        pass
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        game = Game(sys.argv[1:])
    else:
        print('Please provide the list of players as a command line argument')