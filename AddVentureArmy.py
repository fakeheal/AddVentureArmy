import pygame.freetype

from constants import GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT, GAME_TITLE

pygame.init()
pygame.font.init()

# Game Window Setup
GameWindow = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Fonts
GameFont = pygame.freetype.Font('resources/fonts/monogram.ttf', 48)

# Clock
FramePerSec = pygame.time.Clock()

# Custom Events
BONUS_HIT = pygame.USEREVENT + 1
BONUS_SPAWN = pygame.USEREVENT + 2
