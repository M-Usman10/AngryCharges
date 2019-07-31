import pygame


def display_background_squares(screen, box1, box2, width, height):
    count = 0
    for n in range(int(height / 50)):
        for i in range(int(width / 50)):
            count += 1
            count = count % 2
            if (count):
                screen.blit(box1, (i * 50, n * 50))
            else:
                screen.blit(box2, (i * 50, n * 50))
        count += 1


def display_background(screen, imagePath):
    img = pygame.image.load(imagePath)
    screen.blit(img, (0, 0))
