import math, random, pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirx=1, diry=0, color=(255, 0, 0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos(self.pos[0] + self.dirx, self.pos[1] + self.diry)


    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            center = dis//2
            radius = 3
            circleMiddle = (i*dis+center-radius, j*dis+8)
            circleMiddle2 = (i*dis+dis-radius*2, j*dis+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake(object):
    body = []
    turns = []

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.keys.get_pressed()
            for key in keys:
                if key[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]
                elif key[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif key[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif key[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]
            for i, c in enumerate(self.body):
                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move = (turn[0], turn[1])
                    if i == len(self.body)-1:
                        self.turns.pop(p)
                else:
                    if c.dirx == -1 and c.pos[0] <= 0:
                        c.pos = (c.rows-1, c.pos[1])
                    elif c.dirx == 1 and c.pos[0] >= c.rows-1:
                        c.pos = (0, c.pos[1])
                    elif c.diry == 1 and c.pos[1] >= c.rows-1:
                        c.pos = (c.pos[0], 0)
                    elif c.diry == -1 and c.pos[1] <= 0:
                        c.pos = (c.pos[0], c.rows-1)
                    else:
                        c.move(c.dirx, c.diry)


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)



def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x += sizeBetween
        y += sizeBetween
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
    pass

def redrawWindow(surface):
    global rows, width, s
    surface.fill((0, 0, 0))
    s.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()
    

def message_box(subject, content):
    pass

def main():
    global rows, width, s
    width = 50
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        redrawWindow(win)
    


main()
