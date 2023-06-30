import pygame
import random

WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = WINDOW.get_size()

colors = {
    "bg_color": (0, 0, 0),
    "border_color": (255, 255, 255),
    "tile_color": (0, 100, 0),
    "snake_color": (26, 187, 249),
    "food_color": (255, 121, 249),
}


def draw(snake, food):
    # A board is 40 tiles tall, and 40 tiles wide.
    # Around the board is a border of one tile.
    tile_size = HEIGHT / 42
    spacing = (WIDTH - HEIGHT) / 2
    board_size = HEIGHT - 2 * tile_size

    WINDOW.fill(colors["bg_color"])

    pygame.draw.rect(WINDOW, colors["border_color"], (spacing, 0, HEIGHT, HEIGHT))
    pygame.draw.rect(WINDOW, colors["tile_color"], (spacing + tile_size, tile_size, board_size, board_size))

    snake_image = pygame.image.load("assets/snake_body.png")
    snake_image = pygame.transform.scale(snake_image, (tile_size, tile_size))

    snake_head_image = pygame.image.load("assets/snake_head.png")
    snake_head_image = pygame.transform.scale(snake_head_image, (tile_size, tile_size))
 
    head_drawn = False
    for body in snake:
        if not head_drawn:
            draw_image(snake_head_image, spacing + tile_size * (body['x'] + 1), tile_size * (body['y'] + 1), tile_size,
                       tile_size)

            head_drawn = True
            continue

        draw_image(snake_image, spacing + tile_size * (body['x'] + 1), tile_size * (body['y'] + 1), tile_size,
                   tile_size)

    pygame.draw.rect(
        WINDOW,
        colors["food_color"],
        (spacing + tile_size + tile_size * food['x'], tile_size + tile_size * food['y'], tile_size, tile_size)
    )

    pygame.display.update()


def draw_image(image, x, y, width, height):
    rect = image.get_rect()
    rect.update(x, y, width, height)
    WINDOW.blit(image, (x, y, width, height))

    pygame.draw.rect(
        WINDOW,
        colors["snake_color"],
        rect,
        1
    )


def check_for_collision(snake):
    # checks if snake head has collided with body
    if snake.count((snake[0])) > 1:
        return True

    # checks if snake head has hit the wall
    if snake[0]['x'] < 0 or snake[0]['y'] < 0 or snake[0]['x'] > 39 or snake[0]['y'] > 39:
        return True

    return False


def move(direction, snake, food):
    next_head_x = snake[0]['x']
    next_head_y = snake[0]['y']

    if not food == {'x': next_head_x, 'y': next_head_y}:
        snake.pop()
    else:
        food.update({'x': random.randint(0, 39), 'y': random.randint(0, 39)})

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


def main():
    snake = [
        {'x': 5, 'y': 5},
        {'x': 5, 'y': 6},
        {'x': 5, 'y': 7},
    ]
    food = {'x': 2, 'y': 3}
    score = 0

    pygame.display.set_caption("Snake")
    direction = 'up'
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 250 - score)
    running = True
    draw(snake, food)

    while running:
        clock.tick(60)  # FPS

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = 'up'

                if event.key == pygame.K_a:
                    direction = 'left'

                if event.key == pygame.K_s:
                    direction = 'down'

                if event.key == pygame.K_d:
                    direction = 'right'

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                move(direction, snake, food)
                has_collided = check_for_collision(snake)
                if has_collided:
                    running = False

                draw(snake, food)

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
