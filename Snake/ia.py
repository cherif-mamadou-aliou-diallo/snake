import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Taille de la fenêtre
WIDTH, HEIGHT = 600, 400

# Initialisation de la fenêtre
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - AI")

# Horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()

# Variables du serpent
snake_size = 20
snake_speed = 15
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Position initiale de la pomme
food_pos = [random.randrange(1, (WIDTH//snake_size)) * snake_size,
            random.randrange(1, (HEIGHT//snake_size)) * snake_size]

# Fonction pour afficher le score
def Your_score(score):
    font = pygame.font.SysFont(None, 35)
    score_surface = font.render(f"Score : {score}", True, WHITE)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WIDTH/2, 15)
    window.blit(score_surface, score_rect)

# Fonction pour l'IA
def move_towards_food():
    global direction

    if food_pos[0] > snake_pos[0]:
        direction = 'RIGHT'
    elif food_pos[0] < snake_pos[0]:
        direction = 'LEFT'
    elif food_pos[1] > snake_pos[1]:
        direction = 'DOWN'
    elif food_pos[1] < snake_pos[1]:
        direction = 'UP'

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Appel de la fonction de l'IA
    move_towards_food()

    # Déplacement du serpent
    if direction == 'UP':
        snake_pos[1] -= snake_size
    if direction == 'DOWN':
        snake_pos[1] += snake_size
    if direction == 'LEFT':
        snake_pos[0] -= snake_size
    if direction == 'RIGHT':
        snake_pos[0] += snake_size

    # Ajout de la tête du serpent
    snake_body.insert(0, list(snake_pos))

    # Vérification de la collision avec la pomme
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_pos = [random.randrange(1, (WIDTH//snake_size)) * snake_size,
                    random.randrange(1, (HEIGHT//snake_size)) * snake_size]
    else:
        # Suppression de la dernière partie du serpent
        snake_body.pop()

    # Affichage de la pomme
    window.fill(GREEN)
    for pos in snake_body:
        pygame.draw.rect(window, WHITE, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # Vérification de la collision avec les bords
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-snake_size or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-snake_size:
        pygame.quit()
        sys.exit()

    Your_score(len(snake_body)-1)

    pygame.display.flip()

    # Contrôle de la vitesse du jeu
    clock.tick(snake_speed)
