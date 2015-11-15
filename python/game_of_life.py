#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author Mikael Wikström
# https://github.com/leakim/GameOfLifeKata
#
import pygame
from time import sleep
from resources import GameOfLife, move, draw

def iter_next(state):
    """ given this generation as a set(), return a new set() for the next generation """
    newstate = set()
    # TODO: do something fancy
    return newstate

#######################################################################

def main():
    WINDOW_SIZE = [512, 512]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    state = move(GameOfLife.THREE_0, (10, 10))
    #state = move(GameOfLife.GLIDER_0, (10, 10))
    while True:
        print state
        draw(screen, state)
        sleep(0.2)
        state = iter_next(state)

if __name__ == "__main__":
    main()
