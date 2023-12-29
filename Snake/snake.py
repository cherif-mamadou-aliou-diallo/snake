import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Taille de la fenêtre
WIDTH, HEIGHT = 600, 400

# Taille d'une cellule du serpent
CELL_SIZE = 20

# Initialisation de la fenêtre
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()

# Fonction principale du jeu
def game():
    # Position initiale du serpent
    snake = [(100, 100)]
    snake_direction = (1, 0)  # Direction initiale vers la droite

    # Position initiale de la pomme
    apple = spawn_apple()

    # Score initial
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Déplacement du serpent
        new_head = (snake[0][0] + snake_direction[0] * CELL_SIZE, snake[0][1] + snake_direction[1] * CELL_SIZE)
        snake.insert(0, new_head)

        # Vérification des collisions
        if check_collision(snake):
            game_over(score)

        # Vérification si le serpent a mangé la pomme
        if snake[0] == apple:
            score += 1
            apple = spawn_apple()
        else:
            snake.pop()

        # Dessiner le fond
        window.fill(BLACK)

        # Dessiner le serpent
        for segment in snake:
            pygame.draw.rect(window, WHITE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Dessiner la pomme
        pygame.draw.rect(window, RED, (apple[0], apple[1], CELL_SIZE, CELL_SIZE))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Contrôler la vitesse du jeu
        clock.tick(10)

# Fonction pour générer une nouvelle position de la pomme
def spawn_apple():
    x = random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE
    y = random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
    return x, y

# Fonction pour vérifier les collisions avec les bords de l'écran ou le serpent lui-même
def check_collision(snake):
    head = snake[0]
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]
    ):
        return True
    return False

# Fonction pour afficher l'écran de fin de jeu
def game_over(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game Over - Score: {score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Pause de 2 secondes avant de quitter
    pygame.quit()
    sys.exit()

# Lancer le jeu
game()
