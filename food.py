"""
Charles Kellogg

Food for the snake
"""
from pygame.sprite import Sprite
from pygame import Surface
from pygame import draw
from random import randint


class Food(Sprite):
    def __init__(self, space_width, grid_width, grid_size, color=(102, 153, 255)):
        super().__init__()

        # Dimensions
        self.space_width = space_width

        # Color
        self.color = color

        # Screen width
        self.grid_width = grid_width

        # Size of the grid
        self.grid_size = grid_size

        # Set location reference
        self.x_y_top_left = grid_width / 2
        new_tl = self.x_y_top_left
        while new_tl > 0:
            self.x_y_top_left = new_tl
            new_tl -= self.space_width

        # Actual location
        self.x = self.x_y_top_left + (self.grid_size / 3) * self.space_width
        self.y = self.x_y_top_left + (self.grid_size / 3) * self.space_width

    def draw(self, surf):
        # Set image and location
        self.image = Surface([self.space_width, self.space_width])
        draw.rect(self.image, self.color,
                  (0, 0, self.space_width, self.space_width))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        # Draw
        surf.blit(self.image, self.rect)

    def new_loc_test(self):
        x = self.x_y_top_left + randint(1, self.grid_size - 1) * self.space_width
        y = self.x_y_top_left + randint(1, self.grid_size - 1) * self.space_width
        return x, y

    def set_loc(self, x, y):
        self.x = x
        self.y = y
