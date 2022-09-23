from typing import Hashable

from .vector2 import Vector2

from .bounds import Bounds


class HashGrid:
    def __init__(self, cell_size: int):
        self.cell_size = cell_size
        self.buckets = {}
        self.item_to_buckets = {}

    def clear(self):
        self.buckets.clear()
        self.item_to_buckets.clear()

    def hash(self, vector: Vector2):
        return int(vector.x / self.cell_size), int(vector.y / self.cell_size)

    def add(self, item, bounds: Bounds):
        pass
