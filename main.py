import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT,))
    while True:

        # Quit from the program
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0,))
        pygame.display.flip()


if __name__ == "__main__":
    main()
