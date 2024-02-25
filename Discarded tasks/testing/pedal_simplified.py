import pygame
import csv

f = open('pedal_simplified.csv', 'w',newline='')
writer = csv.writer(f,delimiter=',')
writer.writerow(['time_ms', 'axis0', 'axis1', 'axis2', 'axis3'])

pygame.joystick.init()
joysticks = pygame.joystick.get_count()
if joysticks:
    print(str(joysticks) + " joystick(s) detected!")

# Initialize each joystick
for i in range(joysticks):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()
    print("Joystick " + str(i) + " name: " + name)

FPS = 100  # frames per second setting

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

while running:
    passed_ms = clock.tick(FPS)
    count_ms += passed_ms
    if count_ms >= passed_ms:
        count_ms = count_ms % 500
        # writer.writerow([passed_ms, joystick.get_axis(0), joystick.get_axis(1)])
        axis0 = joystick.get_axis(0)
        axis1 = joystick.get_axis(1)
        print(type(axis1))
        writer.writerow([passed_ms, axis0, axis1])
    print(passed_ms)
    # pygame.display.update()
    # fpsClock.tick(FPS)

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
        if (event.type == KEYDOWN):
            if (event.unicode == K_ESCAPE):
                running = False

f.close()
pygame.quit()
sys.exit()