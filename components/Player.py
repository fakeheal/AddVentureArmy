import pygame.sprite

from AddVentureArmy import GameWindow
from components.PlayerScore import PlayerScore
from constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT, PLAYER_SCALE
from resources.SpriteSheet import SpriteSheet

sprite_sheet_image_0 = pygame.image.load("resources/images/player_0.png").convert()
sprite_sheet_image_1 = pygame.image.load("resources/images/player_1.png").convert()
sprite_sheet_0 = SpriteSheet(sprite_sheet_image_0)
sprite_sheet_1 = SpriteSheet(sprite_sheet_image_1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.interval = 100
        self.next_tick = pygame.time.get_ticks() + self.interval

        self.image = sprite_sheet_0.get_image(self.frame, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SCALE)
        self.rect = self.image.get_rect()

        self.rect.center = (
            GAME_WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2 * PLAYER_SCALE,
            GAME_WINDOW_HEIGHT - PLAYER_HEIGHT / 2 * PLAYER_SCALE
        )

        self.player_score = PlayerScore()

    def update(self, ticks):
        if ticks > self.next_tick:
            self.next_tick = ticks + self.interval
            self.frame = (self.frame + 1) % 4

        pressed_keys = pygame.key.get_pressed()

        next_x = self.rect.x

        if pressed_keys[pygame.K_LEFT]:
            next_x += -1 * PLAYER_SPEED
        if pressed_keys[pygame.K_RIGHT]:
            next_x += PLAYER_SPEED

        if next_x < 0:
            next_x = 0
        elif next_x > GAME_WINDOW_WIDTH - PLAYER_WIDTH:
            next_x = GAME_WINDOW_WIDTH - PLAYER_WIDTH

        self.rect.x = next_x

    def draw(self):
        if self.player_score.score >= 100:
            self.image = sprite_sheet_1.get_image(self.frame, PLAYER_WIDTH * 2, PLAYER_HEIGHT, PLAYER_SCALE)
        else:
            self.image = sprite_sheet_0.get_image(self.frame, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SCALE)
        GameWindow.blit(self.image, self.rect)
        self.player_score.draw(self.rect.x, self.rect.y)

    def __str__(self):
        return f"Player: {self.rect.x}, {self.rect.y}"
