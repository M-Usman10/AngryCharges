from background import *
from q_position import position_estimator
import time
pygame.init()
width, height = 1060, 700
screen=pygame.display.set_mode((width, height))

p = ([0, 0, 0], [100, 0, 0])
while 1:
    screen.fill(0)
    start_time = time.time() # start time of the loop
    display_background(screen,"resources/Backgrounds/Game_Bg-2.png")

    p = position_estimator([10, 0, 0], [0, 0, 1], 1, p[0], p[1], 1, 0.01)
    pygame.draw.circle(screen,[255,0,0],[int(p[0][0]+width/2),int(p[0][1]+height/2)],10)

    pygame.display.flip()
    print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)