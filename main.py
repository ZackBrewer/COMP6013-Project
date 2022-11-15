import pygame as pg
import os
import math
import random
import time

import pygame.time

pg.init()
print("*** PyGame Initialised ***")


# Initialising PyGame Screen and Assets to display starting game screen.
def drawScreen():
    # initialise screen variables and colour
    background_colour = (234, 212, 252)
    SCREEN = pg.display.set_mode((700, 700))
    pg.display.set_caption("Game Screen")
    SCREEN.fill(background_colour)
    # initialise car asset
    REDCAR = pg.image.load("/Users/rossbrewer/PycharmProjects/MLCarGame/assets/redCar.png").convert_alpha()
    REDCAR = pg.transform.smoothscale(REDCAR, (75, 150))

    X = 50
    Y = 50
    Height = 50
    Width = 30
    vel = 10

    # game screen loop
    pg.display.flip()
    running = True
    while running:
        pg.time.delay(100)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # This will give us a dictionary where each key has a value of 1 or 0. Where
        # 1 is pressed and 0 is not pressed.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
        if keys[pygame.K_LEFT]:
            X -= vel
        if keys[pygame.K_RIGHT]:
            X += vel
        if keys[pygame.K_UP]:
            Y -= vel
        if keys[pygame.K_DOWN]:
            Y += vel

        pygame.draw.rect(SCREEN, (255, 0, 0), (X, Y, Width, Height))
        pygame.display.update()
    return None


# def uploadMedia():
#     TRACK = "SRCIMAGE"
#     CAR_AI = "SRCIMAGE"
#     CAR_USER = "SRCIMAGE"
#
#     return TRACK, CAR_AI, CAR_USER

# Function to contain any details about project.
def main():
    print(f'-----------------------------------------')
    print(f'Welcome, this is a project built by')
    print(f'Zack Brewer. 19056696')
    print(f'-----------------------------------------')


# Program initialisation
if __name__ == '__main__':
    main()
    drawScreen()
