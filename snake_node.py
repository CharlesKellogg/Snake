"""
Charles Kellogg

A node in the snake
"""
from pygame.sprite import Sprite
from pygame import Surface
from pygame import draw


class SnakeNode(Sprite):
    def __init__(self, space_width, grid_width, past_dir=-1, frame=0, color=(51, 204, 51)):
        super().__init__()

        # Dimensions
        self.space_width = space_width

        # Color
        self.color = color

        # Location
        self.x = 0
        self.y = 0

        self.past_x = 0
        self.past_y = 0

        # Next node
        self.next = None

        # Direction of next move
        self.direction = past_dir

        # Direction of previous move
        self.past_dir = past_dir

        # Frame
        self.frame = frame

        # Screen width
        self.grid_width = grid_width

    def set_im(self, x, y):
        # Set image and location
        self.image = Surface([self.space_width, self.space_width])
        draw.rect(self.image, self.color,
                  (0, 0, self.space_width, self.space_width))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def cycle(self):
        # Increment the frame
        self.frame += 1

        # Only move every 5 frames
        if self.frame % 5 == 0:
            # Note this x and y and direction
            self.past_x = self.x
            self.past_y = self.y

            self.past_dir = self.direction

            # Move in a direction
            if self.direction == 0:
                self.set_loc(self.x, self.y - self.space_width)
            elif self.direction == 1:
                self.set_loc(self.x + self.space_width, self.y)
            elif self.direction == 2:
                self.set_loc(self.x, self.y + self.space_width)
            elif self.direction == 3:
                self.set_loc(self.x - self.space_width, self.y)

        if self.next is not None:
            # Cycle the next node before updating
            self.next.cycle()

            # Pass frame and direction to the next node
            self.next.frame = self.frame
            self.next.direction = self.past_dir

    def draw(self, surf):
        # Update to current location
        self.set_im(self.x, self.y)

        if self.next is not None:
            self.next.draw(surf)

        # Draw
        surf.blit(self.image, self.rect)

    def add(self, group):
        if self.next is None:
            self.next = SnakeNode(self.space_width, self.past_dir)
            self.next.set_loc(self.past_x, self.past_y)
            self.next.past_x = self.past_x
            self.next.past_y = self.past_y
            group.add(self.next)
        else:
            self.next.add(group)

    def set_loc(self, x, y):
        self.x = x
        self.y = y

    def in_snake(self, x, y):
        if self.x == x and self.y == y:
            return True

        if self.next is None:
            return False

        return self.next.in_snake(x, y)
