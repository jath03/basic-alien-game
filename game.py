import pygame
from aliens import AlienManager
from ship import Ship
from utils import WIDTH, HEIGHT, EXTRA_LIVES, NUM_ALIENS


class GameManager:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.ship = Ship(window)
        self.alien_mgr = AlienManager(window)
        self.done = False
        self.lives_remaining = EXTRA_LIVES
        self.mini_ship = pygame.transform.scale(self.ship.image, (20, 20))
        self.score = 0
        self.score_font = pygame.font.Font(None, 10)

    def game_over(self, won: bool) -> bool:
        if won:
            print("Hooray!")
            return False
        else:
            if self.lives_remaining > 0:
                self.alien_mgr.reset()
                self.ship.reset()
                self.lives_remaining -= 1
                return True
            else:
                print("You suck")
                return False

    def update(self) -> bool:
        self.score = NUM_ALIENS - len(self.alien_mgr.aliens)
        window.blit(font.render(f"{self.score}", True, (57, 255, 20)), (5, 5))
        for i in range(self.lives_remaining):
            self.window.blit(self.mini_ship, (i * 25 + 5, HEIGHT - 25))
        if not self.ship.update(self.alien_mgr.aliens) or not self.alien_mgr.update(self.ship.bullets):
            return self.game_over(False)
        if len(self.alien_mgr.aliens) == 0:
            return self.game_over(True)
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
            # Checking if window was closed
            running = False

        window.fill(pygame.color.Color(0, 0, 0))
        running = game_mgr.update()
        pygame.display.flip()
        clock.tick(60)
