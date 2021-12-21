import pygame

from src.Color import Color


class Block:
    def __init__(self, x, y, w, h, color, extreme_block, free):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.up_extreme_block, self.left_extreme_block, \
        self.down_extreme_block, self.right_extreme_block = extreme_block
        self.free = free
        self.step = 85

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))

    def get_coord(self):
        return (self.x, self.y, self.w, self.h)

    def is_unbreakable(self):
        if self.color == Color.gray:
            return True
        return False

    def step_left(self):
        self.x = self.x - self.step

    def step_right(self):
        self.x = self.x + self.step

    def step_up(self):
        self.y = self.y - self.step

    def step_down(self):
        self.y = self.y + self.step

    def left_coor(self):
        return (self.x - self.step, self.y, self.w, self.h)

    def right_coor(self):
        return (self.x + self.step, self.y, self.w, self.h)

    def up_coor(self):
        return (self.x, self.y - self.step, self.w, self.h)

    def down_coor(self):
        return (self.x, self.y + self.step, self.w, self.h)