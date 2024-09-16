import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position, self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # remove drawings on GUI
        self.kill()

        # if already small asteroid, do nothing
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        smaller_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid1.velocity = velocity1 * 1.2

        smaller_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid2.velocity = velocity2 * 1.2






