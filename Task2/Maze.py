import random

DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def create_maze(width, height):
    width = width if width % 2 == 1 else width + 1
    height = height if height % 2 == 1 else height + 1
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def in_bounds(x, y):
        return 0 < x < height-1 and 0 < y < width-1

    def carve(x, y):
        maze[x][y] = 0
        random.shuffle(DIRECTIONS)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and maze[nx][ny] == 1:
                maze[x + dx//2][y + dy//2] = 0
                carve(nx, ny)

    carve(1, 1)
    maze[0][1] = 0
    maze[height-1][width-2] = 0
    return maze

def solve_maze(maze):
    height = len(maze)
    width = len(maze[0])
    visited = [[False] * width for _ in range(height)]

    def dfs(x, y):
        if not (0 <= x < height and 0 <= y < width):
            return False
        if maze[x][y] != 0 or visited[x][y]:
            return False
        visited[x][y] = True
        if (x, y) == (height - 1, width - 2):
            maze[x][y] = 2
            return True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            if dfs(x+dx, y+dy):
                maze[x][y] = 2
                return True
        return False

    dfs(0, 1)
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(str(cell) for cell in row))

maze = create_maze(10, 10)
print("Generated Maze:")
print_maze(maze)

solved_maze = solve_maze(maze)
print("\nSolved Maze:")
print_maze(solved_maze)
