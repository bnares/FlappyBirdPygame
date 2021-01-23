import pygame, sys

pygame.init()

width = 280
height = 510
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()


bgSurface = pygame.image.load("background-day.png").convert()
floorSurface = pygame.image.load("base.png").convert()

#bgSurface = pygame.transform.scale2x(bgSurface)

#increment values

floorXPos = 0


def drawFloor():
    screen.blit(floorSurface, (floorXPos, height-50))
    screen.blit(floorSurface, (floorXPos+width, height-50))



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bgSurface, (0,0))
    drawFloor()
    floorXPos -=1
    if floorXPos <-width:
        floorXPos =0
    clock.tick(60)
    pygame.display.update()