
import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen")


BG_COLOR = (0, 0, 0)


rect_width, rect_height = 200, 100
rect_color = (0, 128, 255)

rect = pygame.Rect(0, 0, rect_width, rect_height)
rect.center = (WIDTH // 2, HEIGHT // 2)


font = pygame.font.SysFont(None, 40)
text = font.render("Hello Pygame", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, 50))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, rect_color, rect)
    screen.blit(text, text_rect)
    pygame.display.update()

pygame.quit()
sys.exit()