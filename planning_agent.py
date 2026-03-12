# Planning Agent

class PlanningAgent:
    def __init__(self, goal):
        self.goal = goal

    def plan(self):
        print("Planning steps to achieve goal-", self.goal)
        steps = ["Analyze environment", "Choose actions", "Execute plan"]
        return steps

agent = PlanningAgent("Reach destination:")

for step in agent.plan():
    print(step)