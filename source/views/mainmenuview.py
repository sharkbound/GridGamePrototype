import arcade as arc
import arcade.key
import arcade.gui
import arcade.color as colors
from ..utils import Bounds, Vector2


class MainMenuView(arc.View):
    def __init__(self):
        super().__init__()
        self.shift = Vector2(1, .5)
        self.bounds = Bounds.from_size(Vector2.zero(), Vector2(50, 100))

    def on_draw(self):
        arc.start_render()

        self.bounds.shift(self.shift)
        arc.draw_circle_filled(*self.bounds.top_left, 10, arc.color.RED)
        arc.draw_circle_filled(*self.bounds.top_right, 10, arc.color.RED_BROWN)
        arc.draw_circle_filled(*self.bounds.bottom_right, 10, arc.color.BLUE)
        arc.draw_circle_filled(*self.bounds.bottom_left, 10, arc.color.LIGHT_BLUE)
