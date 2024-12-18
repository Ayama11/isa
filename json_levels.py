import json


levels_data = {
    "levels": [
        {
            "level_number": 1,
            "board_size": 4,
            "initial_positions": [
                {"piece_type": "magnet_purple", "position": [2, 0]},
                {"piece_type": "iron", "position": [1, 2]}
            ],
            "white_rings": [[1, 1], [1, 3]]
        },
        # {
        #     "level_number": 2,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [4, 0]},
        #         {"piece_type": "iron", "position": [1, 2]},
        #         {"piece_type": "iron", "position": [2, 1]},
        #         {"piece_type": "iron", "position": [2, 3]},
        #         {"piece_type": "iron", "position": [3, 2]}
        #     ],
        #     "white_rings": [[0, 2], [2, 0], [2, 2], [2, 4], [4, 2]]
        # },
        # {
        #     "level_number": 3,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [ 2,0]},
        #         {"piece_type": "iron", "position": [1,2]},

        #     ],
        #     "white_rings": [[2,3], [0, 3]]
        # },
        # {
        #     "level_number": 4,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [2,0]},
        #         {"piece_type": "iron", "position": [1,1]},
        #         {"piece_type": "iron", "position": [3,1]}
        #     ],
        #     "white_rings": [[0, 0], [0, 2], [4,1]]
        # },
        # {
        #     "level_number": 5,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [3,1]},
        #         {"piece_type": "iron", "position": [1, 0]},
        #         {"piece_type": "iron", "position": [1,2]},
        #         {"piece_type": "iron", "position": [2, 0]},
        #         {"piece_type": "iron", "position": [2,2]},
        #     ],
        #     "white_rings": [[0,0],[0, 2], [1,0], [1,2],[3,0]]
        # },
        # {
        #     "level_number": 6,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [2,0]},
        #         {"piece_type": "iron", "position": [1, 1]},
        #         {"piece_type": "iron", "position": [1,3]},

        #     ],
        #     "white_rings": [[0,3], [1,2],[2,3]]
        # },
        # {
        #     "level_number": 7,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [2,1]},
        #         {"piece_type": "iron", "position": [1, 0]},
        #         {"piece_type": "iron", "position": [3,1]},
        #         {"piece_type": "iron", "position": [2, 0]},
        #         {"piece_type": "iron", "position": [3,2]},
        #     ],
        #     "white_rings": [[0,0], [1,0],[2,3] ,[3,2],[4,3]]
        # },
        # {
        #     "level_number": 8,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [2,0]},
        #         {"piece_type": "iron", "position": [1, 1]},
        #         {"piece_type": "iron", "position": [1,2]},

        #     ],
        #     "white_rings": [[0,0],[0, 2], [2,2]]
        # },
        # {
        #     "level_number": 9,
        #     "board_size": 7,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [0,0]},
        #         {"piece_type": "iron", "position": [0,3]},
        #         {"piece_type": "iron", "position": [0,5]},

        #     ],
        #     "white_rings": [[0,1],[0, 3], [0,6]]
        # },
        # {
        #     "level_number": 10,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [0,0]},

        #         {"piece_type": "iron", "position": [3,1]},
        #         {"piece_type": "iron", "position": [2, 3]},
        #         {"piece_type": "iron", "position": [2,2]},
        #     ],
        #     "white_rings": [[1,1],[1,3], [3,3], [3,0]]
        # },
        # {
        #     "level_number": 11,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_red", "position": [1, 2]},
        #         {"piece_type": "iron", "position": [0, 0]},
        #         {"piece_type": "iron", "position": [0, 4]}
        #     ],
        #     "white_rings": [[0, 2], [0, 1], [0, 3]]
        # },
        # {
        #     "level_number": 12,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_red", "position": [3,1]},
        #         {"piece_type": "iron", "position": [0, 0]},
        #         {"piece_type": "iron", "position": [1,0]},
        #         {"piece_type": "iron", "position": [4,3]},

        #     ],
        #     "white_rings": [[1,0],[ 2,0], [4,0], [4,2]]
        # },
        # {
        #     "level_number": 13,
        #     "board_size": 6,
        #     "initial_positions": [
        #         {"piece_type": "magnet_red", "position": [2,3]},
        #         {"piece_type": "iron", "position": [0, 0]},
        #         {"piece_type": "iron", "position": [0,4]},
        #         {"piece_type": "iron", "position": [0,5]},

        #     ],
        #     "white_rings": [[0,3],[0, 4], [1,1], [2,1]]
        # },
        # {
        #     "level_number": 14,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_red", "position": [3,3]},
        #         {"piece_type": "iron", "position": [0,3]},
        #         {"piece_type": "iron", "position": [2,0]},
        #         {"piece_type": "iron", "position": [3, 0]},

        #     ],
        #     "white_rings": [[1,0],[1,1], [2,1], [2,2]]
        # },
        # {
        #     "level_number": 15,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [1,2]},
        #          {"piece_type": "magnet_red", "position": [2,2]},
        #         {"piece_type": "iron", "position": [0,1]},
        #         {"piece_type": "iron", "position": [0,3]},

        #     ],
        #     "white_rings": [[0,0],[0, 2], [1,4], [2,4]]
        # },
        # {
        #     "level_number": 16,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [2,4]},
        #         {"piece_type": "magnet_red", "position": [2,0]},
        #         {"piece_type": "iron", "position": [1,2]},
        #         {"piece_type": "iron", "position": [3,2]},
        #     ],
        #     "white_rings": [[0,3],[0, 4], [4,0], [4,3]]
        # },
        # {
        #     "level_number": 17,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [3, 3]},
        #         {"piece_type": "magnet_red", "position": [0, 0]},
        #         {"piece_type": "iron", "position": [0, 2]},
        #         {"piece_type": "iron", "position": [2, 0]}
        #     ],
        #     "white_rings": [[1, 1], [1, 3], [2, 2], [3, 1]]
        # },
        # {
        #     "level_number": 18,
        #     "board_size": 6,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [4, 3]},
        #         {"piece_type": "magnet_red", "position": [4,2]},
        #         {"piece_type": "iron", "position": [0, 3]},
        #         {"piece_type": "iron", "position": [2, 0]},
        #         {"piece_type": "iron", "position": [2, 5]}
        #     ],
        #     "white_rings": [[2, 1], [1, 3], [2, 2], [2,3],[2,5]]
        # },
        # {
        #     "level_number": 19,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [0,2]},
        #         {"piece_type": "magnet_red", "position": [2,2]},
        #         {"piece_type": "iron", "position": [0, 1]},
        #         {"piece_type": "iron", "position": [3, 0]},
        #         {"piece_type": "iron", "position": [4,1]},
        #         {"piece_type": "iron", "position": [4,3]}
        #     ],
        #     "white_rings": [[1, 0], [1,4], [2, 1], [3, 0],[3, 1],[3, 4]]
        # },
        # {
        #     "level_number": 20,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [4,2]},
        #         {"piece_type": "magnet_red", "position": [4,3]},
        #         {"piece_type": "iron", "position": [0, 2]},
        #         {"piece_type": "iron", "position": [0,1]},
        #         {"piece_type": "iron", "position": [4, 0]}
        #     ],
        #     "white_rings": [[0, 1], [0, 3], [2, 0], [3, 0],[1,0]]
        # },
        # {
        #     "level_number": 21,
        #     "board_size": 4,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [2,0]},
        #         {"piece_type": "magnet_red", "position": [2,3]},
        #         {"piece_type": "iron", "position": [1, 2]},
        #         {"piece_type": "iron", "position": [0,1]},
        #         {"piece_type": "iron", "position": [1,1]}
        #     ],
        #     "white_rings": [[0, 2], [1,1], [2, 0], [2,1],[1,0]]
        # },
        # {
        #     "level_number": 22,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [0,0]},
        #         {"piece_type": "magnet_red", "position": [3,2]},
        #         {"piece_type": "iron", "position": [0, 3]},
        #         {"piece_type": "iron", "position": [3,0]},
        #         {"piece_type": "iron", "position": [0,4]}
        #     ],
        #     "white_rings": [[0, 1], [0, 3],  [1,4],[1,0],[2,1]]
        # },
        # {
        #     "level_number": 23,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [3,2]},
        #         {"piece_type": "magnet_red", "position": [3,4]},
        #         {"piece_type": "iron", "position": [0,3]},
        #         {"piece_type": "iron", "position": [1,4]},
        #         {"piece_type": "iron", "position": [2, 0]}
        #     ],
        #     "white_rings": [[0, 2], [2,2], [2, 1], [3, 2],[2,3]]
        # },
        #  {
        #     "level_number": 24,
        #     "board_size": 5,
        #     "initial_positions": [
        #         {"piece_type": "magnet_purple", "position": [1,4]},
        #         {"piece_type": "magnet_red", "position": [3,0]},
        #         {"piece_type": "iron", "position": [0,1]},
        #         {"piece_type": "iron", "position": [1,3]},
        #         {"piece_type": "iron", "position": [3,4]}
        #     ],
        #     "white_rings": [[0, 3], [2,3], [2, 1], [4,1],[4,2]]
        # },
    ]
}


with open('levels.json', 'w') as file:
    json.dump(levels_data, file)

print("JSON  done")


