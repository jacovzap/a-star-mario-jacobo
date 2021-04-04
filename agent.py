class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function_BFS(self, state, actions):
        successors = []
        for action in actions:
            if action == self.settings.NORTH:
                successors.append([state[0] - 1, state[1]])
            if action == self.settings.SOUTH:
                successors.append([state[0] + 1, state[1]])
            if action == self.settings.WEST:
                successors.append([state[0], state[1] - 1])
            if action == self.settings.EAST:
                successors.append([state[0], state[1] + 1])

        return successors

    def transition_function_A(self, state, actions):
        successors = []
        for action in actions:
            if action == self.settings.NORTH:
                successors.append([state[0] - 1, state[1]])
            if action == self.settings.SOUTH:
                successors.append([state[0] + 1, state[1]])
            if action == self.settings.WEST:
                successors.append([state[0], state[1] - 1])
            if action == self.settings.EAST:
                successors.append([state[0], state[1] + 1])

            if action == self.settings.NORTHEAST:
                successors.append([state[0] - 1, state[1] + 1])
            if action == self.settings.NORTHWEST:
                successors.append([state[0] - 1, state[1] - 1])
            if action == self.settings.SOUTHWEST:
                successors.append([state[0] + 1, state[1] - 1])
            if action == self.settings.SOUTHEAST:
                successors.append([state[0] + 1, state[1] + 1])

        return successors


