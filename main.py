import pygame as pg
import pygame.time
import os
import math
import random
import time

pg.init()

print(f"*** PyGame Initialised ***")


# Function to scale the image to a certain factor. Makes
# changing the size of the image easier on initialisation of
# image assets.
def scaleImg(img, factor):
    imgSize = round(img.get_width() * factor), round(img.get_height() * factor)
    return pg.transform.scale(img, imgSize)


# initialise image assets
REDCAR = scaleImg(pg.image.load("/Users/rossbrewer/PycharmProjects/MLCarGame/assets/redCar.png"), 0.1)
TRACK = scaleImg(pg.image.load("/Users/rossbrewer/PycharmProjects/MLCarGame/assets/track.png"), 1.5)
# TRACK_BORDER = scaleImage(pg.image.load("/Users/rossbrewer/PycharmProjects/MLCarGame/assets/track.png"), 1.5)

# Array of assets and their starting X and Y Coords.
assets = [(TRACK, (0, 0)), (REDCAR, (100, 115))]


# Function to draw (*blit*) each image onto the canvas
# using a list containing the image asset and its
# (X and Y)coords on the window.
def drawImages(window, asset):
    for img, position in asset:
        window.blit(img, position)


# Initialising PyGame Screen and Assets to display starting game screen.
def drawScreen():
    # initialise screen variables and colour
    background_colour = (0, 255, 0)
    SCREEN = pg.display.set_mode((700, 700))
    pg.display.set_caption("Game Screen")
    SCREEN.fill(background_colour)

    drawImages(SCREEN, assets)

    FPS = 60
    Time = pg.time.Clock()

    # ----------------------
    # TESTING VARIABLES for movement of object on window using keyboard inputs.
    X = 75
    Y = 75
    Height = 50
    Width = 30
    vel = 5
    # ----------------------

    # game screen loop
    pg.display.flip()
    running = True
    while running:
        Time.tick(FPS)

        pygame.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # TODO Implement car image that is controlled by key input.
        # This will give us a dictionary where each key has a value of 1 or 0. Where
        # 1 is pressed and 0 is not pressed.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_x]:
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

    # TODO Implement neural network
    # TODO Implement NEAT algorithm
    # TODO Implement data analytics and statistic evaluation


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
