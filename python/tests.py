#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author Mikael Wikström
# https://github.com/leakim/GameOfLifeKata
#

import unittest
from resources import GameOfLife, move
from game_of_life import *

class game_of_life_tests(unittest.TestCase):

    # TODO: add more tests here

    def test_next(self):
        self.assertEqual( iter_next(GameOfLife.BLOCK_0),
                                    GameOfLife.BLOCK_1)
        self.assertEqual( iter_next(GameOfLife.THREE_0),
                                    GameOfLife.THREE_1)
        self.assertEqual( iter_next(GameOfLife.GLIDER_0),
                                    GameOfLife.GLIDER_1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

