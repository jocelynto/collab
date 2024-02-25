import pygame
import csv

f = open('testing_simul_1.csv', 'w',newline='')
writer = csv.writer(f,delimiter=',')
writer.writerow(['time_ms', 'axis0', 'axis1', 'axis2', 'axis3'])

clock = pygame.time.Clock()
count_ms = 0
FPS = 100

axis1_0 = None

start = False
running = False

while not start:
    trigger = input()
    if trigger == 's':
        running = True
        start = True

while running:
    passed_ms = clock.tick(FPS)
    count_ms += passed_ms
    if count_ms >= passed_ms:
        count_ms = count_ms % 500
        axis0 = 0.128374
        axis1 = -0.1294813
        axis2 = axis0 * axis1
        axis3 = axis2 ** axis1 + axis0
        writer.writerow([passed_ms, axis0, axis1, axis2, axis3])