from .vector2 import Vector2


class Bounds:
    __slots__ = ('top_left', 'top_right', 'bottom_left', 'bottom_right')

    def __init__(self, bottom_left: Vector2, top_right: Vector2):
        self.top_right = Vector2.zero()
        self.bottom_left = Vector2.zero()
        self.top_left = Vector2.zero()
        self.bottom_right = Vector2.zero()

        self.recalculate_corners(bottom_left=bottom_left, top_right=top_right)

    @classmethod
    def from_size(cls, bottom_left: Vector2, size: Vector2):
        return cls(bottom_left, bottom_left + size.abs())

    @property
    def size(self):
        return (self.bottom_left - self.top_right).abs()

    def recalculate_corners(self, bottom_left: Vector2, top_right: Vector2):
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.top_left = Vector2(self.bottom_left.xf, self.top_right.yf)
        self.bottom_right = Vector2(self.top_right.xf, self.bottom_left.yf)

    def shift(self, change: Vector2, inplace=True):
        if not inplace:
            return self.__class__(self.bottom_left + change, self.top_right + change)

        self.recalculate_corners(self.bottom_left + change, self.top_right + change)
        return self

    def __repr__(self):
        return f'<Bounds size={self.size} bottom_left={self.bottom_left} top_right={self.top_right}>'
