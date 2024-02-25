#!/usr/bin/env python

from __future__ import division
import sys #, os, struct, time
import pygame
import pygame.gfxdraw
from pygame.locals import *
import csv
# import math, string

# Initialize pygame - only the modules we use (because the mixer module takes forever to quit and we're not using it).
pygame.display.init()
pygame.font.init()
pygame.joystick.init()

# Pygame Stuff
FPS = 1  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window

WINDOW_HEIGHT = 70
WINDOW_WIDTH = 380  # 360 + 2 x 10

margin = 10

window = pygame.Rect(0, 0, WINDOW_WIDTH + margin + margin, WINDOW_HEIGHT + margin + margin)
DISPLAYSURF = pygame.display.set_mode((window.width, window.height))

caption = "PRESSI Test"
pygame.display.set_caption(caption)

joysticks = pygame.joystick.get_count()
if joysticks:
    print(str(joysticks) + " joystick(s) detected!")

# Initialize each joystick
for i in range(joysticks):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()
    print("Joystick " + str(i) + " name: " + name)

class LabelledNumericalDisplay():
    def __init__(self, label, format_string, left, top):
        self.label = label
        self.format_string = format_string
        self.R = Rect(window.left + left, window.top + top, 120, 70)
        pygame.draw.rect(DISPLAYSURF, pygame.Color('black'), self.R)

        fontObj = pygame.font.SysFont('arial', 14)
        textSurfaceObj = fontObj.render(str(self.label), True, pygame.Color('white'), pygame.Color('black'))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (self.R.left + 5, self.R.top + 5)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        self.fontObj = pygame.font.SysFont('arial', 24)
        tso = self.fontObj.render(str("9.999"), True, pygame.Color('white'), pygame.Color('black'))
        self.tso_last = tso
        self.tro = textSurfaceObj.get_rect()
        self.tro.centerx = (self.R.centerx)
        self.tro.bottom = (self.R.bottom - 15)
        DISPLAYSURF.blit(tso, self.tro)

    def update(self, value):
        s = ('%2.3f' % value)
        tso = self.fontObj.render(str(s), True, pygame.Color('white'), pygame.Color('black'))
        self.tso_last = tso
        DISPLAYSURF.blit(self.tso_last, self.tro)


DISPLAYSURF.fill(pygame.Color('lightgray'))

# Pressure = LabelledNumericalDisplay("P.S.I.", "%d", 10, 10)
# Voltage = LabelledNumericalDisplay("Voltage", "%d", 140, 10)
# Vzero = LabelledNumericalDisplay("Vzero", "%d", 270, 10)
# Left = LabelledNumericalDisplay("Left", "%d", 10, 10)
# Right = LabelledNumericalDisplay("Right", "%d", 140, 10)

f = open('pedal.csv', 'w',newline='')
writer = csv.writer(f,delimiter=',')
writer.writerow(['time_ms', 'counted_ms', 'axis0', 'axis1'])

clock = pygame.time.Clock()
count_ms = 0

axis1_0 = None

start = False
running = False

while not start:
    trigger = input()
    if trigger == 's':
        running = True
        start = True
        print('started running')

while running:
    passed_ms = clock.tick(FPS)
    count_ms += passed_ms
    if count_ms >= passed_ms:
        # count_ms = count_ms % 500
        # writer.writerow([passed_ms, joystick.get_axis(0), joystick.get_axis(1)])
        axis0 = joystick.get_axis(0)
        axis1 = joystick.get_axis(1)
        # print(type(axis1))
        writer.writerow([passed_ms, count_ms, axis0, axis1])
    # print(passed_ms)
    pygame.display.update()
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
        if (event.type == KEYDOWN):
            if (event.unicode == K_ESCAPE):
                running = False

f.close()
pygame.quit()
sys.exit()