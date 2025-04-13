from obstacles import *
from settings import *
import pygame, pymunk
from multi import *

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

        self.segmentA_2 = OBSTACLE_START

        self.make_obstacles()

    def make_obstacles(self):
        while self.curr_row_count <= self.final_row_count:
            for i in range(self.curr_row_count):
                if self.curr_row_count == 3 and self.updated_coords[0] > OBSTACLE_START[0] + OBSTACLE_PAD:
                    self.segmentB_1 = self.updated_coords
                elif self.curr_row_count == self.final_row_count and i ==0:
                    self.segmentA_1 = self.updated_coords
                elif self.curr_row_count == self.final_row_count and i == self.final_row_count - 1:
                    self.segmentB_2 = self.updated_coords
                self.obstacles_list.append(self.spawn_obstacle(self.updated_coords, self.space))
                self.updated_coords = (int(self.updated_coords[0] + OBSTACLE_PAD), self.updated_coords[1])
            self.updated_coords = (int(WIDTH - self.updated_coords[0] + (.5 * OBSTACLE_PAD)), int(self.updated_coords[1] + OBSTACLE_PAD))
            self.curr_row_count += 1
        self.multi_x, self.multi_y = self.updated_coords[0] + OBSTACLE_PAD, self.updated_coords[1]

        # make boundaries
        self.spawn_segments(self.segmentA_1, self.segmentA_2, self.space)
        self.spawn_segments(self.segmentB_1, self.segmentB_2, self.space)
        self.spawn_segments((self.segmentA_2[0], 0), self.segmentA_2, self.space)
        self.spawn_segments(self.segmentB_1, (self.segmentB_1[0], 0), self.space)

        self.spawn_multis()


    def spawn_multis(self):
        self.multi_amounts = [val[1] for val in multi_rgb.keys()]
        self.rgb_vals = [val for val in multi_rgb.values()]
        for i in range(NUM_MULT):
            multi = Multi((self.multi_x, self.multi_y), self.rgb_vals[i], self.multi_amounts[i])
            multi_group.add(multi)
            self.multi_x += OBSTACLE_PAD

    #def draw_multis(self, multi_group):
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
            pygame.draw.circle(self.display_surface, OBSTACLE_COLOR, (pos_x,pos_y), OBSTACLE_RAD)

    def spawn_segments(self, pointA, pointB, space):
        segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        segment_shape = pymunk.Segment(segment_body, pointA, pointB, 5)
        self.space.add(segment_body, segment_shape)

    def update(self):
        self.draw_obstacle(self.obstacles_list)
        multi_group.draw(self.display_surface)
        multi_group.update()
