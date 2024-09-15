import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adds all instances of Player class to the two groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable)

    player = Player(x,y)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for thing in updateable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game Over!")
                sys.exit()
        pygame.display.flip()

        # Limits game to 60fps
        # no code goes after this line
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()