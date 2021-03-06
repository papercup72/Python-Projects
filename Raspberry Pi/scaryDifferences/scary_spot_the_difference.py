import pygame
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))

difference = pygame.image.load('Raspberry Pi/scaryDifferences/spot_the_diff.png')
difference = pygame.transform.scale(difference, (width, height))

screen.blit(difference, (0, 0))
pygame.display.update()

sleep(3)

pygame.quit()