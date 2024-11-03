import json

from board import Board
from piece import Piece


class Game:
    def __init__(self):
        self.current_level = 0
        self.levels = self.load_levels('levels.json')
        self.board = None

    def load_levels(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data['levels']

    def setup_level(self):
        level_data = self.levels[self.current_level]
        board_size = level_data['board_size']
        self.board = Board(board_size)
        self.board.white_rings = [tuple(ring) for ring in level_data['white_rings']]
        for pos in level_data['initial_positions']:
            piece = Piece(pos['piece_type'], tuple(pos['position']))
            self.board.place_piece(piece, *pos['position'])
        self.board.filled_rings.clear()

    def check_win(self):
        return all((x, y) in self.board.filled_rings for x, y in self.board.white_rings)

    def play(self):
        self.setup_level()
        while True:
            print(f"current_level: {self.levels[self.current_level]['level_number']}")
            self.board.display()

            try:
                x, y = map(int, input(" enter x y (x y): ").split())
                target_x, target_y = map(int, input("ف enter target (target_x target_y): ").split())
                piece = self.board.grid[x][y]
                if piece is None:
                    print(f"no piece found")
                    continue
                if piece.piece_type == 'iron':
                    print(f"iron not move")
                    continue

                if self.board.move_piece(piece, target_x, target_y):
                    print("piece move done ")
                else:
                    print("cant move ")

                self.board.apply_magnet_effects()

                if self.check_win():
                    print("level done")
                    self.board.display()
                    self.current_level += 1
                    if self.current_level < len(self.levels):
                        self.setup_level()
                    else:
                        print("all level done")
                        break
                self.board.display()
                self.board.save_board_state()

            except ValueError:
                print("invalid input")
            except IndexError:
                print(" x y out of range")
game = Game()
game.play()