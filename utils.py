
WIDTH = 640
HEIGHT = 480
EXTRA_LIVES = 3
SPEED = 12

class Sprite:
    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)
