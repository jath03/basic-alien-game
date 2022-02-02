import pygame
from utils import Sprite, SPEED, check_collisions
from typing import List


class Bullet(Sprite):
    def __init__(self, window: pygame.Surface, pos: int):
        self.window = window
        self.size = (10, 10)
        self.x = pos
        self.y = 480 - 60

    def update(self):
        self.y -= int(SPEED)
        pygame.draw.circle(self.window, (255, 0, 0), self.position, self.size[0]/2)


class Ship(Sprite):
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.size = (60, 60)
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, self.size)

        self.reset()

    def reset(self):
        # Starting position
        self.x = 640 / 2 - 25
        self.y = 480 - 60

        self.last_bullet = 0
        self.bullets = []

    def shoot(self):
        if pygame.time.get_ticks() - self.last_bullet > 250:
            self.bullets.append(Bullet(self.window, self.x + 30))
            self.last_bullet = pygame.time.get_ticks()

    def update(self, aliens: List["Alien"]) -> bool:
        dead = check_collisions(self, aliens)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += SPEED/2
        if keys[pygame.K_LEFT]:
            self.x -= SPEED/2
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.window.blit(self.image, self.position)
        for bullet in self.bullets:
            bullet.update()
        return not dead
