# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

pygame.init

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print("Screen width: {0}".format(SCREEN_WIDTH))
    print("Screen height: {0}".format(SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              return
        screen.fill(color="black")
        pygame.display.flip()






if __name__ == "__main__":
    main()