from random import randrange, seed

seed(42)
record = {}


def least_frequent(observation, configuration):
    global record
    if observation.step == 0:
        record = {k: 0 for k in range(configuration.signs)}  # init record on 1st step
        return randrange(0, configuration.signs)
    record[observation.lastOpponentAction] += 1
    action = min(record, key=record.get)
    return action
