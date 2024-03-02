import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set aircraft dimensions
AIRCRAFT_WIDTH = 50
AIRCRAFT_HEIGHT = 50

# Set obstacle dimensions
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50

# Set speed of aircraft
AIRCRAFT_SPEED = 5

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flight Simulator")

# Define the aircraft class
class Aircraft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((AIRCRAFT_WIDTH, AIRCRAFT_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 5
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
            self.rect.y = -self.rect.height

# Create aircraft object
aircraft = Aircraft()

# Create obstacle group
obstacles = pygame.sprite.Group()

# Main game loop
running = True
clock = pygame.time.Clock()

def restart_game():
    aircraft.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    obstacles.empty()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                aircraft.speed_x = -AIRCRAFT_SPEED
            elif event.key == pygame.K_RIGHT:
                aircraft.speed_x = AIRCRAFT_SPEED
            elif event.key == pygame.K_UP:
                aircraft.speed_y = -AIRCRAFT_SPEED
            elif event.key == pygame.K_DOWN:
                aircraft.speed_y = AIRCRAFT_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                aircraft.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                aircraft.speed_y = 0

    # Update aircraft position
    aircraft.update()

    # Draw aircraft
    screen.blit(aircraft.image, aircraft.rect)

    # Add obstacles randomly
    if random.randint(0, 100) < 2:
        obstacle = Obstacle()
        obstacles.add(obstacle)

    # Update and draw obstacles
    obstacles.update()
    obstacles.draw(screen)

    # Check for collision with obstacles
    if pygame.sprite.spritecollide(aircraft, obstacles, False):
        restart_game()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
