# defining the player sprite 
import pygame
from constants import *
from circleshape import CircleShape
from shots import Shot

class Player(CircleShape):

    # pass player radius to circleshape constructor
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

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

    def rotate(self, dt):
        self.rotation += dt*PLAYER_TURN_SPEED
    
    def update(self, dt):
        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    

    
    def shoot(self):
        if self.shoot_cooldown > 0:
            pass
        else:
            velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            new_shot = Shot(self.position.x, self.position.y, velocity)
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        
        
        
        
