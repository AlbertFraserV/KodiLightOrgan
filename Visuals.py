import pygame
from pygame.locals import *
from Audio import Audio
import numpy as np
import random

class Visuals:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.audio = Audio("Alone.mp3")
        self.max_db = self.audio.spectrogram.min()

    def play(self):
        pygame.init()
        running = True
        t = pygame.time.get_ticks()
        getTicksLastFrame = t
        pygame.mixer.music.load("Alone.mp3")
        pygame.mixer.music.play(0)
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        freq_ranges = np.arange(100, len(self.audio.frequencies)-1, 100)
        while running:
            screen.fill((0,0,0))
            pygame.display.flip()
            t = pygame.time.get_ticks()
            deltaTime = (t - getTicksLastFrame) / 1000.0
            getTicksLastFrame = t
            rects = []
            x = 0; y = 0
            for f in range(len(freq_ranges)):
                db = self.audio.get_dbs(pygame.mixer.music.get_pos()/1000.0, self.audio.frequencies[freq_ranges[f]])
                self.draw_rect(screen, (random.randint(0,254),random.randint(0,254),random.randint(0,254)), (50,50), (x,y), self.calc_alpha(self.max_db, db))
                x += 10; y += 10
                rects.append(db)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            # for freq in self.audio.frequencies
        pygame.quit()

    def draw_rect(self, screen, color, size, location, alpha):
        s = pygame.Surface(size, pygame.SRCALPHA)  
        s.fill((color[0],color[1],color[2],round(alpha))) 
        screen.blit(s, location)

    def calc_alpha(self, max_db, db):
        return abs(1-(db/max_db))*255

vis = Visuals(1000,1000)
vis.play()