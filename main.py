import sys

import pygame
from pygame import image
import pygame
from Character import *
from Every_enemy import *
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)





abc =Player(100, 100, 50, 50, "rocket.png", 6)
background = pygame.transform.scale(image.load("galaxy.jpg"), (700, 500))





while True:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()


    for enemy in enemies:
        enemy.draw(window)
        enemy.move()

    for bullet in bullets:
        bullet.draw(window)

    abc.move()
    abc.draw(window)
    
    pygame.display.flip()


    fps.tick(60)