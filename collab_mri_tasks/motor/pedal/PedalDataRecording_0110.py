from __future__ import division
import sys, os, struct, time
from idlelib.autocomplete import FORCE

import pygame
import pygame.gfxdraw
from pygame.locals import *
import math, string

# Initialize pygame - only the modules we use (because the mixer module takes forever to quit and we're not using it).
pygame.display.init()
pygame.font.init()
pygame.joystick.init()

# Pygame Stuff
FPS = 100
# FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window

WINDOW_HEIGHT = 70
# WINDOW_WIDTH = 380  # 360 + 2 x 10
WINDOW_WIDTH = 860  # 360 + 2 x 10

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

running = True

clock = pygame.time.Clock()


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

Pressure = LabelledNumericalDisplay("P.S.I._L", "%d", 10, 10)
Voltage = LabelledNumericalDisplay("Voltage_L", "%d", 140, 10)
Vzero = LabelledNumericalDisplay("Vzero_L", "%d", 270, 10)

Pressure_2 = LabelledNumericalDisplay("P.S.I._R", "%d", 400, 10)
Voltage_2 = LabelledNumericalDisplay("Voltage_R", "%d", 530, 10)
Vzero_2 = LabelledNumericalDisplay("Vzero_R", "%d", 660, 10)

axis1_0 = None
axis0_0 = None

isDataRecording = False

f = open('pressi.csv', 'w')
f.write('time')
f.write(',')
f.write('Left')
f.write(',')
f.write('Right\n')

while running:

    axis0 = joystick.get_axis(0)
    axis1 = joystick.get_axis(1)

    print(axis0, axis1)

    if axis1_0 == None:
        axis1_0 = axis1

    v = (axis1 + 1.0) * 2.5
    psi = (axis1 - axis1_0) * 15.0
    v0 = (axis1_0 + 1.0) * 2.5


    Voltage.update(v)
    Pressure.update(psi)
    Vzero.update(v0)

    if axis0_0 == None:
        axis0_0 = axis0

    v_1 = (axis0 + 1.0) * 2.5
    psi_1 = (axis0 - axis0_0) * 15.0
    v0_1 = (axis0_0 + 1.0) * 2.5

    Voltage_2.update(v_1)
    Pressure_2.update(psi_1)
    Vzero_2.update(v0_1)

    if isDataRecording:
        current_time = time.time();

        f.write(str(current_time-start_time))
        f.write(',')
        f.write('%2.3f' % (psi))
        f.write(',')
        f.write('%2.3f\n' % (psi_1))


    pygame.display.update()
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
        if (event.type == KEYDOWN):
            if (event.unicode == u'q'): # stop recording press 'q'
                running = False
            if (event.unicode == u'z'):
                axis1_0 = None
            if (event.unicode == u'm'):
                CLEAR_SCREEN = True
                FORCE_MAX = FORCE
            if (event.unicode == u's'): # start recording press 's'
                start_time = time.time()
                isDataRecording = True

f.close()
pygame.quit()
sys.exit()
