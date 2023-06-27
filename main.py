import pygame


direction = 'up'
snake = [
    {'x': 5, 'y': 5},
    {'x': 5, 'y': 6},
    {'x': 5, 'y': 7},
]
score = 0

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def move():

    eat_fruit = False

    if not eat_fruit:
        snake.pop()

    next_head_x = snake[0]['x']
    next_head_y = snake[0]['y']

    if direction == 'up':
        next_head_y = next_head_y - 1
    elif direction == 'down':
        next_head_y = next_head_y + 1
    elif direction == 'right':
        next_head_x = next_head_x + 1
    elif direction == 'left':
        next_head_x = next_head_x - 1

    snake.reverse()
    snake.append({'x': next_head_x, 'y': next_head_y})
    snake.reverse()


def draw():
    WINDOW.fill((0, 0, 0))
    pygame.draw.rect(WINDOW, (255, 255, 255), (50, 50, 700, 500))
    for body in snake:
        pygame.draw.rect(
            WINDOW,
            (0, 0, 255),
            (50 + 50 * body['x'], 50 + 50 * body['y'], 50, 50)
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
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                move()
                draw()

    pygame.quit()


if __name__ == '__main__':
    main()