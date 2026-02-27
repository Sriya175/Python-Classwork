
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player = pygame.Rect(100, 100, 50, 50)
speed = 5

enemies = []
for i in range(7):
    x = random.randint(0, WIDTH - 40)
    y = random.randint(0, HEIGHT - 40)
    enemies.append(pygame.Rect(x, y, 40, 40))

score = 0
font = pygame.font.SysFont(None, 36)

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


    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1


    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()