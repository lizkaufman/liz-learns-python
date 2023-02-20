# https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers
    :return: int - minutes to prepare

    Fn that takes the number of layers and calculates how long to make lasagna
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate how much time has elapsed so far

    :param number_of_layers: int - layers in lasagna
    :param elapsed_bake_time: int - time in oven so far in mins
    :return: int - minutes passed so far

    While lasagna is in oven, fn returns the amount of time since cooking started
    """
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time + elapsed_bake_time
    