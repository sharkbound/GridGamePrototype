import arcade as arc
import arcade.key
import arcade.gui
import arcade.color as colors
from ..utils import Bounds, Vector2, SpatialHashGrid


class MainMenuView(arc.View):
    def __init__(self):
        super().__init__()
        self.bounds = Bounds.from_size(Vector2(100, 100), Vector2(50, 100))
        self.hashgrid = SpatialHashGrid(50)
        self.hashgrid.add_item('bounds', self.bounds)
        self.mouse_pos = Vector2.zero()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mouse_pos = Vector2(x, y)

    def on_draw(self):
        arc.start_render()

        if self.hashgrid.get_items_in_bounds(Bounds.from_size(self.mouse_pos, Vector2(50, 50))):
            arc.draw_rectangle_outline(self.bounds.center.xf, self.bounds.center.yf, self.bounds.size.xf, self.bounds.size.yf, color=arc.color.GOLD)
        else:
            arc.draw_rectangle_outline(self.bounds.center.xf, self.bounds.center.yf, self.bounds.size.xf, self.bounds.size.yf, color=arc.color.RED)
