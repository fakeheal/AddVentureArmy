import sys

import pygame.freetype
from pygame.locals import *

from AddVentureArmy import GameWindow, FramePerSec, BONUS_HIT
from components.Bonus import Bonus
from components.Player import Player
from constants import GAME_FPS, BONUS_POSITION_LEFT, BONUS_POSITION_RIGHT
from resources.colors import COLOR_WHITE

P1 = Player()
B1 = Bonus(BONUS_POSITION_LEFT)
B2 = Bonus(BONUS_POSITION_RIGHT)

# Creating Sprites Groups
bonuses = pygame.sprite.Group()
bonuses.add(B1, B2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, B1, B2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == BONUS_HIT:
            if event.bonus.alive():
                P1.player_score.add_score(event.bonus.problem.operand, event.bonus.problem.value)
                event.bonus.kill()

    GameWindow.fill(COLOR_WHITE)

    for sprite in all_sprites:
        sprite.update()
        sprite.draw()

    bonus_hit = pygame.sprite.spritecollideany(P1, [B1, B2])
    if bonus_hit:
        pygame.event.post(pygame.event.Event(BONUS_HIT, {"bonus": bonus_hit}))

    pygame.display.update()
    FramePerSec.tick(GAME_FPS)
