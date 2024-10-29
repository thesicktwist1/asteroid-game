from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
   
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand = random.uniform(20 , 50)
            blue_angle = self.velocity.rotate(rand)
            red_angle = self.velocity.rotate(-rand)
            blue_aste = Asteroid(self.position.x, self.position.y , self.radius - ASTEROID_MIN_RADIUS)
            red_aste = Asteroid(self.position.x, self.position.y , self.radius - ASTEROID_MIN_RADIUS)
            blue_aste.velocity = blue_angle * 1.2
            red_aste.velocity = red_angle * 1.2
