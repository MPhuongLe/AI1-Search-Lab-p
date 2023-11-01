import math

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    res = abs(x1 - x2) + abs(y1 - y2)
    return res

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    res = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return res

def vertical_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    res = abs(y1 - y2)
    return res