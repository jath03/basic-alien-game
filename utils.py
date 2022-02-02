import pygame
from typing import List, Tuple

WIDTH = 640
HEIGHT = 480
EXTRA_LIVES = 3
SPEED = 12
NUM_ALIENS = 4


def check_collisions(thing: object, things: List[object]) -> bool:
    return thing.collision_rect.collidelist([other_thing.collision_rect for other_thing in things]) != -1


class Sprite:
    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @property
    def collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.position, self.size)
