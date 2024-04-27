import random

import pygame
from pygame import image
import pygame
from Character import *
enemies = []

for i in range(4):
    enemies.append(Enemy(random.randint(0,700), i * 100, 50, 50, "asteroid.png", 4 ))




