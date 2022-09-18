from random import randrange, seed

seed(42)


def last_opponent_action(observation, configuration):
    if observation.step == 0:
        return randrange(0, configuration.signs)

    opponent_previous = observation.lastOpponentAction
    action = (opponent_previous + 1) % configuration.signs
    return action
