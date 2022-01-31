import pygame
from utils import Sprite


class Bullet(Sprite):
    def __init__(self, window: pygame.Surface, pos: int):
        self.window = window
        self.x = pos
        self.y = 480 - 60

    def update(self):
        self.y -= 4
        pygame.draw.circle(self.window, (255, 0, 0), self.position, 5)


class Ship(Sprite):
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.image = pygame.image.load("ship.jpg")
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Starting position
        self.x = 640 / 2 - 25
        self.y = 480 - 50

        self.last_bullet = 0
        self.bullets = []

    def shoot(self):
        if pygame.time.get_ticks() - self.last_bullet > 250:
            self.bullets.append(Bullet(self.window, self.x + 30))
            self.last_bullet = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.window.blit(self.image, self.position)
        for bullet in self.bullets:
            bullet.update()
