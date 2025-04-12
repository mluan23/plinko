import pygame, ctypes
import os

# maintain screen resolution
ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 600
HEIGHT = 600

OBSTACLE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "obstacle.png")))


class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0

