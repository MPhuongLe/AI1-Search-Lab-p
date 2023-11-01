from algo.simple_heuristics import manhattan_distance

# Consider heuristics
#   manhattan_distance(node->bonus) 
# + manhattan_distance(bonus->goal) 
# + bonus_point
def bidirectional_heuristic(node, goal, bonus_points, bonus_picked):
    min_val = 100000

    for bonus in bonus_points:
        if (bonus not in bonus_picked):
            bonus_point = (bonus[0], bonus[1])
            point = bonus[2]
            min_val = min(
                min_val, 
                manhattan_distance(node, bonus_point) + manhattan_distance(bonus_point, goal) + point
            )
            
    if (min_val == 100000):
        min_val = manhattan_distance(node, goal)
    return min_val

# Consider heuristics
#   manhattan_distance(node->bonus) 
# + bonus_point
def nearest_bonus_heuristic(node, goal, bonus_points, bonus_picked):
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
# + manhattan_distance(node->goal)
# + bonus_point 
def bidirectionally_goal_oriented_heuristic(node, goal, bonus_points, bonus_picked):
    min_val = 100000

    for bonus in bonus_points:
        if (bonus not in bonus_picked):
            bonus_point = (bonus[0], bonus[1])
            point = bonus[2]
            min_val = min(
                min_val, 
                manhattan_distance(bonus_point, goal) + manhattan_distance(node, bonus_point) + point
            )
    
    if (min_val == 100000):
        min_val = 0

    return min_val + manhattan_distance(node, goal)

