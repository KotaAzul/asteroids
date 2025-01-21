# defining the player sprite 
import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):

    # pass player radius to circleshape constructor
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # creating the triangle shape the player will see
    # even though the player hitbox will be a circle with PLAYER_RADIUS size
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)