import heapq

from algo.Search_Maze_Algo import Search_Maze_Algo
from Maze import Maze

class Astar_Teleporter_Algo(Search_Maze_Algo):
    def __init__(self, maze : Maze, heuristic):
        super().__init__(maze)
        self.maze = maze
        self.heuristic = heuristic
    
    def search(self):
        self.closed_state = []
        self.new_open_state = []
        open_set = [(0, self.start, [self.start], [])]

        # g: shortest distance from start to a node
        g = {}
        g[self.start] = 0

        f = {}
        f[self.start] = self.heuristic(self.start, self.goal)

        while open_set:
            prio, point, path, bonus_visited = heapq.heappop(open_set)

            if point == self.goal:
                self.path = path
                self.total_weight = g[point]
                return

            x, y = point
            

            self.closed_state.append(point)

            cur_new_open_state = []

            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                new_x, new_y = point[0] + dx, point[1] + dy
                
                if (
                    0 <= new_x < self.m 
                    and 0 <= new_y < self.n 
                    and self.matrix[new_x][new_y] != 'x'
                ):
                    new_point = (new_x, new_y)
                    next_point_g = g[point]

                    if next_point_g < g.get(new_point, float('inf')):
                        g[new_point] = next_point_g + 1
                        f[new_point] = g[new_point] + self.heuristic(new_point, self.goal)

                        if (new_x, new_y) not in open_set:
                            new_path = path.copy()
                            new_path.append(new_point)

                            heapq.heappush(open_set, (f[new_point], new_point, new_path, bonus_visited))
                            
                            cur_new_open_state.append(new_point)
            if (self.maze.is_teleporter(x, y)):
                tele_label = self.matrix[x][y][0]
                new_point = self.maze.get_tele_dest(tele_label, x, y)
                new_x = new_point[0] 
                new_y = new_point[1]
                next_point_g = g[point]

                if next_point_g < g.get(new_point, float('inf')):
                    g[new_point] = next_point_g
                    f[new_point] = g[new_point] + self.heuristic(new_point, self.goal)

                    if (new_x, new_y) not in open_set:
                        new_path = path.copy()
                        new_path.append(new_point)

                        heapq.heappush(open_set, (f[new_point], new_point, new_path, bonus_visited))

                        cur_new_open_state.append(new_point)
                    
            self.new_open_state.append(cur_new_open_state)

        return None