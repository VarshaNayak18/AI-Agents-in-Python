# MiniMax Agent

class MinimaxAgent:

    def minimax(self, depth, is_maximizing):

        if depth == 0:
            return 0

        if is_maximizing:
            best = -1000

            for _ in range(2):
                value = self.minimax(depth - 1, False)
                best = max(best, value)

            return best

        else:
            best = 1000

            for _ in range(2):
                value = self.minimax(depth - 1, True)
                best = min(best, value)

            return best


agent = MinimaxAgent()
print(agent.minimax(3, True))