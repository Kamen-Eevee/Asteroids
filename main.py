import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #player.update(dt)
        for item in updatable:
            item.update(dt)

        for item in asteroids:
            collision_with_player = player.collision_check(item)
            if collision_with_player:
                print("Game over!")
                return
            for bullet in shots:
                collision_with_bullet = bullet.collision_check(item)
                if collision_with_bullet:
                    item.split()
                    bullet.kill()

        screen.fill("black")

        #player.draw(screen)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()