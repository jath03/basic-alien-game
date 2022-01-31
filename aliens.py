import pygame
from utils import Sprite, SPEED


class Alien(Sprite):
    pass


class AlienManager:
    def __init__(self, window: pygame.Surface):
        self.alien_image = pygame.image.load("alien.png")

    def update(self):
        pass
