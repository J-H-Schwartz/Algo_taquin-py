from models import *


def get_available_movements():
    # TODO : retourner une liste de mouvements possibles ["LEFT", "UP"]
    return []


def move(direction, puzzle):
    # TODO :
    # * récupérer les mouvements possibles pour l'état en cours
    # * appliquer le mouvement si c'est permis
    # * retourner l'état modifié
    return puzzle


def has_won(puzzle):
    status = has_won_models(puzzle)
    return status


def get_random_puzzle():
    puzzle = get_random_puzzle_models()
    return puzzle