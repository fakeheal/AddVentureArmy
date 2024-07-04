import sys

import pygame.freetype
from pygame.locals import *

from AddVentureArmy import FramePerSec, BONUS_HIT, BONUS_SPAWN
from components.Background import Background
from components.Bonus import Bonus
from components.Player import Player
from constants import GAME_FPS, BONUS_POSITION_LEFT, BONUS_POSITION_RIGHT
from resources.problem_randomizer import get_bonus_problems

bonuses = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P = Player()
all_sprites.add(P)

BG = Background()

pygame.time.set_timer(BONUS_SPAWN, 5000)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == BONUS_HIT:
            if event.bonus.alive() and P.can_hit_bonus:
                P.player_score.add_score(event.bonus.problem.operand, event.bonus.problem.value)
                P.can_hit_bonus = False
                event.bonus.kill()
        elif event.type == BONUS_SPAWN:
            P.can_hit_bonus = True
            operand1, value1, operand2, value2 = get_bonus_problems(P.player_score.score)
            B1 = Bonus(BONUS_POSITION_LEFT, operand1, value1)
            B2 = Bonus(BONUS_POSITION_RIGHT, operand2, value2)
            bonuses.add(B1, B2)
            all_sprites.add(B1, B2)

    BG.update()
    BG.draw()

    for sprite in all_sprites:
        sprite.update(pygame.time.get_ticks())
        sprite.draw()

    bonus_hit = pygame.sprite.spritecollideany(P, bonuses)
    if bonus_hit:
        pygame.event.post(pygame.event.Event(BONUS_HIT, {"bonus": bonus_hit}))

    if P.player_score.score <= 0:
        pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    FramePerSec.tick(GAME_FPS)
