import pygame.sprite

from AddVentureArmy import GameWindow
from components.PlayerScore import PlayerScore
from constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT
from resources.colors import COLOR_BLUE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.rect.center = (GAME_WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2, GAME_WINDOW_HEIGHT - PLAYER_HEIGHT / 2)
        self.player_score = PlayerScore()
        self.can_absorb = True

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        next_x = self.rect.x

        if pressed_keys[pygame.K_LEFT]:
            next_x += -1 * PLAYER_SPEED
        if pressed_keys[pygame.K_RIGHT]:
            next_x += PLAYER_SPEED

        if next_x < 0:
            next_x = 0
        elif next_x > GAME_WINDOW_WIDTH - PLAYER_WIDTH:
            next_x = GAME_WINDOW_WIDTH - PLAYER_WIDTH

        self.rect.x = next_x

    def draw(self):
        pygame.draw.rect(GameWindow, COLOR_BLUE, self.rect)
        self.player_score.draw(self.rect.center)

    def __str__(self):
        return f"Player: {self.rect.x}, {self.rect.y}"
