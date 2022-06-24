"""
Charles Kellogg

The game board
"""
from snake import Snake
from food import Food


class Board:
    def __init__(self, width, height, grid_size=15):
        # Dimensions
        # Pixel width and height of screen
        self.width = width
        self.height = height

        # Dimensions of the grid
        self.grid_size = grid_size

        # Pixel width of one space in the grid
        self.space_width = self.width / self.grid_size

        # Snake
        self.snake = Snake(self.space_width, self.width)

        # Key presses
        self.pressed_keys = []

        # Food
        self.food = Food(self.space_width, self.width, self.grid_size)

        # Score
        self.score = 0

        # Sprite group
        self.group = None

    def draw(self, surf):
        self.food.draw(surf)
        self.snake.draw(surf)

    def cycle(self):
        self.snake.cycle()

        # Eat the food
        if self.snake.head.rect.colliderect(self.food.rect):
            self.score += 1
            self.add(self.group)
            self.new_food_loc()

    def set_dir(self, direction):
        # Don't allow 180 turnaround
        if self.snake.head.past_dir != (direction + 2) % 4:
            self.snake.head.direction = direction

    def add(self, group):
        self.group = group
        self.snake.add(group)

    def new_food_loc(self):
        new_loc = self.food.new_loc_test()
        if self.snake.in_snake(new_loc[0], new_loc[1]):
            self.new_food_loc()
        else:
            self.food.set_loc(new_loc[0], new_loc[1])
