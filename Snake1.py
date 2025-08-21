import pygame,sys,random
from pygame.math import Vector2

# ------------------ CLASE SNAKE ------------------
class SNAKE:
        def __init__(self):
               # Cuerpo inicial de la serpiente (3 bloques)
              self.body = [Vector2(7,10),Vector2(6,10), Vector2(5,10)]
              self.direction = Vector2(0,0) # Dirección inicial (parada)
              self.new_block = False # Control para crecer

              # Cargar imágenes de cabeza en cada dirección
              self.head_up = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/head_up.png').convert_alpha()  
              self.head_down = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/head_down.png').convert_alpha()
              self.head_right = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/head_right.png').convert_alpha()
              self.head_left = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/head_left.png').convert_alpha()
              
              # Cargar imágenes de la cola
              self.tail_up = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/tail_up.png').convert_alpha()
              self.tail_down = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/tail_down.png').convert_alpha()
              self.tail_right = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/tail_right.png').convert_alpha()
              self.tail_left = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/tail_left.png').convert_alpha()
              
              # Cargar imágenes del cuerpo y las esquinas
              self.body_vertical = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/body_vertical.png').convert_alpha()
              self.body_horizontal = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/body_horizontal.png').convert_alpha()
              self.body_tr = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/body_tr.png').convert_alpha()
              self.body_tl = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/body_tl.png').convert_alpha()
              self.body_br = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/body_br.png').convert_alpha()
              self.body_bl = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/body_bl.png').convert_alpha()
              
              # Sonido al comer
              self.sound = pygame.mixer.Sound('C:/Users/david/Documents/SnakeGame/Sound/crunch.wav')

        def draw_snake(self):
                # Actualizar gráficos de cabeza y cola
                self.update_head_graphics()
                self.update_tail_graphics()

                # Dibujar cada bloque del cuerpo
                for index,block in enumerate(self.body): 
                        x_pos = int(block.x * cell_size)
                        y_pos = int(block.y * cell_size)
                        block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

                        if index == 0: # cabeza
                                screen.blit(self.head, block_rect)
                        elif index == len(self.body) - 1: # cola
                                screen.blit(self.tail, block_rect)
                        else: 
                                # Calcular orientación del cuerpo intermedio
                                previous_block = self.body[index + 1] - block
                                next_block = self.body[index - 1] - block
                                if previous_block.x  == next_block.x: 
                                        screen.blit(self.body_vertical, block_rect)
                                elif previous_block.y  == next_block.y: 
                                        screen.blit(self.body_horizontal, block_rect)
                                else:   
                                        # Dibujar esquinas
                                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                                                screen.blit(self.body_tl, block_rect)
                                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                                                screen.blit(self.body_bl, block_rect)
                                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                                                screen.blit(self.body_tr, block_rect)
                                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                                                screen.blit(self.body_br, block_rect)

        # Determinar qué cabeza usar según dirección                    
        def update_head_graphics(self): 

                head_relation = self.body[1] - self.body[0]
                if head_relation == Vector2(1,0): self.head = self.head_left
                elif head_relation == Vector2(-1,0): self.head = self.head_right
                elif head_relation == Vector2(0,1): self.head = self.head_up
                elif head_relation == Vector2(0,-1): self.head = self.head_down
        
        # Determinar qué cola usar según dirección
        def update_tail_graphics(self):
                
                tail_relation = self.body[-2] - self.body[-1]
                if tail_relation == Vector2(1,0): self.tail = self.tail_left
                elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
                elif tail_relation == Vector2(0,1): self.tail = self.tail_up
                elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
        
        # Movimiento de la serpiente
        def move_snake (self):
                if self.new_block == True: # crecer
                        body_copy = self.body [:]
                        body_copy.insert(0,body_copy[0] + self.direction)
                        self.body = body_copy[:]
                        self.new_block = False
                else: # moverse normalmente
                        body_copy = self.body [:-1]
                        body_copy.insert(0,body_copy[0] + self.direction)
                        self.body = body_copy[:]
        
        def add_block(self):
                self.new_block = True # activar crecimiento
        
        def play_sound(self):
                self.sound.play()
        
        def reset(self):
                # Reiniciar al estado inicial
                self.body = [Vector2(7,10),Vector2(6,10), Vector2(5,10)]
                self.direction = Vector2(0,0)

