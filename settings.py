import ctypes, pygame, pymunk

TITLE_STRING = 'plinko'
FPS = 60

ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1680
HEIGHT = 960
BG_COLOR = (0,0,0)
MULTI_HEIGHT = int(HEIGHT/19) # 56 on 1920 x 1080
MULTI_COLLISION = HEIGHT - (MULTI_HEIGHT * 2) # 968 on 1920x1080
SCORE_RECT = int(WIDTH/16) # 120 on 1920x1080

OBSTACLE_COLOR = (255,0,0)
OBSTACLE_RAD = int(WIDTH/240) # 8 on 1920 x 1080
OBSTACLE_PAD = int(HEIGHT/19) # 56
OBSTACLE_START = (int((WIDTH / 2) - OBSTACLE_PAD), int((HEIGHT - (HEIGHT * .9))))
segmentA_2 = OBSTACLE_START

BALL_COLOR = (255,255,255)
BALL_RAD = int(WIDTH/120)


# keeps track of which were obtained
multipliers = {
    "1000":0,
    "130":0,
    "100":0,
    "26":0,
    "9":0,
    "4":0,
    "2":0,
    "0.2":0



}

# add as needde
multi_rgb = {
    (0,1000): (255,0,0),
    (1,130):(255,30,0),
    (2,26):(255,60,0),
    (3,9):(255,90,0),
    (4,4):(255,120,0),
    (5,2):(255,150,0),
    (6,0.2):(255,180,0),
    (7,0.2):(255,210,0),
    (8,0.2):(255,240,0),
    (9,0.2):(255,210,0),
    (10,0.2):(255,180,0),
    (11,2):(255,150,0),
    (12,4):(255,120,0),
    (13,9):(255,90,0),
    (14,26):(255,60,0),
    (15,130):(255,30,0),
    (16,1000):(255,0,0)

}

# num multipliers
NUM_MULT = 17

# prevent same class collision
BALL_CATEGORY = 1
OBSTACLE_CATEGORY = 2
BALL_MASK = pymunk.ShapeFilter.ALL_MASKS() ^ BALL_CATEGORY
OBSTACLE_MASK = pymunk.ShapeFilter.ALL_MASKS()

