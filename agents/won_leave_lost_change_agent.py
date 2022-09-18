import random


previous_action = None


def won_leave_lost_change(observation, configuration):
    global previous_action
    choices = configuration.signs
    if observation.step == 0 or previous_action is None:
        action = random.randrange(0, choices)
        previous_action = action
        return action

    previous_opponent_action = observation.lastOpponentAction

    if (previous_opponent_action + 1) % choices == previous_action:
        return previous_action
    else:
        action = random.choice([i for i in range(choices) if i != previous_action])
        previous_action = action
        return action
