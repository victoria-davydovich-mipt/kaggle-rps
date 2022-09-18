from random import randrange, seed

seed(42)


def random(observation, configuration):
    action = randrange(0, configuration.signs)
    print(action)
    return action
