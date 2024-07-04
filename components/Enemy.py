import pygame

from AddVentureArmy import GameWindow
from components.EnemyProblem import EnemyProblem
from constants import GAME_WINDOW_WIDTH, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_POSITION_LEFT, ENEMY_POSITION_RIGHT, \
    ENEMY_SPEED, ENEMY_OFFSET
from resources.colors import COLOR_RED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.rect = pygame.Rect(0, 0, ENEMY_WIDTH, ENEMY_HEIGHT)
        if position == ENEMY_POSITION_LEFT:
            self.problem = EnemyProblem("-", 1)
            self.rect.center = (
                GAME_WINDOW_WIDTH / 2 - ENEMY_WIDTH / 2 - ENEMY_OFFSET,
                ENEMY_HEIGHT / 2
            )
        elif position == ENEMY_POSITION_RIGHT:
            self.problem = EnemyProblem("+", 1)
            self.rect.center = (
                GAME_WINDOW_WIDTH / 2 + ENEMY_WIDTH / 2 + ENEMY_OFFSET,
                ENEMY_HEIGHT / 2
            )

    def update(self):
        self.rect.y += 1 * ENEMY_SPEED

    def draw(self):
        pygame.draw.rect(GameWindow, COLOR_RED, self.rect)
        self.problem.draw(self.rect.center)
