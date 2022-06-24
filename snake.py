"""
Charles Kellogg

The snake
Implemented as a singly linked list
"""
from snake_node import SnakeNode


class Snake:
    def __init__(self, space_width, grid_width):
        self.head = SnakeNode(space_width, grid_width)
        self.head.set_loc(grid_width / 2, grid_width / 2)
        self.head.past_x = grid_width / 2
        self.head.past_y = grid_width / 2

    def cycle(self):
        self.head.cycle()

    def draw(self, surf):
        self.head.draw(surf)

    def add(self, group):
        self.head.add(group)

    def in_snake(self, x, y):
        return self.head.in_snake(x, y)
