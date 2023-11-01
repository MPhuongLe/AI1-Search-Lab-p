from collections import deque

from algo.Search_Maze_Algo import Search_Maze_Algo
from Maze import Maze

# Referenced implementation from ChatGPT

class Bfs_Algo(Search_Maze_Algo):
    def search(self):
        self.closed_state = []
        self.new_open_state = []
        
        visited = []
        open_set = deque()

        open_set.append([self.start, [self.start]])

        while open_set:
            [point, cur_path] = open_set.popleft()
            
            x, y = point[0], point[1]

            if (point in visited):
                continue

            if point == self.goal:
                self.path = cur_path
                self.total_weight = len(self.path) - 1
                return

            self.closed_state.append(point)
            visited.append(point)

            cur_new_open_state = []

            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                
                if (
                    0 <= new_x < self.m 
                    and 0 <= new_y < self.n 
                    and self.matrix[new_x][new_y] != 'x'
                ):
                    new_point = (new_x, new_y)
                    new_path = cur_path.copy()
                    new_path.append(new_point)
                    
                    if new_point not in visited:
                        open_set.append([new_point, new_path])
                        cur_new_open_state.append(new_point)

            self.new_open_state.append(cur_new_open_state)
            

        return None