import pygame
import math

# Constants
WIDTH, HEIGHT = 400, 400
RAINBOW_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
WHITE = (255, 255, 255)

def draw_car(screen, x, y, size):
    # Draw car shape with rainbow colors
    pygame.draw.rect(screen, (0, 0, 0), (x - size//2, y - size//4, size, size//8))  # Body
    pygame.draw.rect(screen, (0, 0, 0), (x - size//4, y - size//4 - size//8, size//2, size//8))  # Roof
    pygame.draw.circle(screen, (0, 0, 0), (x - size//4, y + size//8), size//8)  # Left wheel
    pygame.draw.circle(screen, (0, 0, 0), (x + size//4, y + size//8), size//8)  # Right wheel

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shadow - The Dark Use")

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)
    text_surface = font.render("Shadow - The Dark User", True, (50, 0, 200))  # Rainbow orange color

    angle = 0
    size = 100
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        x = WIDTH // 2 + int(100 * math.sin(angle))
        y = HEIGHT // 2 + int(100 * math.cos(angle))

        draw_car(screen, x, y, size)
        screen.blit(text_surface, (x - text_surface.get_width()//2, y - text_surface.get_height()//2))

        angle += 0.02
        size = 100 + int(20 * math.sin(angle))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
