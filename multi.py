from settings import *
import pygame, pygame.gfxdraw

multi_group = pygame.sprite.Group()
clock = pygame.time.Clock()
delta_time = clock.tick(FPS) / 1000.0

class Multi(pygame.sprite.Sprite):
    def __init__(self, position, color, multi_amt):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont(None, 26)
        self.color = color
        self.border_radius = 10
        self.position = position
        self.rect_width, self.rect_height = OBSTACLE_PAD - (OBSTACLE_PAD / 14), MULTI_HEIGHT
        self.image = pygame.Surface((self.rect_width, self.rect_height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), border_radius=self.border_radius)
        self.rect = self.image.get_rect(center=position)
        self.multi_amt = multi_amt
        self.prev_multi = int(WIDTH/21.3)

        # animation stuff, framerate indepdent; we prob will omit these in the future
        self.animated_frames = 0
        self.animation_frames = int(0.25 / delta_time)
        self.is_animating = False

        self.render_multi()

    def render_multi(self):
        text_surface = self.font.render(f"{self.multi_amt}x", True, (0,0,0))
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

    def hit_sound(self):
        pass

    def animate(self, color, amount):
        if self.animated_frames < self.animation_frames // 2:
            self.rect.bottom += 2
        else:
            self.rect.bottom -= 2
        self.animated_frames += 1
        if self.animated_frames == (self.animation_frames // 2) * 2:
            self.is_animating = False
            self.animated_frames = 0

    def update(self):
        if self.is_animating:
            self.animate(self.color, self.multi_amt)