import pygame


class Bullet:
    pass


class Ship:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.image = pygame.image.load("ship.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Starting position
        self.x = 640 / 2 - 25
        self.y = 480 - 50

        self.bullets = []

    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_LEFT]:
            self.x -= 5
        self.window.blit(self.image, self.position)
