import sys

import pygame.freetype
from pygame.locals import *

from AddVentureArmy import GameWindow, FramePerSec, BONUS_HIT, BONUS_SPAWN
from components.Bonus import Bonus
from components.Player import Player
from constants import GAME_FPS, BONUS_POSITION_LEFT, BONUS_POSITION_RIGHT
from resources.colors import COLOR_WHITE
from resources.math import get_bonus_problems

bonuses = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
all_sprites.add(P1)

pygame.time.set_timer(BONUS_SPAWN, 5000)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == BONUS_HIT:
            if event.bonus.alive() and P1.can_absorb:
                P1.player_score.add_score(event.bonus.problem.operand, event.bonus.problem.value)
                P1.can_absorb = False
                event.bonus.kill()
        elif event.type == BONUS_SPAWN:
            P1.can_absorb = True
            operand1, value1, operand2, value2 = get_bonus_problems(P1.player_score.score)
            B1 = Bonus(BONUS_POSITION_LEFT, operand1, value1)
            B2 = Bonus(BONUS_POSITION_RIGHT, operand2, value2)
            bonuses.add(B1, B2)
            all_sprites.add(B1, B2)

    GameWindow.fill(COLOR_WHITE)

    for sprite in all_sprites:
        sprite.update()
        sprite.draw()

    bonus_hit = pygame.sprite.spritecollideany(P1, bonuses)
    if bonus_hit:
        pygame.event.post(pygame.event.Event(BONUS_HIT, {"bonus": bonus_hit}))

    pygame.display.update()
    FramePerSec.tick(GAME_FPS)
