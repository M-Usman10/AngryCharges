
import pygame
from pygame.locals import *
from background import displayBackground
from q_position import position_estimator
# 2 - Initialize the game
pygame.init()
width, height = 1920, 1080
screen=pygame.display.set_mode((width, height))

# 3 - Load images
box1 = pygame.image.load("resources/1.jpg")
box2 = pygame.image.load("resources/2.jpg")

p = ([0, 0, 0], [100, 0, 0])
# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # displayBackground(screen,box1,box2,width,height)
    # 7 - update the screen
    p = position_estimator([10, 0, 0], [0, 0, 1], 1, p[0], p[1], 1, 0.01)
    pygame.draw.circle(screen,[255,0,0],[int(p[0][0]+1920/2),int(p[0][1]+1080/2)],10)

    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)