import pygame
from utils import Sprite, SPEED, WIDTH, HEIGHT, NUM_ALIENS, check_collisions
from typing import List


class Alien(Sprite):
    'A class to represent an individual alien'
    def __init__(self, window: pygame.Surface, idx: int):
        self.window = window
        self.idx = idx
        self.size = (80, 80)
        self.reset()

    def reset(self):
        'Resets this alien to it\'s starting position'
        self.x = (self.idx % 5) * 90 + 20
        self.y = (self.idx // 5) * 90 + 5
        if (self.idx // 5) % 2 == 1:
            self.x += 50

    def update(self, right: bool):
        self.y += SPEED/8
        if right:
            self.x += SPEED/3
        else:
            self.x -= SPEED/3


class AlienManager:
    'A class to manage the aliens and their movement'
    def __init__(self, window: pygame.Surface, num: int = NUM_ALIENS):
        self.window = window
        self.alien_image = pygame.image.load("alien.png")
        self.alien_image = pygame.transform.scale(self.alien_image, (80, 80))
        self.aliens = [Alien(self.window, i) for i in range(num)]
        self.right = True

    def reset(self):
        'Resets the aliens to their starting positions'
        for alien in self.aliens:
            alien.reset()

    def update(self, bullets: List["Bullet"]) -> bool:
        'Moves the aliens and checks whether any have died'
        # Checking whether the aliens have hit the sides of the game.
        should_go_left = max(alien.x for alien in self.aliens) >= (WIDTH - 90)
        should_go_right = min(alien.x for alien in self.aliens) <= 10
        if should_go_left and self.right:
            self.right = False
        elif should_go_right and not self.right:
            self.right = True
        # Checking if each alien has been shot and displaying them if not
        for alien in self.aliens:
            if check_collisions(alien, bullets):
                self.aliens.remove(alien)
            alien.update(self.right)
        self.window.blits([(self.alien_image, alien.position) for alien in self.aliens])
        # Error only occurs at the end of the game, and is ok to ignore.
        try:
            # Returns false, indicating the game should end, if the aliens have
            # reached the ground
            return not HEIGHT - max(alien.y for alien in self.aliens) <= 80
        except ValueError:
            return True
