# this allows us to use code from
# the open-source pygame library
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # create instance of player object at the center of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    astrofield = AsteroidField()
    # game loop
    while True:

        # setting frame rate to 60 fps
        dt = clock.tick(60) / 1000  # converts milliseconds to seconds 

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

        for ast in asteroids:
            if ast.collision_check(player):
                print('Game over!')
                return
            for shot in shots:
                if ast.collision_check(shot):
                    shot.kill()
                    ast.split()
            

                

  

if __name__ == '__main__':
    main()
