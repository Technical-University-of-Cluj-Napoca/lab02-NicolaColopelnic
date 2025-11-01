import sys
from collections import deque

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def read_maze(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start_end_points(maze):
    start = None
    target = None
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "S":
                start = (y, x)
            elif maze[y][x] == "T":
                target = (y, x)
    return start, target

def get_neighbors(y, x, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != "#":
            neighbors.append((ny, nx))
    return neighbors

def bfs(maze, start, target):
    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == target:
            break
        for neighbor in get_neighbors(*current, maze):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return reconstruct_path(parent, start, target)

def dfs(maze, start, target):
    stack = [start]
    parent = {start: None}

    while stack:
        current = stack.pop()
        if current == target:
            break
        for neighbor in get_neighbors(*current, maze):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    return reconstruct_path(parent, start, target)

def reconstruct_path(parent, start, target):
    if target not in parent:
        return []

    path = []
    current = target
    while current:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path

def create_path(maze, path, start, target):
    for (y, x) in path:
        if (y, x) != start and (y, x) != target:
            maze[y][x] = f"{RED}*{RESET}"

    sy, sx = start
    ty, tx = target

    maze[sy][sx] = f"{YELLOW}S{RESET}"
    maze[ty][tx] = f"{GREEN}T{RESET}"

def print_maze(maze):
    for row in maze:
        print("".join(row))

def main():
    if len(sys.argv) != 3:
        print("not enough arguments")

    algorithm = sys.argv[1].lower()
    filename = sys.argv[2]

    maze = read_maze(filename)
    start, target = find_start_end_points(maze)

    if algorithm == "bfs":
        path = bfs(maze, start, target)
    elif algorithm == "dfs":
        path = dfs(maze, start, target)
    else:
        print("invalid algorithm")
        return

    if not path:
        print("no path found")
    else:
        create_path(maze, path, start, target)
        print_maze(maze)

if __name__ == "__main__":
    main()
