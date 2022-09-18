from random import randrange, seed
from helpers import SlidingWindow

seed(42)
window = SlidingWindow(2)


def duplet_stats(observation, configuration):
    global window

    # skipping first 2 steps to fill in the records for the sliding window of size 2
    if observation.step in [0, 1]:
        return randrange(0, configuration.signs)

    last = observation.lastOpponentAction
    window.update(last)

    # dict mapping action to its # occurencies after last opponent action
    action_stats = {
        record[1]: count
        for record, count in window.history.items()  # history accumulates # occurences of 2-grams
        if record[0] == last
    }

    most_frequent = max(
        action_stats, key=action_stats.get
    )  # most frequest action after last action
    action = (most_frequent + 1) % configuration.signs
    return action
