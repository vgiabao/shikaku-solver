maze = [[0, 0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 20, 0, 0, 8, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 6, 0, 0, 0],
        [10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 6, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0, 0]]


def find_lim(maze, point):
     x = point.x
     y = point.y
     range = 1


def find_children(parent):
    potentials = []
    for child in range(2, parent):
        if parent % child == 0:
            potentials.append([child, int(parent / child)])
    return potentials


class Validpoint():
    def __init__(self, value, x, y, potentials):
        self.value = value
        self.x = x
        self.y = y
        self.potentials = potentials

    # def __tup__(self):
    #     return self.x, self.y


def get_maze(maze, w, h):
    square_points = []
    for y in range(h):
        for x in range(w):
            if maze[y][x] != 0 and isinstance(maze[y][x], int):
                potentials = find_children(maze[y][x])
                point = Validpoint(maze[y][x], x, y, potentials)
                square_points.append(point)
    return square_points


if __name__ == '__main__':
    w = 10
    h = 10
    result = get_maze(maze, w, h)
    for value in result:
        print(value.x, value.y, value.value, value.potentials)
