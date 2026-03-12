# Game Playing Agent

import random

class GameAgent:
    def choose_move(self):
        moves = ["rock", "paper", "scissors"]
        return random.choice(moves)

agent = GameAgent()

print("Agent move:", agent.choose_move())