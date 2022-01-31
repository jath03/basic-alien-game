import pygame
from aliens import AlienManager
from ship import Ship

WIDTH = 640
HEIGHT = 480
EXTRA_LIVES = 3


class GameManager:
    def __init__(self):

        self.ship = Ship()
        self.alien_mgr = AlienManager()

    def update():
        pass

    def game_over(won: bool):
        pass


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Alien Invasion")
    game_mgr = GameManager()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        game_mgr.update()
