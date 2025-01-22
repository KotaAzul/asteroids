import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # shot collision checks asteroid radius. small asteroids get removed. larger asteroids get split in two.
    # random.uniform is used to generate the angles for split asteroids
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            new_ast_1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            new_ast_1.velocity = self.velocity.rotate(random_angle)*1.2

            new_ast_2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            new_ast_2.velocity = self.velocity.rotate(-random_angle)*1.2
