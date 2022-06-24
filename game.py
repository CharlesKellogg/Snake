"""
Charles Kellogg

Game Class
"""
import pygame
import sys
from button import Button
from board import Board
from time import sleep


class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up fps
        self.fps = 30
        self.frames_per_sec = pygame.time.Clock()

        # Colors
        self.snake_color = (51, 204, 51)
        self.background_color = (0, 0, 0)
        self.square_color = (255, 255, 255)
        self.food_color = (102, 153, 255)
        self.text_color = (255, 255, 255)
        self.text_alt_color = (102, 153, 255)
        self.game_over_color = (255, 0, 0)

        # Screen dimensions
        self.screen_width = 600
        self.screen_height = 600

        # Fonts
        self.font = pygame.font.SysFont("Verdana", 120)
        self.font_small = pygame.font.SysFont("Verdana", 50)
        self.font_game_over = pygame.font.SysFont("Verdana", 90)
        self.game_over = self.font_game_over.render("GAME OVER", True, self.game_over_color)
        self.snake_cap = self.font.render("SNAKE", True, self.text_color)
        self.start_text = self.font_small.render("START", True, self.text_color)
        self.start_text_alt = self.font_small.render("START", True, self.text_alt_color)

        # Screen number
        self.screen_num = 0

        # Game board
        self.board = Board(self.screen_width, self.screen_height)

    def run(self):
        # Set the display surface
        display_surf = pygame.display.set_mode((self.screen_width, self.screen_height))
        display_surf.fill(self.background_color)
        pygame.display.set_caption("SNAKE")

        # Sprites
        start_button = Button(self.start_text, self.start_text_alt,
                              self.screen_width / 2, self.screen_height * 0.75,
                              200, 100)

        # Sprite groups
        screen_0_buttons = pygame.sprite.Group()
        screen_0_buttons.add(start_button)

        nodes = pygame.sprite.Group()

        for i in range(3):
            self.board.add(nodes)

        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen_num == 0:
                        for entity in screen_0_buttons:
                            entity.click(self)

            # Redraw the background
            display_surf.fill(self.background_color)

            # Screen 0
            if self.screen_num == 0:
                # Draw screen 0 sprites
                for entity in screen_0_buttons:
                    display_surf.blit(entity.image, entity.rect)
                    entity.cycle()

                # Draw title text
                display_surf.blit(self.snake_cap,
                                  (self.screen_width / 2 - self.snake_cap.get_width() / 2,
                                   self.screen_height / 3 - self.snake_cap.get_height() / 2))

            # Screen 1
            elif self.screen_num == 1:
                # Draw screen 1
                self.board.draw(display_surf)

                head = self.board.snake.head

                # Get key input
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP]:
                    self.board.set_dir(0)
                elif pressed_keys[pygame.K_RIGHT]:
                    self.board.set_dir(1)
                elif pressed_keys[pygame.K_DOWN]:
                    self.board.set_dir(2)
                elif pressed_keys[pygame.K_LEFT]:
                    self.board.set_dir(3)

                # Check for collision
                for node in nodes:
                    # If head collides with a mobile node (so we can add nodes on top of existing ones)
                    if head.rect.colliderect(node.rect) \
                            and node.past_dir > 0:
                        self.screen_num = 2

                # Check if we are offscreen
                if head.x < 0 or head.x > self.screen_width or head.y < 0 \
                        or head.y > self.screen_height:
                    self.screen_num = 2

                # Cycle
                self.board.cycle()

            # Screen 2 (Game Over)
            elif self.screen_num == 2:
                # Draw game over message
                display_surf.blit(self.game_over, (self.screen_width / 2
                                                   - self.game_over.get_width() / 2,
                                                   self.screen_height / 4
                                                   - self.game_over.get_height() / 2))

                # Display score
                score_msg = self.font_small.render("Score: %s" % self.board.score, True, self.text_color)
                display_surf.blit(score_msg, (self.screen_width / 2
                                              - score_msg.get_width() / 2,
                                              self.screen_height * (2/3)
                                              - score_msg.get_height() / 2))

                pygame.display.update()

                # Wait 2 seconds, then exit
                sleep(2)
                pygame.quit()
                sys.exit()

            # Update
            pygame.display.update()
            self.frames_per_sec.tick(self.fps)
