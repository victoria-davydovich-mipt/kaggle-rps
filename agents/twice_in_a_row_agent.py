from random import randrange, seed
from helpers import SlidingWindow

seed(42)
window = SlidingWindow(2)


def twice_in_a_row(observation, configuration):
    global window
    choices = configuration.signs
    if observation.step in [0, 1]:
        return randrange(0, choices)
    last_opponent_action = observation.lastOpponentAction
    window.update(last_opponent_action)
    twice_in_a_row = window.is_same_item()
    action = last_opponent_action if twice_in_a_row else randrange(0, choices)
    return action
