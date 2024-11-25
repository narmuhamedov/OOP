import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Кадровая частота
clock = pygame.time.Clock()
FPS = 10

# Размер одного квадратика
BLOCK_SIZE = 20

# Начальная позиция змейки
snake = [pygame.Rect(WIDTH // 2, HEIGHT // 2, BLOCK_SIZE, BLOCK_SIZE)]
snake_dir = (BLOCK_SIZE, 0)  # Движение вправо

# Позиция еды
food = pygame.Rect(
    random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
    BLOCK_SIZE,
    BLOCK_SIZE,
)

# Скорость и направление еды
food_dir = (BLOCK_SIZE, 0)

# Счёт
score = 0

# Функция завершения игры
def game_over():
    font = pygame.font.Font(None, 48)
    game_over_text = font.render(f"Игра окончена! Очки: {score}", True, RED)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, BLOCK_SIZE):
        snake_dir = (0, -BLOCK_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -BLOCK_SIZE):
        snake_dir = (0, BLOCK_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (BLOCK_SIZE, 0):
        snake_dir = (-BLOCK_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-BLOCK_SIZE, 0):
        snake_dir = (BLOCK_SIZE, 0)

    # Движение змейки
    new_head = snake[0].move(snake_dir)
    snake = [new_head] + snake[:-1]

    # Проверка на столкновение с едой
    if snake[0].colliderect(food):
        score += 1
        snake.append(snake[-1].copy())  # Увеличиваем длину змейки
        # Перемещение еды
        food.x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food.y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    # Движение еды
    food.move_ip(food_dir)

    # Если еда достигает границы, меняем её направление
    if food.left < 0 or food.right > WIDTH:
        food_dir = (-food_dir[0], food_dir[1])
    if food.top < 0 or food.bottom > HEIGHT:
        food_dir = (food_dir[0], -food_dir[1])

    # Проверка на столкновение с собой или стеной
    if (
        snake[0].x < 0
        or snake[0].x >= WIDTH
        or snake[0].y < 0
        or snake[0].y >= HEIGHT
        or any(part.colliderect(snake[0]) for part in snake[1:])
    ):
        game_over()

    # Отрисовка
    screen.fill(WHITE)

    # Рисуем еду
    pygame.draw.rect(screen, RED, food)

    # Рисуем змейку
    for part in snake:
        pygame.draw.rect(screen, GREEN, part)

    # Отображение очков
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Очки: {score}', True, RED)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение игры
pygame.quit()
sys.exit()
