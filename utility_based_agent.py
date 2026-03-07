# Utility-Based Agent

def choose_action(actions):
    utilities = {
        "A": 5,
        "B": 8,
        "C": 3
    }
    return max(utilities, key=utilities.get)

print("Best action:", choose_action(["A", "B", "C"]))