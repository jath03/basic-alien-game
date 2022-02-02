import pygame
from utils import Sprite, SPEED, WIDTH, HEIGHT, check_collisions
from typing import List


class Alien(Sprite):
    def __init__(self, window: pygame.Surface, idx: int):
        self.window = window
        self.idx = idx
        self.size = (80, 80)
        self.reset()

    def reset(self):
        self.x = (self.idx % 8) * 90 + 20
        self.y = (self.idx // 8) * 90 + 5
        if (self.idx // 8) % 2 == 1:
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

    def reset(self):
        for alien in self.aliens:
            alien.reset()

    def update(self, bullets: List["Bullet"]) -> bool:
        should_go_left = max(alien.x for alien in self.aliens) >= (WIDTH - 90)
        should_go_right = min(alien.x for alien in self.aliens) <= 10
        if should_go_left and self.right:
            self.right = False
        elif should_go_right and not self.right:
            self.right = True
        for alien in self.aliens:
            if check_collisions(alien, bullets):
                self.aliens.remove(alien)
            alien.update(self.right)
        self.window.blits([(self.alien_image, alien.position) for alien in self.aliens])
        try:
            return not HEIGHT - max(alien.y for alien in self.aliens) <= 80
        except ValueError:
            return True
