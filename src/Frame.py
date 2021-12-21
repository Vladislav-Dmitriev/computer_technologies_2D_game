from src.Color import Color
import pygame


class Frame:
    def __init__(self, x, y, w, h, color, thick):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.thick = thick
        self.step = 85

    def draw_circle(self, win):
        pygame.draw.circle(win, Color.blue,
                           (self.x + int(self.w / 2), self.y + int(self.h / 2)), int(self.w / 4), 5)

    def get_coord(self):
        return (self.x, self.y, self.w, self.h)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h), self.thick)

    def left_coor(self):
        return (self.x - self.step, self.y, self.w, self.h)

    def right_coor(self):
        return (self.x + self.step, self.y, self.w, self.h)

    def up_coor(self):
        return (self.x, self.y - self.step, self.w, self.h)

    def down_coor(self):
        return (self.x, self.y + self.step, self.w, self.h)

    def step_left(self):
        self.x = self.x - self.step

    def step_right(self):
        self.x = self.x + self.step

    def step_up(self):
        self.y = self.y - self.step

    def step_down(self):
        self.y = self.y + self.step