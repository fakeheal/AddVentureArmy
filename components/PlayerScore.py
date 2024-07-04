from AddVentureArmy import GameFont, GameWindow
from resources.colors import COLOR_WHITE
from resources.math import apply_operation


class PlayerScore:
    def __init__(self):
        self.score = 1
        self.can_absorb = False

    def draw(self, center):
        score_text = str(self.score)
        score_rect = GameFont.get_rect(score_text)
        score_rect.center = center
        GameFont.render_to(GameWindow, score_rect, score_text, COLOR_WHITE)

    def add_score(self, operand, value):
        if self.can_absorb:
            self.score = apply_operation(self.score, operand, value)
