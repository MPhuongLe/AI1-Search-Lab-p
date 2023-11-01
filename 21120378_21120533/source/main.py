from algo.Bfs_Algo import Bfs_Algo
from algo.Ucs_Algo import Ucs_Algo
from algo.Astar_Algo import Astar_Algo
from algo.Dfs_Algo import Dfs_Algo
from algo.Greedy_Algo import Greedy_Algo
from algo.Astar_Bonus_Algo import Astar_Bonus_Algo
from algo.Astar_Pickup_Algo import Astar_Pickup_Algo
from algo.Astar_Teleporter_Algo import Astar_Teleporter_Algo

import algo.heuristics_with_bonus as bonus
import algo.heuristics_with_pickup as pickup
from algo.simple_heuristics import manhattan_distance
from algo.simple_heuristics import euclidean_distance
from algo.simple_heuristics import vertical_distance

from util.helper import process_for_level 

import sys
sys.path.append('../')

algo1 = [
        [Bfs_Algo, "bfs", None], 
        [Dfs_Algo, "dfs", None],
        [Ucs_Algo, "ucs", None],
        [Greedy_Algo, "gbfs_heuristic_1", manhattan_distance],
        [Greedy_Algo, "gbfs_heuristic_2", euclidean_distance],
        [Greedy_Algo, "gbfs_heuristic_3", vertical_distance],
        [Astar_Algo, "astar_heuristic_1", manhattan_distance],
        [Astar_Algo, "astar_heuristic_2", euclidean_distance],
        [Astar_Algo, "astar_heuristic_3", vertical_distance]]

algo = [[Astar_Bonus_Algo, "astar_bonus_heuristic_1", bonus.bidirectional_heuristic], 
        [Astar_Bonus_Algo, "astar_bonus_heuristic_2", bonus.nearest_bonus_heuristic],
        [Astar_Bonus_Algo, "astar_bonus_heuristic_3", bonus.bidirectionally_goal_oriented_heuristic]]

algo3 = [[Astar_Pickup_Algo, "astar_pickup_heuristic_1", pickup.farthest_pickup_from_goal_heuristic], 
         [Astar_Pickup_Algo, "astar_pickup_heuristic_2", pickup.nearest_pickup_heuristic]] 

algo4 = [[Astar_Teleporter_Algo, "astar_teleporter_heuristic_1", manhattan_distance],
         [Astar_Teleporter_Algo, "astar_teleporter_heuristic_2", euclidean_distance]]

process_for_level("input\\level_1", algo1)
process_for_level("input\\level_2", algo)
process_for_level("input\\level_3", algo3)
process_for_level("input\\advance", algo4)

