import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Platformer Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#Load images
player_idel_img = pygame.image.load("idel.png")
player_walk1_img = pygame.image.load("Walk_1.png")
playerwalk2_img = pygame.image.load("Walk_2.png")
platform_img = pygame.image.load()
coin_img = pygame.image.load()

# Set up the player
player_x = 400
player_y = 300
player_x_speed = 0
player_y_speed = 0
player_is_idle = True
Player_walk_counter = 0

# Set up the playforms
Platforms = []
for i in range(10):
    platform_x = random.randint(0, screen_width - platform_img.get_width())
    platform_y = random.randint(50, screen_height - coin_img.get_height())
    Platforms.append((platform_x, platform_y))

# Set up the coins
    coins = []
    for i in range(5):
        coin_x = random.randint(0, screen_width - coin_img.get_width())
        coin_y = random.randint(50, screen_height - coin_img.get_height())
        coins.append((coin_x, coin_y))

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_speed = -5
                player_is_idle = False
            elif event.key == pygame.K_RIGHT:
                player_x_speed = 5
                player_is_idle = False
        elif event.key == pygame.K_UP:
            player_y_speed = -5
            player_is_idle = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_left or event.key == pygame.K_RIGHT:
                player_x_speed = 0
                player_is_idle = True