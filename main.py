import pygame 
from pygame.locals import (
     K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import sys
import time
import random
pygame.init()

backgroundimg = 'Backgroundimg.jpg'
restartimg = 'restartbutton.jpg'
sentenceFile = 'words.txt'


color_heading = (255,255,255)
color_text = (255,255,255)
color_results = (255,0,0)
pygame.display.set_caption("Typing Game")
bg_img = pygame.image.load(backgroundimg)
w=612
h=382
screen = pygame.display.set_mode((w, h))
running = True
screen.blit(bg_img,(0,0))
pygame.display.flip()
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False


