# Importing the heapq module for priority queue operations
import heapq

# File name of the maze to be solved
maze_file = "maze"


# A class to represent a maze node  
class Node:
    def __init__(self, parent=None, position=None):
        # The node that led to this node
        self.parent = parent
        # The position of this node
        self.position = position

        # Cost from start to current node  (could be one line with three =, but i wanted to separate these)
        self.g = 0
        # Estimated cost from current node to goal
        self.h = 0
        # Total cost
        self.f = 0

    # Equality check based on node's position
    def __eq__(self, other):
        return self.position == other.position
    
    # For priority queue that prioritizes smaller f value
    def __lt__(self, other):
        return self.f < other.f


# Function to read the maze file and identify start and end positions
def read_maze():
    with open(maze_file, 'r') as f:
        # Create a list of lists representing the maze
        maze = [list(line.strip()) for line in f]

    # find start and end positions
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '0':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)

    return maze, start, end


# Function implementing A* search algorithm
def astar(maze, start, end):
    # Create start and end nodes
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = set()

    # Add the start node
    heapq.heappush(open_list, (start_node.f, start_node))

    # Loop until you find the end
    while open_list:
        # Get the node with the lowest f(x) value
        _, current_node = heapq.heappop(open_list)

        # Found the goal
        if current_node.position == end_node.position:
            # Return reversed path
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] 

        # Mark node as explored
        closed_list.add(current_node.position)

        # Generate children nodes
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Ensure node is within the parameters of the maze
            if (
                node_position[0] < 0
                or node_position[0] >= len(maze)
                or node_position[1] < 0
                or node_position[1] >= len(maze[node_position[0]])
                or maze[node_position[0]][node_position[1]] == 'X'
                or node_position in closed_list
            ):
                continue

            # Create new node and append it to children
            new_node = Node(current_node, node_position)
            children.append(new_node)

        # Loop through children
        for child in children:
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            # If child is already in the open list and has larger g value, skip
            for _, open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    break
            else:
                # Add the child to the open list
                heapq.heappush(open_list, (child.f, child))

    return None  # Return None if no path is found


def main():
    maze, start, end = read_maze()
    path = astar(maze, start, end)

    # If a path is found, mark it on the maze and print
    if path is not None:
        for position in path:
            if maze[position[0]][position[1]] not in ('0', 'F'):
                maze[position[0]][position[1]] = '.'

        for row in maze:
            print(''.join(row))
    else:
        print("No path found in the maze.")

    # Wait for q to quit
    input("Press 'Q' to quit the program: ")


if __name__ == '__main__':
    main()  # Run the main function
