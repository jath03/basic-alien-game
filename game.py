import pygame
from aliens import AlienManager
from ship import Ship
from utils import WIDTH, HEIGHT


class GameManager:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.ship = Ship(window)
        self.alien_mgr = AlienManager(window)
        self.done = False

    def game_over(self, won: bool):
        if won:
            print("Hooray!")
        else:
            print("You suck")

    def update(self) -> bool:
        if not self.ship.update(self.alien_mgr.aliens) or not self.alien_mgr.update(self.ship.bullets):
            self.game_over(False)
            return False
        if len(self.alien_mgr.aliens) == 0:
            self.game_over(True)
            return False
        return True


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Alien Invasion")

    game_mgr = GameManager(window)
    running = True

    while running:
        for event in pygame.event.get():
            # Checking if window was closed or if q or escape keys were pressed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                running = False

        window.fill(pygame.color.Color(0, 0, 0))
        running = game_mgr.update()
        pygame.display.flip()
        clock.tick(60)
