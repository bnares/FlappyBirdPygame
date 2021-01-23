import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500,680))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)