import arcade as arc
from .vector2 import Vector2


def screen_center():
    window = arc.get_window()
    return Vector2(window.width / 2, window.height / 2)


def window_size():
    window = arc.get_window()
    return Vector2(window.width, window.height)
