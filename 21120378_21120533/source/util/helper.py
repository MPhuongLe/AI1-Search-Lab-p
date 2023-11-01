
from util.draw_maze import visualize_maze
from util.draw_maze import add_point

from Maze import Maze

import time
import csv
import os

import matplotlib.pyplot as plt

def create_gif_from_images(images, output_gif, duration=500):
    images[0].save(
        output_gif, 
        save_all=True, 
        append_images=images[1:], 
        duration=duration, 
        loop = 0
    )

def export_path_image(maze, path, filename):
    fig = None
    ax = None
    fig, ax, init_image = visualize_maze(maze = maze, fig = fig, ax = ax, route=path, close_plot = True)
    rgb_image = init_image.convert("RGB")
    rgb_image.save(filename, "JPEG")

def export_open_close_image(maze, new_open_state, closed_state, open_close_name):
    fig = None
    ax = None

    total_open_state = []

    for state in new_open_state:
        for point in state:
            total_open_state.append(point)

    fig, ax, init_image = visualize_maze(
        maze = maze, 
        fig = fig, 
        ax = ax, 
        closed_state = closed_state, 
        open_state = total_open_state, 
        close_plot = True)
    
    rgb_image = init_image.convert("RGB")
    rgb_image.save(open_close_name, "JPEG")

def export_gif(maze, path, new_open_state, closed_state, gif_name):
    fig = None
    ax = None
    fig, ax, init_image = visualize_maze(maze = maze, fig = fig, ax = ax, close_plot = False)

    images = [init_image] 
    for i in range(0, len(closed_state) ):
        fig, ax, image = add_point(fig, ax, None, [closed_state[i]], new_open_state[i])
        images.append(image)
    plt.close()

    for i in range(0, len(path)+1):
        fig, ax, image = visualize_maze(maze, path[:i])
        images.append(image)

    
    create_gif_from_images(images, gif_name, duration=50)
    plt.close()

def run_algo_for_file(algo_class, algo_name, heuristic, maze_file, new_folder_txt, new_folder_jpg, new_folder_open_close_jpg, new_folder_gif):
    start_time = time.time()

    maze = Maze(maze_file)

    if (heuristic != None):
        algo = algo_class(maze, heuristic)
    else:
        algo = algo_class(maze)
    algo.search()

    end_time = time.time()

    if (algo.total_weight == None):
        algo.total_weight = "NO"

    elapsed_time = end_time - start_time

    with open(new_folder_txt, "w") as file:
        file.write(str(algo.total_weight))

    total_open_state = 0
    for x in algo.new_open_state:
        total_open_state += len(x)

    print(f"Exporting image for {algo_name}...")
    export_path_image(maze, algo.path, new_folder_jpg)

    print(f"Exporting opened close state image for {algo_name}...")
    export_open_close_image(maze, algo.new_open_state, algo.closed_state, new_folder_open_close_jpg)

    print(f"Exporting gif for {algo_name}...")
    export_gif(maze, algo.path, algo.new_open_state, algo.closed_state, new_folder_gif)

    return algo.total_weight, total_open_state, elapsed_time

def process_for_level(root_folder, algo):
    csv_file = root_folder.replace("input", "output") + ".csv"

    if not os.path.exists("output"):
        os.makedirs("output")
        
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        fieldnames = ("maze", "algorithm", "cost", "open", "time")
        writer.writerow(fieldnames)
        
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith('.txt'): 
                    maze_file_path = os.path.join(foldername, filename)
                    print("---------------------")
                    print("Maze: ", maze_file_path)
                    for algo_class, algo_name, heuristic in algo:
                        input_name = filename.split('.')[0]
                        new_folder = foldername.replace("input", "output")
                        new_folder = os.path.join(new_folder, input_name, algo_name)

                        new_folder_jpg = os.path.join(new_folder, algo_name + ".jpg")
                        new_folder_open_close_jpg = os.path.join(new_folder, algo_name + "_open_close_state.jpg")
                        new_folder_txt = os.path.join(new_folder, algo_name + ".txt")
                        new_folder_gif = os.path.join(new_folder, algo_name + ".gif")

                        if not os.path.exists(new_folder):
                            os.makedirs(new_folder)
                        
                        pCost, pOpened, pTime = run_algo_for_file(algo_class, algo_name, heuristic, maze_file_path, new_folder_txt, new_folder_jpg, new_folder_open_close_jpg, new_folder_gif)
                        writer.writerow((maze_file_path, algo_name, pCost, pOpened, pTime))

                        # Print
                        print("\nAlgorithm:", algo_name)
                        print("Length of path: ", pCost)
                        print("Number of opened nodes: ", pOpened)
                        print(f"Time taken: {pTime} seconds\n")
                        
