#Creating Window by Kristopher Cooper, v0.0
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Maze Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('img/sky.jpg')
ground_surface = pygame.image.load('img/ground.jpg')

while True:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            pygame.quit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,200))
            
    pygame.display.update()
    clock.tick(60)