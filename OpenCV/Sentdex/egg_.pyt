#The egg and basket game

import pygame
from pygame.locals import *
import time
import random
clock = pygame.time.Clock()
x=260
y=500
#Screen initialize
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("egg")

#Background
cloud=pygame.image.load("clouds.png").convert_alpha()
cloud=pygame.transform.scale(cloud,(600,600))
screen.blit(cloud,(0,0))

#Basket
basket=pygame.image.load("basket.png").convert_alpha()
basket=pygame.transform.scale(basket,(80,80))
screen.blit(basket,(x,y))
pygame.display.update()

#egg
egg=pygame.image.load("eggs.png").convert_alpha()
egg=pygame.transform.scale(egg,(20,20))

#screen.blit(egg,(290,20))
pygame.display.update()

#Movement of basket
ychange=0
xchange=0
exiting=False


xegg = random.randrange(50,550)
yegg = 20
while not exiting:
#xegg=random.randrange(50,550)
#for yegg in range(20,550):
    print yegg
    if yegg<550:
        yegg += 5
        pygame.display.update()
        clock.tick(60)
        screen.blit(egg,(xegg,yegg))

    else:
        yegg=20
        xegg = random.randrange(50,550)
        yegg=yegg+ychange
        pygame.display.update()
        clock.tick(60)
        screen.blit(egg,(xegg,yegg))
    #yegg=20
    pygame.display.update()
    clock.tick(60)
    #yegg=20

    for event in pygame.event.get():
        print(event)
        if(event.type==pygame.QUIT):
            exiting=True
            pygame.quit()
            quit()
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                xchange=-5
            if(event.key==pygame.K_RIGHT):
                xchange=5
        screen.blit(basket,(x,y))
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                xchange=0

        x=x+xchange
        print(x)
        screen.blit(cloud,(0,0))

        screen.blit(basket,(x,y))

        pygame.display.update()
        clock.tick(60)

i=i+1
ychange=0
    #random position of eggs

    #MOVEMENT OF egg