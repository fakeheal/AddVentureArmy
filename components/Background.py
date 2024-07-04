import math

import pygame

from AddVentureArmy import GameWindow
from constants import BONUS_SPEED

background = pygame.image.load("resources/images/background_0.png").convert()


class Background:
    def __init__(self):
        self.height = background.get_height()
        self.tiles = math.ceil(GameWindow.get_height() / self.height) + 1
        self.scroll = GameWindow.get_height() - self.height

    def update(self):
        self.scroll += BONUS_SPEED
        if self.scroll >= GameWindow.get_height():
            self.scroll = GameWindow.get_height() - self.height

    def draw(self):
        for i in reversed(range(self.tiles - 1, -1, -1)):
            GameWindow.blit(background, (0, -i * self.height + self.scroll))
