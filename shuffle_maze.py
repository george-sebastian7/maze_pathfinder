import random

path_modifier = 1.2

def create_maze(x, y):
    # Initialize all cells as walls ('X')
    maze = [['X'] * y for _ in range(x)]

    # Choose a random start and finish position in the maze grid
    start = (random.randint(0, x-1), random.randint(0, y-1))
    finish = (random.randint(0, x-1), random.randint(0, y-1))
    
    # Ensure that start and finish positions are not the same. If they are, 
    # choose a new random position for the finish until they differ
    while start == finish:
        finish = (random.randint(0, x-1), random.randint(0, y-1))
        
    # Mark the start and finish points in the maze
    maze[start[0]][start[1]] = '0'
    maze[finish[0]][finish[1]] = 'F'

    # Randomly create open paths (' ') in the maze. 
    # We create a number of paths equal to 60% of the total number of cells.
    # This factor can be adjusted to make more or less paths.
    for _ in range(int(path_modifier * x * (y - 1))):  # Adjusted to exclude the left edge
        path = (random.randint(0, x-1), random.randint(1, y-1))  # Adjusted to exclude the left edge

        # Ensure that path position is not the same as start or finish. If it is, 
        # choose a new random position for the path until it differs
        while path == start or path == finish:
            path = (random.randint(0, x-1), random.randint(1, y-1))  # Adjusted to exclude the left edge

        maze[path[0]][path[1]] = ' '

    # Make sure the left edge is a wall
    for i in range(x):
        maze[i][0] = 'X'

    # Return the created maze
    return maze

def print_maze(maze):
    # Open a file named "maze" in write mode. 
    # If the file already exists, it gets overwritten. Otherwise, a new file is created.
    with open("maze", 'w') as f:
        # Iterate over each row in the maze
        for row in maze:
            # Join all cells in the row into a single string, and write it to the file.
            # Each row is written as a new line in the file.
            f.write(''.join(row) + '\n')

# Ask user for the number of rows and columns for the maze
x = int(input("Enter the number of rows: "))
y = int(input("Enter the number of columns: "))

# Create a random maze with the specified size
maze = create_maze(x, y)
# Write the generated maze to a file
print_maze(maze)
