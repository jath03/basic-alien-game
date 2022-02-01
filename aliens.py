import pygame
from utils import Sprite, SPEED, WIDTH
from ship import Bullet


class Alien(Sprite):
    def __init__(self, window: pygame.Surface, idx: int):
        self.window = window
        self.size = (80, 80)
        self.x = (idx % 8) * 90 + 20
        self.y = (idx // 8) * 90 + 5
        if (idx // 8) % 2 == 1:
            self.x += 50

    def update(self, right: bool):
        self.y += SPEED/8
        if right:
            self.x += SPEED/3
        else:
            self.x -= SPEED/3


class AlienManager:
    def __init__(self, window: pygame.Surface, num: int = 4):
        self.window = window
        self.alien_image = pygame.image.load("alien.png")
        self.alien_image = pygame.transform.scale(self.alien_image, (80, 80))
        self.aliens = [Alien(self.window, i) for i in range(num)]
        self.right = True

    def check_collisions(self, alien: Alien, bullets: list[Bullet]) -> bool:
        return alien.collision_rect.collidelist([bullet.collision_rect for bullet in bullets]) != -1

    def update(self, bullets: list[Bullet]):
        should_go_left = max(alien.x for alien in self.aliens) >= (WIDTH - 90)
        should_go_right = min(alien.x for alien in self.aliens) <= 10
        if should_go_left and self.right:
            self.right = False
        elif should_go_right and not self.right:
            self.right = True
        for alien in self.aliens:
            if self.check_collisions(alien, bullets):
                self.aliens.remove(alien)
            alien.update(self.right)
        self.window.blits([(self.alien_image, alien.position) for alien in self.aliens])
