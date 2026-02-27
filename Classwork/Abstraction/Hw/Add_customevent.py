#add custom event
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Color Change")

WHITE = (255, 255, 255)

sprite1 = pygame.Rect(150, 150, 80, 80)
sprite2 = pygame.Rect(350, 150, 80, 80)

color1 = (255, 0, 0)
color2 = (0, 0, 255)


CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill(WHITE)
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)
    pygame.display.update()

pygame.quit()
sys.exit()