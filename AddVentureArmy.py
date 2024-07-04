import pygame.freetype

from constants import GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT, GAME_TITLE

pygame.init()
pygame.font.init()

GameWindow = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

GameFont = pygame.freetype.Font('resources/fonts/monogram.ttf', 48)

FramePerSec = pygame.time.Clock()
