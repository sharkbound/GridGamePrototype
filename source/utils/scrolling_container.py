import arcade as arc

from .vector2 import Vector2
from .spatialhashgrid import SpatialHashGrid
from .bounds import Bounds
from .vector_funcs import screen_center


class ScrollingContainer:
    def __init__(self):
        self.center = Vector2.zero()
        self.hashgrid = SpatialHashGrid(20)

    def get_items_in_view(self, size: Vector2):
        return self.hashgrid.get_items_in_bounds(Bounds(self.center - (size.xf / 2, size.yf / 2), self.center + (size.xf / 2, size.yf / 2)))

    def translate_to_screen_coords(self, grid_vec: Vector2):
        return screen_center() + (grid_vec - self.center)

    def shift(self, change: Vector2):
        self.center += change

    def add_item(self, item, bounds: Bounds):
        self.hashgrid.add_item(item, bounds)

    def remove_item(self, item):
        self.hashgrid.remove_item(item)
