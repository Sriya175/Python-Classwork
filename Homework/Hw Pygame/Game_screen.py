import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Set the window dimensions (width, height)
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 3. Set the window title
pygame.display.set_caption("My Pygame Window")

# Define a color (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 4. Main game loop
running = True
while running:
    # 5. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 6. Drawing (fill the background color)
    screen.fill(BLACK) # Fills the screen with black

    # 7. Update the display
    pygame.display.flip() # or pygame.display.update()

# 8. Quit Pygame
pygame.quit()
sys.exit()

