from Maze import Maze

class Search_Maze_Algo:
    def __init__(self, maze : Maze):
        # Matrix info
        self.matrix = maze.matrix
        self.start = maze.start
        self.goal = maze.goal
        self.m = maze.height
        self.n = maze.width
        self.bonus_points = maze.bonus_points

        # Return info
        self.path = None
        self.closed_state = None
        self.new_open_state = None
        self.total_weight = None