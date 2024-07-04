from AddVentureArmy import GameFont, GameWindow
from resources.colors import COLOR_WHITE
from resources.problem_randomizer import apply_operation


class PlayerScore:
    def __init__(self):
        self.score = 1

    def draw(self, x, y):
        score_text = str(self.score)
        score_rect = GameFont.get_rect(score_text)
        score_rect.x = x
        score_rect.y = y - 30
        GameFont.render_to(GameWindow, score_rect, score_text, COLOR_WHITE)

    def add_score(self, operand, value):
        self.score = apply_operation(self.score, operand, value)
