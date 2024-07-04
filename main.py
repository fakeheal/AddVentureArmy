import sys

import pygame.freetype
from pygame.locals import *

from AddVentureArmy import GameWindow, FramePerSec
from components.Enemy import Enemy
from components.Player import Player
from constants import GAME_FPS, ENEMY_POSITION_LEFT, ENEMY_POSITION_RIGHT
from resources.colors import COLOR_WHITE

P1 = Player()
E1 = Enemy(ENEMY_POSITION_LEFT)
E2 = Enemy(ENEMY_POSITION_RIGHT)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    E2.update()

    GameWindow.fill(COLOR_WHITE)

    P1.draw()
    E1.draw()
    E2.draw()

    pygame.display.update()
    FramePerSec.tick(GAME_FPS)
