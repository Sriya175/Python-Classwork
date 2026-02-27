
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangle Sprites")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


player = pygame.Rect(100, 150, 60, 60)
block = pygame.Rect(400, 150, 60, 60)

speed = 5

running = True
while running:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed


    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, block)
    pygame.display.update()

pygame.quit()
sys.exit()