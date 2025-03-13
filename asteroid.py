import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __int__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.velocity += self.velocity * dt
