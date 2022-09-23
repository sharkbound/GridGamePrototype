from typing import Hashable

from .vector2 import Vector2

from .bounds import Bounds


class SpatialHashGrid:
    def __init__(self, cell_size: int):
        self.cell_size = cell_size
        self.buckets = {}
        self.item_to_buckets = {}

    def clear(self):
        self.buckets.clear()
        self.item_to_buckets.clear()

    def hash(self, vector: Vector2):
        return int(vector.xf / self.cell_size), int(vector.yf / self.cell_size)

    def iter_cell_indexes_for_bounds(self, bounds: Bounds):
        for x in range(bounds.bottom_left.x, bounds.bottom_right.x + 1, self.cell_size):
            for y in range(bounds.bottom_left.y, bounds.top_left.y + 1, self.cell_size):
                yield self.hash(Vector2(x, y))

    def add_item(self, item, bounds: Bounds):
        for cell in self.iter_cell_indexes_for_bounds(bounds):
            bucket = self.buckets.setdefault(cell, set())
            bucket.add(item)
            self.item_to_buckets.setdefault(item, []).append(bucket)

    def remove_item(self, item):
        if item not in self.item_to_buckets:
            return False

        for bucket in self.item_to_buckets.get(item, []):
            bucket.discard(item)

        del self.item_to_buckets[item]

    def get_items_at_vector(self, vector: Vector2):
        return tuple(self.buckets.get(self.hash(vector), ()))

    def get_items_in_bounds(self, bounds: Bounds):
        print('--start--')
        items = set()
        for cell in self.iter_cell_indexes_for_bounds(bounds):
            print(cell)
            items.update(self.buckets.get(cell, []))
        return items
