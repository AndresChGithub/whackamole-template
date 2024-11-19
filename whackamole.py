import pygame
import random


def draw_grid(screen, grid_size, color):
    #Draws a grid on the screen.
    for x in range(0, screen.get_width(), grid_size):
        pygame.draw.line(screen, color, (x, 0), (x, screen.get_height()))
    for y in range(0, screen.get_height(), grid_size):
        pygame.draw.line(screen, color, (0, y), (screen.get_width(), y))

def get_random_grid_position(grid_size, screen_width, screen_height):
    #Gets a random grid-aligned position.
    x = random.randint(0, (screen_width // grid_size) - 1) * grid_size
    y = random.randint(0, (screen_height // grid_size) - 1) * grid_size
    return x, y

def main():
    try:
        pygame.init()
        SCREEN_WIDTH, SCREEN_HEIGHT = 640, 512
        GRID_SIZE = 32
        BACKGROUND_COLOR = (220, 20, 60)
        GRID_COLOR = (0, 0, 0)

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        mole_x, mole_y = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # checking if the click is on the mole
                    if mole_x <= mouse_x < mole_x + GRID_SIZE and mole_y <= mouse_y < mole_y + GRID_SIZE:
                        mole_x, mole_y = get_random_grid_position(GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)


            screen.fill(BACKGROUND_COLOR)
            draw_grid(screen, GRID_SIZE, GRID_COLOR)
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
