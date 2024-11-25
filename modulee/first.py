import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Паучья игра")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Кадровая частота
clock = pygame.time.Clock()
FPS = 60

# Игрок паук
spider = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 40)
spider_speed = 5

# Насекомое с рандомным движением
bug = pygame.Rect(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), 20, 20)
bug_speed = [random.choice([-3, 3]), random.choice([-3, 3])]  # Скорость по x и y

# Счёт
score = 0

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление пауком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spider.left > 0:
        spider.x -= spider_speed
    if keys[pygame.K_RIGHT] and spider.right < WIDTH:
        spider.x += spider_speed
    if keys[pygame.K_UP] and spider.top > 0:
        spider.y -= spider_speed
    if keys[pygame.K_DOWN] and spider.bottom < HEIGHT:
        spider.y += spider_speed

    # Движение насекомого
    bug.x += bug_speed[0]
    bug.y += bug_speed[1]

    # Проверка границ для насекомого
    if bug.left <= 0 or bug.right >= WIDTH:
        bug_speed[0] = -bug_speed[0]
    if bug.top <= 0 or bug.bottom >= HEIGHT:
        bug_speed[1] = -bug_speed[1]

    # Соприкосновения с насекомым
    if spider.colliderect(bug):
        score += 1
        bug.x = random.randint(50, WIDTH - 50)
        bug.y = random.randint(50, HEIGHT - 50)
        bug_speed = [random.choice([-3, 3]), random.choice([-3, 3])]  # Новый случайный вектор скорости

    # Отрисовка
    screen.fill(WHITE)

    # Паутина
    for i in range(0, WIDTH, 50):
        pygame.draw.line(screen, GRAY, (i, 0), (i, HEIGHT))
    for j in range(0, HEIGHT, 50):
        pygame.draw.line(screen, GRAY, (0, j), (WIDTH, j))

    # Рисуем паука
    pygame.draw.rect(screen, BLUE, spider)

    # Рисуем насекомое
    pygame.draw.rect(screen, RED, bug)

    # Отображение очков
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Очки: {score}', True, BLUE)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение игры
pygame.quit()
sys.exit()
