import heapq

from algo.Search_Maze_Algo import Search_Maze_Algo

class Ucs_Algo(Search_Maze_Algo):
    def search(self):
        self.new_open_state = []
        self.closed_state = []

        open_set = [(0, self.start, [self.start])]

        # shortest distance from start to a node
        shortest_dist = {}
        shortest_dist[self.start] = 0

        while open_set:
            prio, point, path = heapq.heappop(open_set)

            if point == self.goal:
                self.path = path
                self.total_weight = shortest_dist[point]

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
                    next_point_shortest_dist = shortest_dist[point] + 1

                    if next_point_shortest_dist < shortest_dist.get(new_point, float('inf')):
                        shortest_dist[new_point] = next_point_shortest_dist

                        if (new_x, new_y) not in open_set:
                            new_path = path.copy()
                            new_path.append(new_point)
                            
                            heapq.heappush(open_set, (shortest_dist[new_point], new_point, new_path))
                            
                            cur_new_open_state.append(new_point)

            self.new_open_state.append(cur_new_open_state)


        return None