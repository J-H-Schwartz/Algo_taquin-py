from random import shuffle
from settings import PUZZLE_SIZE, EMPTY_CELL_VALUE


def has_won_models(puzzle):
    solved_puzzle = get_correct_position_models()
    if puzzle == solved_puzzle:
        return True
    else:
        return False



def get_random_puzzle_models():
    solvable = False
    while not solvable:
        cells = list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE]
        shuffle(cells)
        puzzle = [list(a) for a in zip(*[iter(cells)] * PUZZLE_SIZE)]
        solvable = is_solvable_models(puzzle)
        if not solvable:
            print("plop")
    return puzzle


def get_correct_position_models():
    CORRECT_SOLUTION = [list(a) for a in
                        zip(*[iter(list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE])] * PUZZLE_SIZE)]
    return CORRECT_SOLUTION


def is_solvable_models(puzzle):

    # Boucle de transformation du puzzle en liste simple.
    puzzle_list = []
    for i in puzzle:
        for j in i:
            puzzle_list.append(j)

    # Boucle de comptage d'inversions.
    inversions = 0
    comparing = 0
    empty_cell_index = 0
    while comparing < len(puzzle_list):
        compared = comparing + 1
        if not puzzle_list[comparing] == EMPTY_CELL_VALUE:
            while compared < len(puzzle_list):
                if not puzzle_list[compared] == EMPTY_CELL_VALUE:
                    if puzzle_list[comparing] > puzzle_list[compared]:
                        inversions += 1
                compared += 1
        else:
            empty_cell_index = comparing
        comparing += 1

    # Positionnement de la case vide.
    row = 0
    while empty_cell_index > PUZZLE_SIZE - 1:
        empty_cell_index -= PUZZLE_SIZE
        row += 1

    # Conditions de solvabilité, renvoie True ou False et les coordonnées x et y de la case vide.
    if (PUZZLE_SIZE % 2) != 0 and (inversions % 2) == 0:
        return True
    elif PUZZLE_SIZE % 2 == 0:
        if (row % 2 != 0) == (inversions % 2 == 0):
            return True
        else:
            return False
    else:
        return False


def empty_cell_location_models(puzzle):
    for x, row in enumerate(puzzle):
        for y, cell in enumerate(row):
            if cell == EMPTY_CELL_VALUE:
                return x, y
