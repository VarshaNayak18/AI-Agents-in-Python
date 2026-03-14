# A* Pathfinding Agent

import heapq

class AStarAgent:

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star(self, start, goal):

        open_list = []
        heapq.heappush(open_list, (0, start))

        came_from = {}
        cost_so_far = {start: 0}

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == goal:
                break

            neighbors = [
                (current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1)
            ]

            for next_node in neighbors:
                new_cost = cost_so_far[current] + 1

                if next_node not in cost_so_far:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal, next_node)
                    heapq.heappush(open_list, (priority, next_node))
                    came_from[next_node] = current

        return came_from


agent = AStarAgent()
print(agent.a_star((0,0), (2,2)))