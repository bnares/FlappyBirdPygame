import pygame, sys, random

pygame.init()

width = 280
height = 510
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

#importy zdjec
bgSurface = pygame.image.load("background-day.png").convert()
floorSurface = pygame.image.load("base.png").convert()
birdSurface = pygame.image.load("bluebird-midflap.png").convert()
birdRect = birdSurface.get_rect(center = (width/2-100, height/2))
pipeSurface = pygame.image.load("pipe-green.png").convert()


#ustawiania timera w grze ktora co wyznaczony czas w milsek bedzie uruchamial jakies zdarzenie - pojawienie sie obrazka z rura

SPAWNPIPE = pygame.USEREVENT  #USEREVENT dziala tak jak event loop,  zmienna spawnpipe to nosi nazwe tego wydarzenia
pygame.time.set_timer(SPAWNPIPE, 1200)   #ustalenie co ile czasu wydarzenie spawnpipe bedzie sie powtarzalo
pipeList = []

pipeHeight = [100,200,300]  #random pipe heights


def createPipe():
    randomPipePos = random.choice(pipeHeight) #choose height
    bottomPipe = pipeSurface.get_rect(midtop = (width+200, height- randomPipePos))
    topPipe = pipeSurface.get_rect(midbottom = (width+200, height-randomPipePos-150))
    return bottomPipe, topPipe

def movePipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return  pipes


def drawPipes():
    for i in pipeList:

        if i.bottom>=height-100:
            screen.blit(pipeSurface, i)
        else:
            flipPipe = pygame.transform.flip(pipeSurface, False,True)
            screen.blit(flipPipe,i)



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

        #evry time this ivent below is triggered we wannt to create a pipe
        if event.type == SPAWNPIPE:
            pipeList.extend(createPipe())



    screen.blit(bgSurface, (0,0))
    drawFloor()
    floorXPos -=1
    if floorXPos <-width:
        floorXPos =0

    #bird
    birdRect.centery +=birdMovement
    screen.blit(birdSurface, birdRect)
    clock.tick(60)
    birdMovement+=gravity

    #pipes
    pipeList = movePipes(pipeList)
    drawPipes()

    pygame.display.update()