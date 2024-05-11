import json
import sys

import pygame
from pygame import image
import pygame
from Character import *
from Every_enemy import *

def my_mega_game():
    global settings
    window = pygame.display.set_mode((700, 500))
    fps = pygame.time.Clock()

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("space.ogg")
    pygame.mixer.music.play(-1)

    def read_data():
        global settings
        try:
            with open("settings.json", "r", encoding="utf-8") as file:
                settings = json.load(file)
        except:
            settings = {
                "skin": "img.png",
                "money": 0,
                "player_skin": "img.png"
            }

    def write_data():
        global settings
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)
    read_data()


    abc =Player(100, 100, 50, 50, settings["player_skin"], 6)
    background = pygame.transform.scale(image.load("galaxy.jpg"), (700, 500))





    while True:
        window.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                return


        for bullet in abc.bullets:
            for enemy in enemies:
                if bullet.hitbox.colliderect(enemy.hitbox):
                    settings["money"] += 1
                    write_data()
                    enemy.defeat()


        for enemy in enemies:
            enemy.draw(window)
            enemy.move()

        for bullet in bullets:
            bullet.draw(window)

        abc.move()
        abc.draw(window)

        pygame.display.flip()


        fps.tick(60)