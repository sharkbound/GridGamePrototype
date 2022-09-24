from types import SimpleNamespace

import arcade as arc
import arcade.key
import arcade.gui
import arcade.color
from ..utils import (
    Bounds,
    Vector2,
    SpatialHashGrid,
    ScrollingContainer,
    window_size
)


class CircleObject:
    def __init__(self, scrollcontainer: ScrollingContainer, pos: Vector2, size: int, color: tuple):
        self.scroll_container = scrollcontainer
        self.size = size
        self.color = color
        self.pos = pos
        self.bounds = Bounds.from_vector(pos)

    def render(self):
        xy = self.scroll_container.translate_to_screen_coords(self.pos)
        arc.draw_circle_filled(xy.x, xy.y, self.size, self.color)


class MainMenuView(arc.View):
    def __init__(self):
        super().__init__()
        self.mouse_pos = Vector2.zero()
        self.scrolling_container = ScrollingContainer()
        self.objects = {'dot': CircleObject(self.scrolling_container, Vector2(100, 100), 20, arc.color.RED)}
        self.scrolling_container.add_item('dot', self.objects['dot'].bounds)
        self.mouse_buttons = set()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        vel = Vector2(-dx, -dy)
        self.mouse_pos = Vector2(x, y)
        if arc.MOUSE_BUTTON_LEFT in self.mouse_buttons:
            self.scrolling_container.shift(vel)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.mouse_buttons.add(button)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.mouse_buttons.discard(button)

    def on_draw(self):
        arc.start_render()

        for obj_id in self.scrolling_container.get_items_in_view(window_size()):
            self.objects[obj_id].render()
