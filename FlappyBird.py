import pygame, sys

pygame.init()

width = 280
height = 510
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

#importy zdjec
bgSurface = pygame.image.load("background-day.png").convert()
floorSurface = pygame.image.load("base.png").convert()
birdSurface = pygame.image.load("bluebird-midflap.png").convert()
birdRect = birdSurface.get_rect(center = (width/2, height/2))
pipeSurface = pygame.image.load("pipe-green.png").convert()


#ustawiania timera w grze ktora co wyznaczony czas w milsek bedzie uruchamial jakies zdarzenie - pojawienie sie obrazka z rura

SPAWNPIPE = pygame.USEREVENT  #USEREVENT dziala tak jak event loop,  zmienna spawnpipe to nosi nazwe tego wydarzenia
pygame.time.set_timer(SPAWNPIPE, 1200)   #ustalenie co ile czasu wydarzenie spawnpipe bedzie sie powtarzalo





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

        if event.type == SPAWNPIPE:
            print("pipe")


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