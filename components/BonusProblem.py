from AddVentureArmy import GameFont, GameWindow
from resources.colors import COLOR_WHITE

class BonusProblem:
    def __init__(self, operand, value):
        self.operand = operand
        self.value = value

    def draw(self, center):
        problem_text = f"{self.operand} {self.value if self.value is not None else ''}"
        problem_rect = GameFont.get_rect(problem_text)
        problem_rect.center = center
        GameFont.render_to(GameWindow, problem_rect, problem_text, COLOR_WHITE)
