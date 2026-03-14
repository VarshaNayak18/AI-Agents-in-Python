# Q-Learning Learning

import numpy as np

class QLearningAgent:

    def __init__(self):
        self.q_table = np.zeros((5, 2))
        self.learning_rate = 0.1

    def update(self, state, action, reward):
        self.q_table[state][action] += self.learning_rate * reward

agent = QLearningAgent()

agent.update(0, 1, 10)

print(agent.q_table)