# Slaughterhouse Five Game for AP English Literature
# Code by Ethan Davenport
# Version 0.0.1
# Build 0005

import os, sys
import pygame
from pygame.locals import *

if not pygame.font:
    print("Warning! Fonts disabled.")
if not pygame.mixer:
    print("Warning! Sound disabled.")

def loadImage(name, colorkey=None):
    fullname = os.path.join("images", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("[ERROR] Could not load image: " + name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def loadSound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join("audio", name)
    try:
        sound = ppygame.mixer.Sound(fullname)
    except pygame.error:
        print("[ERROR] Could not load sound: " + name)
        raise SystemExit
    return sound

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Pygame Sprite Initializer
        self.image, self.rect = loadImage("billy.bmp", -1)
        self.falling = False

    def update(self):
        # keyboard read and pos update go here
        self.rect.midtop = pos
    
    def jump(self):
        # handle jumps here
        pass

