import random

class NimAI():

    def __init__(self, alpha=0.5, epsilon=0.1):
        """
        Initialize AI with an empty Q-learning dictionary,
        an alpha (learning) rate, and an epsilon rate.

        The Q-learning dictionary maps `(state, action)`
        pairs to a Q-value (a number).
         - `state` is a tuple of remaining piles, e.g. (1, 1, 4, 4)
         - `action` is a tuple `(i, j)` for an action
        """
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        """
        Return the Q-value for the state `state` and the action `action`.
        If no Q-value exists yet in `self.q`, return 0.
        """
        if (tuple(state), action) in self.q:
            return self.q[(tuple(state), action)]
        return 0



if __name__ == '__main__':
    nimAi = NimAI()

    states = [[1, 2, 3, 4], [1, 1, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0]]
    actions = [(1, 0), (1, 1), (0, 1), (0, 0)]

    state = states[0]

    for action in actions:
        nimAi.q[(tuple(state), action)] = random.randint(1, 100)

    print(nimAi.q)
    # sorted_q = max(sorted(actions, key=lambda action: nimAi.get_q_value(state,
    #                                                               action)))

    best_action = max(actions, key=lambda action: nimAi.get_q_value(state,
                                                                  action))

    print(best_action)