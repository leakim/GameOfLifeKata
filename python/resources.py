#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Resources to make it easier and faster to implement and test game of life
#
# @author Mikael Wikström
# https://github.com/leakim/GameOfLifeKata
#
import pygame

class GameOfLife:
    # still
    BLOCK_0 = set([(0, 0), (0, 1), (1, 0), (1, 1)])
    BLOCK_1 = BLOCK_0

    # oscillators
    THREE_0 = set([(0, 1), (0, 0), (0, 2)])
    THREE_1 = set([(0, 1), (-1, 1), (1, 1)])

    # spaceships (moves)
    GLIDER_0 = set([(0, 1), (1, 2), (0, 0), (0, 2), (2, 1)])
    GLIDER_1 = set([(0, 1), (1, 2), (-1, 1), (1, 0), (0, 2)])

def move(state, (x, y)):
    newstate = set()
    for (u, v) in state:
        newstate.add((x + u, y + v))
    return newstate

#WINDOW_SIZE = [2*255, 2*255]
#screen = pygame.display.set_mode(WINDOW_SIZE)
def draw(screen, state, rows=25, cols=25, MARGIN=1):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    (w, h) = screen.get_size()
    width, height = w/cols, h/rows
    screen.fill(BLACK)
    for (x, y) in state:
        pygame.draw.rect(screen, WHITE, [
            (MARGIN + width) * x + MARGIN,
            (MARGIN + height) * y + MARGIN,
            width, height])
    pygame.display.flip()
