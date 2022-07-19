from directing.director import Director
from pad import Button
from contants import *
import pygame
import random
import time


def main():

    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Simon Game')

    game = Director()
    game.new_sequence()
    press = pygame.mixer.Sound('simon-game/sounds/touch.wav')
    running = True

    while running:
        pygame.display.update()
        game.redraw(win)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, b in enumerate(game.buttons):
                    if b.isOver(pygame.mouse.get_pos()):
                        game.press_button(i)
                        press.play()

    pygame.quit()


if __name__ == "__main__":
    main()
