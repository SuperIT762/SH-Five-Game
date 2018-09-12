# Slaughterhouse Five Game for AP English Literature
# Code by Ethan Davenport
# Version 0.0.1
# Build 0006

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
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print("[ERROR] Could not load sound: " + name)
        raise SystemExit
    return sound

#class Player(pygame.sprite.Sprite):
#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self) # Pygame Sprite Initializer
#        self.image, self.rect = loadImage("billy.bmp", -1)
#        self.falling = False

#    def update(self):
#        # keyboard read and pos update go here
#        # handle animation
#        self.rect.midtop = pos
    
#    def jump(self):
#        # handle jumps here
#        pass

#class BgObj(pygame.sprite.Sprite, img, clrKy):
#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self) # Pygame Sprite Initializer
#        self.image, self.rect = loadImage(img, clrKy)
#        screen = pygame.display.get_surface()
#        self.area = screen.get_rect()
#        self.frame = 0

class GameObject(pygame.sprite.Sprite):
    # A general object class to hold various on screen objects
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.visible = True
        self.layer = 0

    def update():
        if self.visible:


    def vanish():
        self.visible = False

    def appear():
        self.visible = True

    def toggleVisible():
        self.visible = not self.visible

    def setLayer(newLayer):
        if newLayer >= 0:
            self.layer = newLayer
        else:
            self.layer = 0

    def getVisible():
        return self.visible

    def getLayer():
        return self.layer

        