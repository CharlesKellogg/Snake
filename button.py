"""
Charles Kellogg

Class for the start button
"""
from pygame.sprite import Sprite
from pygame import Surface
from pygame import draw
from pygame import mouse


class Button(Sprite):
    def __init__(self, text, text_alt, x, y, width, height,
                 color=(255, 255, 255), alt_color=(102, 153, 255), border_width=5):
        super().__init__()

        # Set colors
        self.color = color
        self.alt_color = alt_color

        self.curr_color = self.color

        # Set border width
        self.border_width = border_width

        # Set text
        self.text = text
        self.text_alt = text_alt

        self.curr_text = self.text

        # Set location
        self.x = x
        self.y = y

        # Set width and height
        self.width = width
        self.height = height

        # Set alt color status
        self.alt = False

        # Set image and location
        self.set_reg()

    def cycle(self):
        if self.rect.collidepoint(mouse.get_pos()):
            if not self.alt:
                self.set_alt()

        else:
            if self.alt:
                self.set_reg()

    def set_reg(self):
        # Set alt color status
        self.alt = False

        self.curr_color = self.color
        self.curr_text = self.text

        self.set_im()

    def set_alt(self):
        self.alt = True

        self.curr_color = self.alt_color
        self.curr_text = self.text_alt

        self.set_im()

    def set_im(self):
        # Set alt image and location
        self.image = Surface([self.width, self.height])
        draw.rect(self.image, self.curr_color,
                  (0, 0, self.width, self.height), self.border_width)
        self.image.blit(self.curr_text, (self.width / 2 - self.curr_text.get_width() / 2,
                                         self.height / 2 - self.curr_text.get_height() / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def click(self, game):
        if self.rect.collidepoint(mouse.get_pos()):
            game.screen_num = 1
            game.board.set_dir(1)
