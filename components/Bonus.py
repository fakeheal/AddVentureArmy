import pygame

from AddVentureArmy import GameWindow
from components.BonusProblem import BonusProblem
from constants import GAME_WINDOW_WIDTH, BONUS_WIDTH, BONUS_HEIGHT, BONUS_POSITION_LEFT, BONUS_POSITION_RIGHT, \
    BONUS_SPEED, BONUS_OFFSET
from resources.SpriteSheet import SpriteSheet

bonus_image_1 = pygame.image.load("resources/images/bonus_1.png").convert()
bonus_image_0 = pygame.image.load("resources/images/bonus_0.png").convert()
bonus_image_left = SpriteSheet(bonus_image_1)
bonus_image_right = SpriteSheet(bonus_image_0)


class Bonus(pygame.sprite.Sprite):
    def __init__(self, position, operand, value):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, BONUS_WIDTH, BONUS_HEIGHT)
        self.problem = BonusProblem(operand, value)

        if position == BONUS_POSITION_LEFT:
            self.image = bonus_image_left.get_image(0, BONUS_WIDTH, BONUS_HEIGHT, 1)
        elif position == BONUS_POSITION_RIGHT:
            self.image = bonus_image_right.get_image(0, BONUS_WIDTH, BONUS_HEIGHT, 1)

        self.rect = self.image.get_rect()

        center_x = GAME_WINDOW_WIDTH / 2
        center_y = BONUS_HEIGHT / 2

        if position == BONUS_POSITION_LEFT:
            center_x = GAME_WINDOW_WIDTH / 2 - BONUS_WIDTH / 2 - BONUS_OFFSET
        elif position == BONUS_POSITION_RIGHT:
            center_x = GAME_WINDOW_WIDTH / 2 + BONUS_WIDTH / 2 + BONUS_OFFSET

        self.rect.center = (center_x, center_y)

    def update(self, ticks):
        self.rect.y += 1 * BONUS_SPEED

    def draw(self):
        if self.alive() is None:
            return self
        GameWindow.blit(self.image, self.rect)
        self.problem.draw(self.rect.centerx, self.rect.y)

    def __str__(self):
        return f"Bonus: {self.problem.operand} {self.problem.value}"
