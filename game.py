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
        print("Hooray!" if won else "You suck")

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

    font = pygame.font.Font(None, 50)
    window.blit(font.render("Space Invaders", True, (57, 255, 20)), (WIDTH/2 - 120, HEIGHT/2 - 50))
    font2 = pygame.font.Font(None, 25)
    window.blit(font2.render("Press <space> to begin", True, (57, 255, 20)), (WIDTH/2 - 90, HEIGHT/2))
    pygame.display.flip()
    running = True
    started = False

    while not started:
        for event in pygame.event.get():
            # Checking if window was closed or if q or escape keys were pressed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                started = True
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                started = True
        pygame.time.wait(50)
    pygame.time.wait(250)

    game_mgr = GameManager(window)

    while running:
        for event in pygame.event.get(pygame.QUIT):
            # Checking if window was closed or if q or escape keys were pressed
            running = False

        window.fill(pygame.color.Color(0, 0, 0))
        running = game_mgr.update()
        pygame.display.flip()
        clock.tick(60)
