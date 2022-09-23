from .vector2 import Vector2


class Bounds:
    __slots__ = ('top_left', 'top_right', 'bottom_left', 'bottom_right')

    def __init__(self, top_left: Vector2, bottom_right: Vector2):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.top_right = Vector2(self.bottom_right.x, self.top_left.y)
        self.bottom_left = Vector2(self.bottom_right.x, self.top_left.y)

    def __repr__(self):
        return f'<Bounds size={self.top_left - self.bottom_right}>'
