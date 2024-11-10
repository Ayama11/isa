import json

from board import Board
from piece import Piece


class Game:
    def __init__(self):
        self.current_level = 0
        self.levels = self.load_levels('levels.json')
        self.board = None
        self.solve_automatically = False  # Flag to determine if the game should be solved automatically

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

        user_choice = input("enter  '1' for user play , enter '2' play BFS: ")

        if user_choice == '1':
            # تشغيل اللعبة يدوياً
            while True:
                print(f"المستوى الحالي: {self.levels[self.current_level]['level_number']}")
                self.board.display()

                try:
                    x, y = map(int, input("enter x y (x y): ").split())
                    target_x, target_y = map(int, input("enter target x y (target_x target_y): ").split())
                    piece = self.board.grid[x][y]
                    if piece is None:
                        print(" No piece found ")
                        continue
                    if piece.piece_type == 'iron':
                        print("iron dont move ")
                        continue

                    if self.board.move_piece(piece, target_x, target_y):
                        print("piece moved done")
                    else:
                        print("cant move")

                    self.board.apply_magnet_effects()

                    if self.check_win():
                        print("level done")
                        self.board.display()
                        self.current_level += 1
                        if self.current_level < len(self.levels):
                            self.setup_level()
                        else:
                            print("All levels done")
                            break
                    self.board.display()
                    self.board.save_board_state()

                except ValueError:
                    print("invail input")
                except IndexError:
                    print("x y out of range")

        elif user_choice == '2':
            
            solution = self.bfs()  
            if solution:
                print(" solution solved with BFS:")
                for step in solution:
                    print(step)
            else:
                print("no solution this level")
        else:
            print(" invaild input enter '1' or '2'.")


    def bfs(self):
        if self.board is None:
            self.setup_level()

        initial_state = self.board.get_state()  # Get the initial state of the board
        visited = set([tuple(sorted(initial_state.items()))])  # Store visited states
        queue = [(initial_state, [])]  # Queue of (state, path to reach it)
# تم استدعاؤها بشكل صحيح هنا
        while queue:
            current_state, path = queue.pop(0)

            if self.is_goal_state(current_state):
                return path  # Return the sequence of moves to solve the game

            for next_state, move in self.get_neighbors(current_state):
                state_tuple = tuple(sorted(next_state.items()))
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    queue.append((next_state, path + [move]))  # Add the new state and move to path

        return None  # Return None if no solution found



    


    def is_goal_state(self, state):
        """التحقق من إذا كانت الحالة هي حالة الهدف (جميع الحلقات البيضاء مليئة بقطع حديدية أو مغناطيسات)"""
        # تحقق من أن جميع الحلقات البيضاء مليئة بقطع حديدية أو مغناطيسات
        for x, y in self.board.white_rings:
            piece = state.get((x, y))
            if not piece or piece[0] not in ['iron', 'magnet_red', 'magnet_purple']:
                return False
        return True

   
    def get_neighbors(self, state):
        """إرجاع الحركات المجاورة لحالة معينة"""
        neighbors = []
        for x in range(self.board.size):
            for y in range(self.board.size):
                piece = state.get((x, y))
                if isinstance(piece, Piece) and piece.piece_type in ['magnet_red', 'magnet_purple']:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        for distance in range(1, 3):
                            nx, ny = x + dx * distance, y + dy * distance
                            if self.board.is_within_bounds(nx, ny): 
                                target_piece = self.board.grid[nx][ny]
                                if target_piece is None or target_piece.piece_type == 'iron': 
                                    new_state = self.apply_move(state, piece, nx, ny)
                                    neighbors.append((new_state, (x, y, nx, ny)))
        return neighbors
   


    # def get_neighbors(self, state):
    #     neighbors = []
    #     for x in range(self.board.size):
    #         for y in range(self.board.size):
    #             piece = state.get((x, y))
    #             if isinstance(piece, Piece) and piece.piece_type in ['magnet_red', 'magnet_purple']:
    #                 # Generate moves for adjacent cells (up, down, left, right)
    #                 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #                     for distance in range(1, 3):  # Can adjust range if needed
    #                         nx, ny = x + dx * distance, y + dy * distance
    #                         if self.board.is_within_bounds(nx, ny):
    #                             target_piece = self.board.grid[nx][ny]
    #                             if target_piece is None or target_piece.piece_type == 'iron':
    #                                 # Generate new state by applying the move
    #                                 new_state = self.apply_move(state, piece, nx, ny)
    #                                 neighbors.append((new_state, (x, y, nx, ny)))  # Store the move
    #     return neighbors



    def apply_move(self, state, piece, nx, ny):
        new_state = state.copy()  # Copy the current state to modify
        current_position = piece.position
        # Update the position of the piece in the new state
        new_state[(current_position[0], current_position[1])] = None
        new_state[(nx, ny)] = piece  # Set the piece in the new position
        piece.position = (nx, ny)  # Update the piece's position
        return new_state
  
    

    def apply_solution(self, solution):
        """تطبيق الحل المقدم من خوارزمية BFS على اللعبة"""
        for move in solution:
            x, y, target_x, target_y = move
            piece = self.board.grid[x][y]
            self.board.move_piece(piece, target_x, target_y)
            self.board.apply_magnet_effects()

    def make_hashable(self, state):
        """تحويل الحالة إلى شكل قابل للتجزئة (hashable)"""
        hashable_state = {}
        for key, value in state.items():
            if isinstance(value, set):
                hashable_state[key] = frozenset(value)
            else:
                hashable_state[key] = value
        return hashable_state


game = Game()
game.play()
