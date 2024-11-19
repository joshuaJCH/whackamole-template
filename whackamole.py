import pygame
import random

def main():
    try:
        pygame.init()
        GRID_WIDTH = 32
        GRID_HEIGHT = 32
        GRID_COLUMNS = 20
        GRID_ROWS = 16
        SCREEN_WIDTH = GRID_COLUMNS * GRID_WIDTH
        SCREEN_HEIGHT = GRID_ROWS * GRID_HEIGHT



        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (GRID_WIDTH, GRID_HEIGHT))
        clock = pygame.time.Clock()

        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_pixel_x, mole_pixel_y = mole_x * GRID_WIDTH, mole_y * GRID_HEIGHT
                    if mole_pixel_x <= mouse_x < mole_pixel_x + GRID_WIDTH and \
                       mole_pixel_y <= mouse_y < mole_pixel_y + GRID_HEIGHT:
                        mole_x = random.randrange(GRID_COLUMNS)
                        mole_y = random.randrange(GRID_ROWS)


            screen.fill("brown")
            for x in range(0, SCREEN_WIDTH, GRID_WIDTH):
                pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_HEIGHT):
                pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))
            screen.blit(mole_image, (mole_x * GRID_WIDTH, mole_y * GRID_HEIGHT))


            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
