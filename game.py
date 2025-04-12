import ctypes, pygame, sys, pymunk
import random

from ball import Ball
from settings import *
from board import *
from obstacles import *


ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        # pymunk handles game physics
        self.space = pymunk.Space()
        self.space.gravity = (0, 1800)

        #plinko setup
        self.ball_group = pygame.sprite.Group()
        self.board = Board(self.space)

        # debugger
        self.balls_played = 0

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    # so we would like to change this for later
                    random_x = WIDTH//2 + random.choice([random.randint(-20,-1), random.randint(1,20)])
                    # delta time helps get close to agnostic game
                    self.ball = Ball((random_x, 20), self.space, self.board, self.delta_time)
                    self.ball_group.add(self.ball)
                    # self.balls_played += 1
                    # print(self.balls_played)


            self.screen.fill(BG_COLOR)

            # helps take care of phsics
            self.delta_time = self.clock.tick(FPS) / 1000.0
            #self.start_time = pygame.time.get_ticks()
            #self.clock.tick(FPS)

            # pymunk
            self.space.step(self.delta_time)
            self.board.update()
            self.ball_group.update()


            pygame.display.update()
            # for ball in self.ball_group:
            #     self.ball_group.remove(ball)


if __name__ == '__main__':
    game = Game()
    game.run()