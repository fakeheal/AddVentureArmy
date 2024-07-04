import pygame.sprite

from constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT
from resources.colors import COLOR_BLUE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.rect.center = (GAME_WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2, GAME_WINDOW_HEIGHT - PLAYER_HEIGHT / 2)

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

    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_BLUE, self.rect)
