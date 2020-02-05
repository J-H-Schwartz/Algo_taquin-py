import random
from settings import PUZZLE_SIZE, EMPTY_CELL_VALUE

def has_won_models(puzzle):
    # TODO : vérifier si le jeu est gagné
    pass


def get_random_puzzle_models():
    # TODO : certains états random ne sont pas solvables,
    # il faut que cette fonction ne renvoie que des états solvables
    cells = list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE]
    random.shuffle(cells)
    return [list(a) for a in zip(*[iter(cells)] * PUZZLE_SIZE)]


def get_correct_position():
    CORRECT_SOLUTION = [list(a) for a in
                        zip(*[iter(list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE])] * PUZZLE_SIZE)]
    return CORRECT_SOLUTION