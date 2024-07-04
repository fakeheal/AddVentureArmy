import pygame

from AddVentureArmy import GameWindow
from components.BonusProblem import BonusProblem
from constants import GAME_WINDOW_WIDTH, BONUS_WIDTH, BONUS_HEIGHT, BONUS_POSITION_LEFT, BONUS_POSITION_RIGHT, \
    BONUS_SPEED, BONUS_OFFSET
from resources.colors import COLOR_RED


class Bonus(pygame.sprite.Sprite):
    def __init__(self, position, operand, value):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, BONUS_WIDTH, BONUS_HEIGHT)
        self.problem = BonusProblem(operand, value)

        center_x = GAME_WINDOW_WIDTH / 2
        center_y = BONUS_HEIGHT / 2

        if position == BONUS_POSITION_LEFT:
            center_x = GAME_WINDOW_WIDTH / 2 - BONUS_WIDTH / 2 - BONUS_OFFSET
        elif position == BONUS_POSITION_RIGHT:
            center_x = GAME_WINDOW_WIDTH / 2 + BONUS_WIDTH / 2 + BONUS_OFFSET

        self.rect.center = (center_x, center_y)

    def update(self):
        self.rect.y += 1 * BONUS_SPEED

    def draw(self):
        if self.problem is None:
            return self
        pygame.draw.rect(GameWindow, COLOR_RED, self.rect)
        self.problem.draw(self.rect.center)

    def __str__(self):
        return f"Bonus: {self.problem.operand} {self.problem.value}"
