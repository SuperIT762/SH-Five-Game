# Slaughterhouse Five Game for AP English Literature
# Code by Ethan Davenport
# Version 0.0.1
# Build 0010
import os, sys, time
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

class GameLevel():
    pass

class GameObject(pygame.sprite.Sprite):
    # A general object class to hold various on screen objects
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.visible = True
        self.layer = 0

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

def gameInit():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Slaughterhouse Five: The Game")
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((5, 5, 5))
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Loading...", 1, (255, 255, 255))
        textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() / 2)
        background.blit(text, textpos)
    return screen, background

def main():
    screen, background = gameInit()
    screen.blit(background, (0, 0))
    pygame.display.flip()
    print("[INFO] Game Window Created")
    time.sleep(5)

main()