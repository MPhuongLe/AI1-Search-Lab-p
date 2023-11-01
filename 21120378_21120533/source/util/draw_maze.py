import os
import matplotlib.pyplot as plt
from PIL import Image
import io

from Maze import Maze

import random

# referenced function read_file of notebook https://colab.research.google.com/drive/1ejLc4LkrmjpbcRYC3W2xjfA0C0o1PWTp?usp=sharing

def generate_random_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    return (red, green, blue)

def visualize_maze(maze: Maze, route = None, closed_state = None, open_state = None, fig = None, ax = None, close_plot = True):
    """
    Args:
      1. maze: An instance of the Maze class containing matrix, bonus points, start, and end.
      2. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
      3. open_state: An array of coordinates to color with gray background.
    """
    matrix = maze.matrix
    bonus = maze.bonus_points
    start = maze.start
    goal = maze.goal

    plt.ion()
    # Define walls and an array of direction based on the route
    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0] - route[i - 1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0] - route[i - 1][0] < 0:
                direction.append('^')  # v
            elif route[i][1] - route[i - 1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

    # Drawing the map
    if (fig is None) or ax is None:
        fig = plt.figure(dpi=100)
        ax=fig.add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls], marker='X',s=40,color='black')
    plt.scatter([i[1] for i in bonus], [-i[0] for i in bonus], marker='P', s=40, color='green')
    plt.scatter(start[1], -start[0], marker='*', s=200, color='gold')
    
    if (open_state):
        for i in range(len(open_state)):
            plt.scatter(open_state[i][1], -open_state[i][0], marker='s', s=70, color=(0.95, 0.80, 0.91), alpha=0.7)
            

    if (closed_state):    
        for i in range(len(closed_state)):
            plt.scatter(closed_state[i][1], -closed_state[i][0], marker='o', s=40, color='gold', edgecolors='black', alpha = 0.7)
    
    if route:
        for i in range(1, len(route)):
            plt.scatter(route[i][1], -route[i][0], marker=direction[i-1], color='gold', edgecolors='black')

    if (maze.teleporters):
        for key, value in maze.teleporters.items():
            random_color = generate_random_color()
            for point in value:
                plt.scatter(point[1], -point[0], marker = "d", color = random_color, edgecolors='black')

    plt.text(goal[1], -goal[0], 'EXIT', color='red',
             horizontalalignment='center',
             verticalalignment='center')
    plt.xticks([])
    plt.yticks([])

    # Display the map
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = Image.open(buf)

    if (close_plot):
        plt.close()

    return fig, ax, image


def add_point(fig,ax, route = None, closed_state = None, open_state = None):
    if (open_state):
        for i in range(len(open_state)):
            plt.scatter(open_state[i][1], -open_state[i][0], marker='s', s=70, color=(0.95, 0.80, 0.91), alpha=0.7)
            
    if (closed_state):    
        for i in range(len(closed_state)):
            plt.scatter(closed_state[i ][1], -closed_state[i ][0], marker='o', s=40, color='gold', edgecolors='black', alpha = 0.7)
    
    if route:
        for i in range(len(route) - 2):
            plt.scatter(route[i + 1][1], -route[i + 1][0], marker=direction[i], color='green')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = Image.open(buf)
    return fig, ax, image