import arcade as arc
import arcade.key
import arcade.gui
import arcade.color as colors
from ..utils import Bounds, Vector2


class MainMenuView(arc.View):
    def __init__(self):
        super().__init__()
        print(Bounds(Vector2(20, 20), Vector2(40, 40)))

    def on_draw(self):
        arc.start_render()
        arc.draw_text('Hello There!', self.window.width / 2, self.window.height / 2, font_size=30, color=arc.color.TEAL, anchor_x='center',
                      anchor_y='center')
        arc.draw_circle_filled(0, 0, 40, arc.color.RED)
