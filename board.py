import json


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.white_rings = []
        self.filled_rings = set()

    def reset_board(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.white_rings.clear()
        self.filled_rings.clear()

    def place_piece(self, piece, x, y):
        if self.is_within_bounds(x, y):
            self.grid[x][y] = piece
            piece.position = (x, y)

    def is_within_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def can_move(self, piece, target_x, target_y):
        if not self.is_within_bounds(target_x, target_y):
            return False
        target_piece = self.grid[target_x][target_y]
        return target_piece is None or (target_x, target_y) in self.white_rings

    def move_piece(self, piece, target_x, target_y):
        x, y = piece.position
        if self.can_move(piece, target_x, target_y):
            self.grid[x][y] = None
            if (x, y) in self.filled_rings:
                self.filled_rings.discard((x, y))
            self.grid[target_x][target_y] = piece
            piece.position = (target_x, target_y)
            if (target_x, target_y) in self.white_rings:
                self.filled_rings.add((target_x, target_y))
            self.save_board_state()
            return True
        return False
    def apply_magnet_effects(self):
        for x in range(self.size):
           for y in range(self.size):
              piece = self.grid[x][y]
              if piece and piece.piece_type in ['magnet_red', 'magnet_purple']:
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    for distance in range(1, 3):
                        nx, ny = x + dx * distance, y + dy * distance
                        if self.is_within_bounds(nx, ny):
                            target_piece = self.grid[nx][ny]
                            if target_piece and target_piece.piece_type == 'iron':
                                if piece.piece_type == 'magnet_red':
                                    target_x, target_y = x - dx, y - dy
                                    if self.is_within_bounds(target_x, target_y) and self.grid[target_x][target_y] is None:
                                        self.grid[nx][ny] = None
                                        target_piece.position = (target_x, target_y)
                                        self.grid[target_x][target_y] = target_piece
                                        if target_piece.position in self.white_rings:
                                            self.filled_rings.add(target_piece.position)
                                elif piece.piece_type == 'magnet_purple':
                                    repel_x, repel_y = nx + dx, ny + dy
                                    if self.is_within_bounds(repel_x, repel_y) and self.grid[repel_x][repel_y] is None:
                                        self.grid[nx][ny] = None
                                        target_piece.position = (repel_x, repel_y)
                                        self.grid[repel_x][repel_y] = target_piece
                                        if target_piece.position in self.white_rings:
                                            self.filled_rings.add(target_piece.position)
                
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    for distance in range(1,3):
                        nx, ny = x + dx * distance, y + dy * distance
                        if self.is_within_bounds(nx, ny):
                            adjacent_piece = self.grid[nx][ny]
                            if adjacent_piece and adjacent_piece.piece_type in ['magnet_red', 'magnet_purple']:
                                if piece.piece_type == 'magnet_red':
                                    
                                    target_x, target_y = x - dx, y - dy
                                    if self.is_within_bounds(target_x, target_y) and self.grid[target_x][target_y] is None:
                                        self.grid[nx][ny] = None
                                        adjacent_piece.position = (target_x, target_y)
                                        self.grid[target_x][target_y] = adjacent_piece
                                elif piece.piece_type == 'magnet_purple':
                                   
                                    repel_x, repel_y = nx + dx, ny + dy
                                    if self.is_within_bounds(repel_x, repel_y) and self.grid[repel_x][repel_y] is None:
                                        self.grid[nx][ny] = None
                                        adjacent_piece.position = (repel_x, repel_y)
                                        self.grid[repel_x][repel_y] = adjacent_piece

  
    def save_board_state(self):
        state = [[
            'X' if (i, j) in self.filled_rings and (self.grid[i][j] is None or self.grid[i][j].piece_type == 'iron') else
            'RX' if (i, j) in self.filled_rings and self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_red' else
            'PX' if (i, j) in self.filled_rings and self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_purple' else
            'O' if (i, j) in self.white_rings else
            'R' if self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_red' else
            'P' if self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_purple' else
            'I' if self.grid[i][j] and self.grid[i][j].piece_type == 'iron' else '_'
            for j, cell in enumerate(row)]
                 for i, row in enumerate(self.grid)]
        with open('board_state.json', 'w') as file:
            json.dump(state, file)
            

    def display(self):
        for i, row in enumerate(self.grid):
            print(' '.join([
                'IX' if (i, j) in self.white_rings and self.grid[i][j] and self.grid[i][j].piece_type == 'iron' else
                'X' if (i, j) in self.filled_rings and (self.grid[i][j] is None or self.grid[i][j].piece_type == 'iron') else
                'RX' if (i, j) in self.filled_rings and self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_red' else
                'PX' if (i, j) in self.filled_rings and self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_purple' else
                'O' if (i, j) in self.white_rings else
                'R' if self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_red' else
                'P' if self.grid[i][j] and self.grid[i][j].piece_type == 'magnet_purple' else
                'I' if self.grid[i][j] and self.grid[i][j].piece_type == 'iron' else '_'
                for j, cell in enumerate(row)
            ]))
        print("\n")

