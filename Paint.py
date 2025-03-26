import pygame

# Инициализация pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Текущий цвет
current_color = BLACK

# Переменные
clock = pygame.time.Clock()
drawing = False
mode = "pencil"  # pencil, rect, circle, eraser
start_pos = None

# Очистка экрана
screen.fill(WHITE)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rect":
                pygame.draw.rect(screen, current_color, (*start_pos, event.pos[0] - start_pos[0], event.pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                radius = int(((event.pos[0] - start_pos[0]) ** 2 + (event.pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pencil":
                pygame.draw.line(screen, current_color, event.pos, pygame.mouse.get_pos(), 2)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pencil"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_SPACE:
                screen.fill(WHITE)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()