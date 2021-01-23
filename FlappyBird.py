import pygame, sys

pygame.init()

width = 280
height = 510
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()


bgSurface = pygame.image.load("background-day.png").convert()
floorSurface = pygame.image.load("base.png").convert()
birdSurface = pygame.image.load("bluebird-midflap.png").convert()
birdRect = birdSurface.get_rect(center = (width/2, height/2))



#increment values

floorXPos = 0
gravity = 0.25
birdMovement = 0


def drawFloor():
    screen.blit(floorSurface, (floorXPos, height-50))
    screen.blit(floorSurface, (floorXPos+width, height-50))





while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdMovement = 0
                birdMovement -=12


    screen.blit(bgSurface, (0,0))
    drawFloor()
    floorXPos -=1
    if floorXPos <-width:
        floorXPos =0


    birdRect.centery +=birdMovement
    screen.blit(birdSurface, birdRect)
    clock.tick(60)
    birdMovement+=gravity
    pygame.display.update()