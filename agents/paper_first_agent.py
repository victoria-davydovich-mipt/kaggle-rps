def paper_first(observation, configuration):
    if observation.step == 0:
        return (
            1  # statistically paper has lesser chance on being selected as 1st action
        )

    opponent_previous = observation.lastOpponentAction
    action = (opponent_previous + 1) % configuration.signs
    return action
