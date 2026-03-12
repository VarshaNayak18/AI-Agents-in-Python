# Path Finding Agent

class PathfindingAgent:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def find_path(self):
        print(f"Finding path from {self.start} to {self.goal}")

agent = PathfindingAgent("A", "D")
agent.find_path()