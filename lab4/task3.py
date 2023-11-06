from pprint import pprint
from PIL import Image, ImageDraw, ImageFont
import random


def random_2d_maze(N):
    EMPTY = '0'
    WALL = '1'
    NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

    maze = {}
    for x in range(N):
        for y in range(N):
            maze[(x, y)] = WALL

    def normalize_maze(maze):
        maze_normal = [[None for x in range(N)] for y in range(N)]
        for y in range(N):
            for x in range(N):
                    maze_normal[y][x] = maze[(x, y)]
        return maze_normal

    def visit(x, y):
        maze[(x, y)] = EMPTY
        while True:
            unvisitedNeighbors = []
            if y > 1 and (x, y - 2) not in hasVisited:
                unvisitedNeighbors.append(NORTH)
            if y < N - 2 and (x, y + 2) not in hasVisited:
                unvisitedNeighbors.append(SOUTH)
            if x > 1 and (x - 2, y) not in hasVisited:
                unvisitedNeighbors.append(WEST)
            if x < N - 2 and (x + 2, y) not in hasVisited:
                unvisitedNeighbors.append(EAST)
            if len(unvisitedNeighbors) == 0:
                return
            else:
                nextIntersection = random.choice(unvisitedNeighbors)
                if nextIntersection == NORTH:
                    nextX = x
                    nextY = y - 2
                    maze[(x, y - 1)] = EMPTY
                elif nextIntersection == SOUTH:
                    nextX = x
                    nextY = y + 2
                    maze[(x, y + 1)] = EMPTY
                elif nextIntersection == WEST:
                    nextX = x - 2
                    nextY = y
                    maze[(x - 1, y)] = EMPTY
                elif nextIntersection == EAST:
                    nextX = x + 2
                    nextY = y
                    maze[(x + 1, y)] = EMPTY

                hasVisited.append((nextX, nextY))
                visit(nextX, nextY)


    hasVisited = [(1, 1)]
    visit(1, 1)

    maze = normalize_maze(maze)

    def desion_handler(maze, desion):
        length = len(maze)
        desion_arr = [[(0, e) for e in range(length)],
                    [(e, length - 1) for e in range(length)],
                    [(length - 1, e) for e in range(length)],
                    [(e, 0) for e in range(length)]][desion]
        check = [(+1, 0), (0, -1), (-1, 0), (0, +1)][desion]
        arr = []
        for e in range(length):
            for j in range(length):
                if (e, j) in desion_arr and not (e in [0, length - 1] and j in [0, length - 1]):
                    arr.append((e, j))
        arr = list(filter(lambda cords: maze[check[0] + cords[0]][check[1] + cords[1]] == "0", arr))
        cord = random.choice(arr)
        return cord, (cord[0] - check[0], cord[1] - check[1])

    def make_enter_and_exit(maze):
        options = list(range(4))
        desion1 = random.choice(options)
        options.remove(desion1)
        desion2 = random.choice(options)
        (y1, x1), (y1_out, x1_out) = desion_handler(maze, desion1)
        (y2, x2), (y2_out, x2_out) = desion_handler(maze, desion2)
        maze[y1][x1] = "0"
        maze[y2][x2] = "0"
        return y1, x1, y2, x2, ((y1_out, x1_out), (y2_out, x2_out))
        

    y1, x1, y2, x2, ((y1_out, x1_out), (y2_out, x2_out)) = make_enter_and_exit(maze)
    return maze, (y1, x1, y2, x2), ((y1_out, x1_out), (y2_out, x2_out))


def get_neib(maze, y, x):
    length = len(maze)
    arr = []
    if y != 0:
        if maze[y - 1][x] == "0":
            arr.append((y - 1, x))
    if y != length - 1:
        if maze[y + 1][x] == "0":
            arr.append((y + 1, x))  
    if x != 0:
        if maze[y][x - 1] == "0":
            arr.append((y, x - 1))
    if x != length - 1:
        if maze[y][x + 1] == "0":
            arr.append((y, x + 1))  
    return arr


def find_way(maze, y1, x1, y2, x2):
    visited = []
    queue = [] 
    back = {}
    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)
        while queue: 
            m = queue.pop(0)
            if m == (y2, x2):
                path = [(y2, x2)]
                next = back[(y2, x2)]
                while next != (y1, x1):
                    path.append(next)
                    next = back[next]
                return path + [(y1, x1)]
            for neighbour in get_neib(graph, *m):
                if neighbour not in visited:
                    back[neighbour] = m
                    visited.append(neighbour)
                    queue.append(neighbour)
    return bfs(visited, maze, (y1, x1))


N = 15
block_size = 50
size = N * block_size
img = Image.new("RGB", (size, size), (255, 255, 255))
font_size = 30
fnt = ImageFont.truetype("/usr/share/fonts/noto/NotoSansMath-Regular.ttf", font_size)

maze, (y1, x1, y2, x2), ((y1_out, x1_out), (y2_out, x2_out)) = random_2d_maze(N)
path = find_way(maze, y1, x1, y2, x2)
# print(y2, x2, " ", y1, x1)
# print(path)

off = block_size - font_size

draw = ImageDraw.Draw(img)
for y in range(N - 1, -1, -1):
    for x in range(N):
        _, _, w, h = draw.textbbox((0, 0), maze[y][x], font=fnt)
        draw.text((x * block_size + (block_size - w) / 2, y * block_size + (block_size - h) / 2 - 4), maze[y][x], font=fnt, fill=(0, 0, 0))
for x in range(0, N * block_size, block_size):
    draw.line([(x, - N * block_size), (x, N * block_size)], fill=(128, 128, 128), width=1)
for y in range(0, N * block_size, block_size):
    draw.line([(- N * block_size, y), (N * block_size, y)], fill=(128, 128, 128), width=1)

off = block_size // 2
path = [(y2_out, x2_out)] + path + [(y1_out, x1_out)]
print(path)
for e in range(len(path) - 1):
    y1, x1 = path[e]
    y2, x2 = path[e + 1]
    draw.line([(x1 * block_size + off, y1 * block_size + off), (x2 * block_size + off,  y2 * block_size + off)], 
              fill=(255, 0, 0), width=2)


img.save("a.png")