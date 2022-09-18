from random import randrange, seed

from helpers import SlidingWindow

seed(42)
window = SlidingWindow(3)
history = []


def triplet_stats(observation, configuration):
    global window
    global history

    if observation.step == 0:
        return randrange(0, configuration.signs)

    last = observation.lastOpponentAction

    if observation.step in [1, 2]:
        action = randrange(0, configuration.signs)
    else:
        window.update(last)

        actions_stats = {
            record[2]: count
            for record, count in window.history.items()
            if record[0] == history[-1] and record[1] == last
        }
        if actions_stats:
            most_frequent = max(actions_stats, key=actions_stats.get)
            action = (most_frequent + 1) % configuration.signs
        else:
            action = randrange(0, configuration.signs)

    history.append(last)
    return action
