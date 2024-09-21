# maze_pathfinder
A simple example of an A* algorithm I pieced together python, feel free to use

# Notes
This program is designed to solve a given maze by finding the shortest path from a start point to an end point 
using the A* (A-Star) pathfinding algorithm. The input to the program is a file containing a grid that represents the maze, 
where '0' represents the start point, 'F' the end point, and 'X' represents a wall or an obstacle. '.' (dot) represents a path the program finds.

It can be run from the pathfinder file, f.e. by opening it, it will solve the maze and display the solution.

The shuffle_maze script lets us create a new random maze based on number of rows and columns
    It needs to be run a couple times to give a solvable maze, or the result needs to be tweaked by hand, but better than having to create mazes by hand completely
        The current modifier should optimize the generation result, feel free to write a better maze genereator using the Astar or other algorithm making sure there will be a path

If there are very few walls, the algorithm gets stuck and can not solve a "maze" finished in a second by a human 
(situation where X appears once in each 30 characters on the grid), but it performs well on regular mazes, 
i was not able to fix this before leaving the project.

# Basic Explanation
1 Node Class: The Node class is created to represent the nodes in the maze. Each node has its parent node (which led to this node), 
its position in the maze, and its g, h, and f values. The g value represents the actual cost from the start node to this node, 
the h value is the heuristic estimated cost from this node to the end node, and f is the total cost which is the sum of g and h.

2 Reading the Maze: The read_maze function reads the maze from the input file and identifies the start and end points.

3 A Search Algorithm*: It starts from the start node, explores the neighbor nodes, updates their costs, and selects the next node 
with the lowest f value. This process is repeated until the end node is reached, or no more nodes can be explored.

4 Path Construction: Once the end node is reached, the program backtracks from the end node to the start node through their parents, which forms the shortest path.

5 Main Function: In the main function, the maze is read from the input file, the astar function is called to compute the shortest path, and then the path is marked on the maze and printed out.

