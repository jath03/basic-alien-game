import pygame

WIDTH = 640
HEIGHT = 480
EXTRA_LIVES = 3
SPEED = 12


def check_collisions(thing, things: list[object]) -> bool:
    return thing.collision_rect.collidelist([other_thing.collision_rect for other_thing in things]) != -1


class Sprite:
    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)

    @property
    def collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.position, self.size)
