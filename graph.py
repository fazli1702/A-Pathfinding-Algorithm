from constant import *
import pygame

def h(pos1, pos2):
    '''heuristic function'''
    x1, y1 = pos1
    x2, y2 = pos2
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return x + y

def get_pos_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x, self.y = self.get_coordinate()
        self.colour = WHITE
        self.neighbours = []

    def get_coordinate(self):
        '''return (x, y) coordinate of node in window'''
        x = SQUARE_SIZE * self.col
        y = SQUARE_SIZE * self.row
        return x, y

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.colour = WHITE

    def is_open(self):
        '''check if node in open set'''
        return self.colour == GREEN

    def is_closed(self):
        return self.colour == RED

    def is_wall(self):
        return self.colour == BLACK

    def set_start(self):
        self.colour = ORANGE

    def set_end(self):
        self.colour = PURPLE

    def set_wall(self):
        self.colour = BLACK

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

    def __repr__(self):
        s = 0
        if self.colour != WHITE:
            s = 1
        return str(s)


class Graph:
    def __init__(self, win):
        self.graph = []
        self.win = win
        self.start = None
        self.end = None
        self.create_graph()

    def get_node(self, row, col):
        return self.graph[row][col]

    def update(self):
        self.draw_graph()
        pygame.display.update()

    def create_graph(self):
        for row in range(ROWS):
            curr_row = []
            for col in range(COLS):
                node = Node(row, col)
                curr_row.append(node)
            self.graph.append(curr_row)

    def left_click(self, mouse_coordinate):
        row, col = get_pos_from_mouse(mouse_coordinate)
        node = self.get_node(row, col)

        if not self.start:
            node.set_start()
            self.start = node

        elif not self.end:
            node.set_end()
            self.end = node

        elif node != self.start and node != self.end:
            node.set_wall()


    def right_click(self, mouse_coordinate):
        row, col = get_pos_from_mouse(mouse_coordinate)
        node = self.get_node(row, col)
        node.reset()

        if node == self.start:
            self.start = None

        elif node == self.end:
            self.end = None


    def print_graph(self):
        print(self.graph)

    def draw_grid(self):
        for y in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.line(self.win, GREY, (0, y), (WIDTH, y))

        for x in range(0, WIDTH, SQUARE_SIZE):
            pygame.draw.line(self.win, GREY, (x, 0), (x, HEIGHT))

    def draw_nodes(self):
        for row in self.graph:
            for node in row:
                node.draw(self.win)

    def draw_graph(self):
        '''draw grid and nodes on window'''
        self.win.fill(WHITE)
        self.draw_nodes()
        self.draw_grid()

