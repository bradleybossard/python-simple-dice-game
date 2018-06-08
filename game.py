import pygame
import sys
import os

'''
Objects
'''

'''
Setup
'''

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

worldx = 960
worldy = 720

fps = 40   # frame rate
ani = 4    # animation rate
clock = pygame.time.Clock()
pygame.init()

world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','background.jpg')).convert()
backdropbox = world.get_rect()

world = pygame.display.set_mode([worldx,worldy])

'''
Main Loop
'''
main = True

while main == True:
    world.blit(backdrop, backdropbox)
    # world.fill(BLUE)
    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
