import pygame

pygame.display.set_caption("Snake")

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 0, 0))
pygame.display.update()
pygame.draw.rect(WINDOW, (255, 255, 255), (50, 50, 700, 500))
pygame.display.update()

DIRECTIONS = ['up', 'right', 'down', 'left']
direction = 0
snake = [
    [5, 5],
    [5, 6],
    [5, 7],
]
score = 0


def move():
    length = len(snake)


def draw():
    for body in snake:
        pygame.draw.rect(
            WINDOW,
            (0, 0, 255),
            (25 + 50 * body[0], 25 + 50 * body[1], 50, 50)
        )
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000 - score)
    running = True
    draw()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                move()
                draw()

    pygame.quit()


if __name__ == '__main__':
    main()