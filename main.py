import sys
import pygame
from pygame.locals import *

from constants import GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT, GAME_TITLE, GAME_FPS
from components.Player import Player
from resources.colors import COLOR_WHITE

pygame.init()

GameWindow = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

FramePerSec = pygame.time.Clock()

P1 = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()

    GameWindow.fill(COLOR_WHITE)
    P1.draw(GameWindow)

    pygame.display.update()
    FramePerSec.tick(GAME_FPS)
