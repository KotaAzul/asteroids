# this allows us to use code from
# the open-source pygame library
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # create instance of player object at the center of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    astrofield = AsteroidField()
    # game loop
    while True:
        # event handling

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #rendering
        screen.fill('black')
        for upd in updatable:
            upd.update(dt)
        for drw in drawable:
          drw.draw(screen)

        pygame.display.flip()

        # setting frame rate to 60 fps
        dt = clock.tick(60) / 1000  # converts milliseconds to seconds    

if __name__ == '__main__':
    main()