# ------------------ CLASE FRUIT ------------------
class FRUIT:
        def __init__(self):
                self.randomize()

        def draw_fruit(self):
                # Dibujar manzana
                fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
                screen.blit(apple,fruit_rect)

        def randomize(self):
                # Generar posición aleatoria
                self.x = random.randint(0,cell_number - 1 )
                self.y = random.randint(0,cell_number - 1 )
                self.pos = Vector2(self.x,self.y)

# ------------------ CLASE MAIN (Control del juego) ------------------
class MAIN:
        def __init__(self):
                self.snake = SNAKE()
                self.fruit = FRUIT()

        def update(self):
                # Actualizar estado en cada tick
                self.snake.move_snake()
                self.check_collision()
                self.check_failed() 
        
        def draw_elements(self):
                # Dibujar todos los elementos
                self.draw_grass()
                self.fruit.draw_fruit()
                self.snake.draw_snake()
                self.draw_score()

        # Verificar colisión entre serpiente y fruta 
        def check_collision(self):
                if self.fruit.pos == self.snake.body[0]:
                        self.fruit.randomize()
                        self.snake.add_block()
                        self.snake.play_sound()

        # Verificar colisiones contra paredes o contra sí misma
        def check_failed(self):
                head = self.snake.body[0]    
                if not 0 <= self.snake.body[0].x < cell_number or  not 0 <= self.snake.body[0].y < cell_number:
                        self.game_over()
                if head in self.snake.body[1:]:
                        self.game_over()
                               
        def game_over(self):
                self.snake.reset()
        
        # Dibujar fondo a cuadros
        def draw_grass(self):
                grass_color = (162, 209, 73)
                for row in range(cell_number):
                        if row % 2 == 0:
                                for col in range(cell_number):
                                        if col % 2 == 0:
                                                grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                                                pygame.draw.rect(screen,grass_color,grass_rect)
                        else: 
                                for col in range(cell_number):
                                        if col % 2 != 0:
                                                grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                                                pygame.draw.rect(screen,grass_color,grass_rect)

        # Dibujar puntaje en pantalla
        def draw_score(self):
                score_text = str(len(self.snake.body) - 3)
                score_surface = game_font.render(score_text,True,(56,74,12))
                score_x = int(cell_size * cell_number - 60)
                score_y = int(cell_size * cell_number - 40)
                score_rect = score_surface.get_rect(center = (score_x,score_y) )
                apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))

                screen.blit(score_surface,score_rect)
                screen.blit(apple,apple_rect)


# ------------------ CONFIGURACIÓN DEL JUEGO ------------------
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size)) ##widht,height
clock = pygame.time.Clock()
apple = pygame.image.load('C:/Users/david/Documents/SnakeGame/Graficos/apple.png').convert_alpha()
game_font = pygame.font.Font('C:/Users/david/Documents/SnakeGame/Font/PoetsenOne-Regular.ttf', 25)


# Evento personalizado que actualiza el movimiento de la serpiente cada 150ms
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

# ------------------ BUCLE PRINCIPAL ------------------
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit() # Cerrar programa
                if event.type == SCREEN_UPDATE:
                        main_game.update()

                # Controles del teclado        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                if main_game.snake.direction.y != 1:
                                        main_game.snake.direction = Vector2(0,-1)
                        if event.key == pygame.K_DOWN:
                                if main_game.snake.direction.y != -1:
                                        main_game.snake.direction = Vector2(0,1)
                        if event.key == pygame.K_RIGHT:
                                if main_game.snake.direction.x != -1:
                                        main_game.snake.direction = Vector2(1,0)
                        if event.key == pygame.K_LEFT:
                                if main_game.snake.direction.x != 1:
                                        main_game.snake.direction = Vector2(-1,0)                                 

        # Dibujar fondo y elementos
        screen.fill(((163,215,81)))
        main_game.draw_elements()
        pygame.display.update() # Refrescar pantalla   
        clock.tick(60) #framerate     
