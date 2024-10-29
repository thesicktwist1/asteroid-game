# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
pygame.init


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print("Screen width: {0}".format(SCREEN_WIDTH))
    print("Screen height: {0}".format(SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroid)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              return
        screen.fill(color="black")
        for things in drawable:
            things.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
        for things in updatable:
            things.update(dt)
        for things in asteroid:
            if player.colliding(things):
                print("GAME OVER!")
                return
            for shot in shots:
                if shot.colliding(things):
                    things.split()
                    shot.kill()        
        



if __name__ == "__main__":
    main()