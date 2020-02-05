from models import has_won_models, get_correct_position_models, get_random_puzzle_models, empty_cell_location_models, make_movements_models
from settings import PUZZLE_SIZE


def get_available_movements(puzzle):
    movements = ["LEFT", "RIGHT", "UP", "DOWN"]
    empty_cell_x, empty_cell_y = empty_cell_location_models(puzzle)
    if empty_cell_x == 0:
        movements.remove("UP")
    if empty_cell_x == (PUZZLE_SIZE - 1):
        movements.remove("DOWN")
    if empty_cell_y == 0:
        movements.remove("LEFT")
    if empty_cell_y == (PUZZLE_SIZE - 1):
        movements.remove("RIGHT")
    return movements


def move(direction, puzzle):
    if direction in get_available_movements(puzzle):
        make_movements_models(direction, puzzle)
    return puzzle


def has_won(puzzle):
    status = has_won_models(puzzle)
    return status


def get_random_puzzle():
    puzzle = get_random_puzzle_models()
    return puzzle


def get_correct_position():
    solution = get_correct_position_models()
    return solution


