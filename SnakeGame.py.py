import pygame, sys, random
from pygame.math import Vector2

pygame.init()
cell_size   = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock  = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# Estado
snake = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
direction = Vector2(1,0)

# Fruta inicial que no caiga encima de la serpiente
fruit_pos = Vector2(random.randint(0, cell_number-1), random.randint(0, cell_number-1))
while fruit_pos in snake:
    fruit_pos = Vector2(random.randint(0, cell_number-1), random.randint(0, cell_number-1))

running = True
while running:
    # --------- Eventos ---------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Evitar reversa inmediata
            if event.key == pygame.K_UP and direction.y != 1:
                direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN and direction.y != -1:
                direction = Vector2(0,1)
            elif event.key == pygame.K_RIGHT and direction.x != -1:
                direction = Vector2(1,0)
            elif event.key == pygame.K_LEFT and direction.x != 1:
                direction = Vector2(-1,0)

        elif event.type == SCREEN_UPDATE:
            # ---- mover ----
            new_head = snake[0] + direction
            snake.insert(0, new_head)

            # ---- comer / crecer ----
            if new_head == fruit_pos:
                # reposicionar fruta fuera del cuerpo
                fruit_pos = Vector2(random.randint(0, cell_number-1), random.randint(0, cell_number-1))
                while fruit_pos in snake:
                    fruit_pos = Vector2(random.randint(0, cell_number-1), random.randint(0, cell_number-1))
                # no hacemos pop() para crecer
            else:
                snake.pop()  # mantener longitud si no comió

            # ---- colisiones (pared) ----
            if not (0 <= new_head.x < cell_number) or not (0 <= new_head.y < cell_number):
                running = False

            # ---- colisión consigo misma ----
            if new_head in snake[1:]:
                running = False

    # --------- Dibujo ---------
    screen.fill((163,215,81))

    # fruta
    fx, fy = int(fruit_pos.x * cell_size), int(fruit_pos.y * cell_size)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(fx, fy, cell_size, cell_size))

    # serpiente
    for block in snake:
        x, y = int(block.x * cell_size), int(block.y * cell_size)
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(x, y, cell_size, cell_size))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
