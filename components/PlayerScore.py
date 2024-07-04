from AddVentureArmy import GameFont, GameWindow
from resources.colors import COLOR_WHITE


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
        if not self.can_absorb:
            return
        if operand == "+":
            self.score += value
        elif operand == "-":
            self.score -= value
        elif operand == "*":
            self.score *= value
        elif operand == "/":
            self.score /= value
