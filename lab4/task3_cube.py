import matplotlib.pyplot as plt
import numpy as np
import random


def random_3d_maze(N):
    EMPTY = '0'
    WALL = '1'
    NORTH, SOUTH, EAST, WEST, UP, DOWN = 'n', 's', 'e', 'w', "u", "d"

    maze = {}
    for x in range(N):
        for y in range(N):
            for z in range(N):
                maze[(x, y, z)] = WALL

    length = len(maze)
    arr = [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]
    t1, t2 = "any1", "any2"
    all = [(0, t1, t2), (t1, 0, t2), (t1, t2, 0), (N - 1, t1, t2), (t1, N - 1, t2), (t1, t2, N - 1)]
    # for a1, a2 in arr:
    #     all.append((x, a1, a2))
    #     all.append((a1, x, a2))
    #     all.append((a1, a2, x))
    checkb = []
    for z, y, x in all:
        z1, y1, x1 = 0, 0, 0
        if z == 0:
            z1 = +1
        if z == N - 1:
            z1 = -1
        if y == 0:
            y1 = +1
        if y == N - 1:
            y1 = -1
        if x == 0:
            x1 = +1
        if x == N - 1:
            x1 = -1
        checkb.append((z1, y1, x1))

    def normalize_maze(maze):
        maze_normal = [[[None for x in range(N)] for y in range(N)] for z in range(N)]
        for z in range(N):
            for y in range(N):
                for x in range(N):
                        maze_normal[z][y][x] = maze[(x, y, z)]
        return maze_normal

    def visit(x, y, z):
        maze[(x, y, z)] = EMPTY
        while True:
            unvisitedNeighbors = []
            if y > 1 and (x, y - 2, z) not in hasVisited:
                unvisitedNeighbors.append(NORTH)
            if y < N - 2 and (x, y + 2, z) not in hasVisited:
                unvisitedNeighbors.append(SOUTH)
            if x > 1 and (x - 2, y, z) not in hasVisited:
                unvisitedNeighbors.append(WEST)
            if x < N - 2 and (x + 2, y, z) not in hasVisited:
                unvisitedNeighbors.append(EAST)
            if z > 1 and (x, y, z - 2) not in hasVisited:
                unvisitedNeighbors.append(UP)
            if z < N - 2 and (x, y, z + 2) not in hasVisited:
                unvisitedNeighbors.append(DOWN)
            if len(unvisitedNeighbors) == 0:
                return
            else:
                nextIntersection = random.choice(unvisitedNeighbors)
                if nextIntersection == NORTH:
                    nextX = x
                    nextY = y - 2
                    nextZ = z
                    maze[(x, y - 1, z)] = EMPTY
                elif nextIntersection == SOUTH:
                    nextX = x
                    nextY = y + 2
                    nextZ = z
                    maze[(x, y + 1, z)] = EMPTY
                elif nextIntersection == WEST:
                    nextX = x - 2
                    nextY = y
                    nextZ = z
                    maze[(x - 1, y, z)] = EMPTY
                elif nextIntersection == EAST:
                    nextX = x + 2
                    nextY = y
                    nextZ = z
                    maze[(x + 1, y, z)] = EMPTY
                elif nextIntersection == UP:
                    nextX = x
                    nextY = y
                    nextZ = z - 2
                    maze[(x, y, z - 1)] = EMPTY
                elif nextIntersection == DOWN:
                    nextX = x
                    nextY = y
                    nextZ = z + 2
                    maze[(x, y, z + 1)] = EMPTY
                hasVisited.append((nextX, nextY, nextZ))
                visit(nextX, nextY, nextZ)


    hasVisited = [(1, 1, 1)]
    visit(1, 1, 1)

    maze = normalize_maze(maze)
    # pprint(maze)
    def desion_handler(maze, desion):
        length = len(maze)
        ch = all[desion]
        # print(all)
        # print(ch)
        desion_arr = []
        for e in range(length):
            for j in range(length):
                cord = list(ch)
                cord[cord.index(t1)] = e
                cord[cord.index(t2)] = j
                desion_arr.append(tuple(cord))
        check = checkb[desion]
        # print(check)
        # arr = [(0, 0), (0, length - 1), (length - 1, 0), (length - 1, length - 1)]
        # print(desion_arr)
        arr = []
        for e in range(length):
            for j in range(length):
                for i in range(length):
                    if (e, j, i) in desion_arr and not (e in [0, length - 1] and j in [0, length - 1] and i not in [0, length - 1]):
                        arr.append((e, j, i))
        # print(arr)
        arr = list(filter(lambda cords: maze[check[0] + cords[0]][check[1] + cords[1]][check[2] + cords[2]] == "0", arr))
        # print(arr)
        cord = random.choice(arr)
        return cord # , (cord[0] - check[0], cord[1] - check[1], cord[2] - check[2])

    def make_enter_and_exit(maze):
        options = list(range(6))
        desion1 = random.choice(options)
        options.remove(desion1)
        desion2 = random.choice(options)
        z1, y1, x1 = desion_handler(maze, desion1)
        z2, y2, x2 = desion_handler(maze, desion2)
        maze[z1][y1][x1] = "0"
        maze[z2][y2][x2] = "0"
        return z1, y1, x1, z2, y2, x2
        

    z1, y1, x1, z2, y2, x2 = make_enter_and_exit(maze)
    return maze, (z1, y1, x1, z2, y2, x2)


def get_neib(maze, z, y, x):
    length = len(maze)
    arr = []
    for dz, dy, dx in [(+1, 0, 0), (-1, 0, 0), (0, +1, 0), (0, -1, 0), (0, 0, +1), (0, 0, -1)]:
        try:
            if maze[z + dz][y + dy][x + dx] == "0":
                arr.append((z + dz, y + dy, x + dx))
        except IndexError:
            ...
    return arr


def find_way(maze, z1, y1, x1, z2, y2, x2):
    visited = []
    queue = [] 
    back = {}
    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)
        while queue: 
            m = queue.pop(0)
            if m == (z2, y2, x2):
                path = [(z2, y2, x2)]
                next = back[(z2, y2, x2)]
                while next != (z1, y1, x1):
                    path.append(next)
                    next = back[next]
                return path + [(z1, y1, x1)]
            for neighbour in get_neib(graph, *m):
                if neighbour not in visited:
                    back[neighbour] = m
                    visited.append(neighbour)
                    queue.append(neighbour)
    return bfs(visited, maze, (z1, y1, x1))


N = 5

maze, (z1, y1, x1, z2, y2, x2) = random_3d_maze(N)
path = find_way(maze, z1, y1, x1, z2, y2, x2)

data_x = []
data_y = []
data_z = []
colors = []
for x in range(N):
    for y in range(N):
        for z in range(N):
            if (z, y, x) in path:
                c = "red"
            elif maze[z][y][x] == "0":
                c = "blue"
            else:
                c = "grey"
            # cord = (x, y, z)
            data_x.append(x)
            data_y.append(y)
            data_z.append(z)
            colors.append(c)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
ax.scatter(data_x, data_y, data_z, c=colors)
plt.show()