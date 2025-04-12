#from obstacles import obstacle
from settings import *
import pygame, pymunk

class Board():
    def __init__(self, space):
        self.space = space
        self.display_surface = pygame.display.get_surface()

        #obstacles
        # we can change these as needed
        self.curr_row_count = 3
        self.final_row_count = 18
        self.obstacles_list = []
        self.obstacle_sprites = pygame.sprite.Group()
        self.updated_coords = OBSTACLE_START

        self.make_obstacles()

    def make_obstacles(self):
        while self.curr_row_count <= self.final_row_count:
            for i in range(self.curr_row_count):
                self.obstacles_list.append(self.spawn_obstacle(self.updated_coords, self.space))
                self.updated_coords = (int(self.updated_coords[0] + OBSTACLE_PAD), self.updated_coords[1])
            self.updated_coords = (int(WIDTH - self.updated_coords[0] + (.5 * OBSTACLE_PAD)), int(self.updated_coords[1] + OBSTACLE_PAD))
            self.curr_row_count += 1
        print(self.obstacles_list)
    def spawn_obstacle(self, position, space):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = position
        body.friction = 0.6
        shape = pymunk.Circle(body, OBSTACLE_RAD)
        shape.elasticity = 0.4

        # so ball only collide with the obstacle
        shape.filter = pymunk.ShapeFilter(categories=OBSTACLE_CATEGORY, mask=OBSTACLE_MASK)

        self.space.add(body, shape)
        # obstacle = Obstacle(body.position.x, body.position.y)
        # self.obstacle_sprites(obstacle)
        return shape

    def draw_obstacle(self, obstacles):
        for obstacle in obstacles:
            pos_x = int(obstacle.body.position.x)
            pos_y = int(obstacle.body.position.y)
            pygame.draw.circle(self.display_surface, (255,0,0), (pos_x,pos_y), OBSTACLE_RAD)

    def update(self):
        self.draw_obstacle(self.obstacles_list)