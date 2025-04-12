import pygame, ctypes
import os

import pymunk

from settings import *
from obstacles import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, position, space, board, delta_time):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.space = space
        self.board = board
        self.delta_time = delta_time
        # cause it moves
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, BALL_RAD)
        self.shape.elasticity = 0.9
        self.shape.density = 10000
        self.shape.mass = 1000
        self.shape.filter = pymunk.ShapeFilter(categories=BALL_CATEGORY, mask=BALL_MASK)
        self.space.add(self.body, self.shape)
        self.image = pygame.Surface((BALL_RAD * 2, BALL_RAD * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.body.position.x, self.body.position.y))

    def update(self):
        pos_x = int(self.body.position.x)
        pos_y = int(self.body.position.y)
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        pygame.draw.circle(self.display_surface, BALL_COLOR, (pos_x, pos_y), BALL_RAD)


