from contants import *
from casting.actor import Actor
from casting.rectangle import Rectangle
from point import Point
import pyray
import pygame
from pygame import mixer

class Button:
    def __init__(self, label, color, x, y, width, height):
        self.label = label
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y -2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y,self.width, self.height), 0)

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
