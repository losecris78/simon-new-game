
import pygame
from pad import Button
import random
from contants import *
from casting.cast import Cast
from color import Color


class Director:
    def __init__(self):
        self.sequence = []
        self.next_step = 0
        self.level = 3
        self.buttons = [
            Button('Blue', (0, 0, 255),    50, 50, 200, 200),
            Button('Yellow', (255, 255, 0), 250, 50, 200, 200),
            Button('green',   (0, 255, 0),    50, 250, 200, 200),
            Button('red',   (255, 0, 0), 250, 250, 200, 200)]
        self._gameover = pygame.mixer.Sound(
            'simon-new-game/sounds/videogamefin.wav')

    def new_sequence(self):
        """generate a sequence of n steps."""
        self.sequence = [random.randint(0,3) for _ in range(self.level)]
        self.next_step = 0
        self.play_demo()
        return self.sequence

    def play_demo(self):
        print(self.sequence)

    def redraw(self, win):
        win.fill((255, 255, 255))
        for b in self.buttons:
            b.draw(win)

    def press_button(self, i):
        expect = self.sequence[self.next_step]
        print(f"pressed button {i}:", self.buttons[i].label)
        print(f"expecting button {expect} at step {self.next_step}")
        if i == expect:
            self.next_step += 1
            print("correct")
            if self.next_step == len(self.sequence):
                print("continue!!")
                self.level += 1
                self.new_sequence()
        else:
            print("Incorrect!")
            self.play_demo()
            self.next_step = 0
            self._gameover.play()
