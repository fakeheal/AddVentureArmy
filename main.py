import math
import sys

import pygame.freetype
from pygame.locals import *

from AddVentureArmy import GameWindow, FramePerSec, BONUS_HIT, BONUS_SPAWN
from components.Bonus import Bonus
from components.Player import Player
from constants import GAME_FPS, BONUS_POSITION_LEFT, BONUS_POSITION_RIGHT, BONUS_SPEED
from resources.problem_randomizer import get_bonus_problems

bonuses = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
all_sprites.add(P1)

background = pygame.image.load("resources/images/background_0.png").convert()
bg_height = background.get_height()
bg_tiles = math.ceil(GameWindow.get_height() / bg_height) + 1
bg_scroll = GameWindow.get_height() - bg_height

pygame.time.set_timer(BONUS_SPAWN, 5000)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == BONUS_HIT:
            if event.bonus.alive() and P1.can_hit_bonus:
                P1.player_score.add_score(event.bonus.problem.operand, event.bonus.problem.value)
                event.bonus.kill()
        elif event.type == BONUS_SPAWN:
            P1.can_hit_bonus = True
            operand1, value1, operand2, value2 = get_bonus_problems(P1.player_score.score)
            B1 = Bonus(BONUS_POSITION_LEFT, operand1, value1)
            B2 = Bonus(BONUS_POSITION_RIGHT, operand2, value2)
            bonuses.add(B1, B2)
            all_sprites.add(B1, B2)

    for i in reversed(range(bg_tiles - 1, -1, -1)):
        GameWindow.blit(background, (0, -i * bg_height + bg_scroll))

    bg_scroll += BONUS_SPEED

    if bg_scroll >= GameWindow.get_height():
        bg_scroll = GameWindow.get_height() - bg_height

    for sprite in all_sprites:
        sprite.update(pygame.time.get_ticks())
        sprite.draw()

    bonus_hit = pygame.sprite.spritecollideany(P1, bonuses)
    if bonus_hit:
        pygame.event.post(pygame.event.Event(BONUS_HIT, {"bonus": bonus_hit}))

    if P1.player_score.score <= 0:
        pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    FramePerSec.tick(GAME_FPS)
