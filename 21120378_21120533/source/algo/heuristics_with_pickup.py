from algo.simple_heuristics import manhattan_distance

# Consider heuristics
#   manhattan_distance(node->bonus) 
# + bonus_point
def nearest_pickup_heuristic(node, goal, bonus_points, bonus_picked):
    min_val = 100000

    for bonus in bonus_points:
        if (bonus not in bonus_picked):
            bonus_point = (bonus[0], bonus[1])
            min_val = min(
                min_val, 
                manhattan_distance(node, bonus_point)
            )

    if (min_val == 100000):
        min_val = manhattan_distance(node, goal)

    return min_val

# Consider heuristics
#   manhattan_distance (node->bonus) 
# + manhattan_distance(bonus->goal) 
def farthest_pickup_from_goal_heuristic(node, goal, bonus_points, bonus_picked):
    max_val = -10000000000

    for bonus in bonus_points:
        if (bonus not in bonus_picked):
            bonus_point = (bonus[0], bonus[1])
            max_val = max(
                max_val, 
                manhattan_distance(bonus_point, goal) + manhattan_distance(node, bonus_point)
            )

    if (max_val == -10000000000):
        max_val = manhattan_distance(node, goal)

    return max_val