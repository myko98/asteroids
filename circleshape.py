import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def checkCollision(self, circleShape2):
        distance = pygame.math.Vector2.distance_to(self.position, circleShape2.position)
        sumRadius = self.radius + circleShape2.radius
        return distance <= sumRadius