# Final Project Kristopher Cooper, v0.3
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
player_idel_img = pygame.image.load("img/idle.png")
player_walk1_img = pygame.image.load("img/Walk_1.png")
player_walk2_img = pygame.image.load("img/Walk_2.png")
platform_img = pygame.image.load("img/Ground.jpg")
coin_img = pygame.image.load("img/Coin.png")
background_img = pygame.image.load("img/Background.png")
background_img = pygame.transform.sccale(background_img, (screen_width, screen_width))

# Set up the player
player_x = 400
player_y = 300
player_x_speed = 0
player_y_speed = 0
player_is_idle = True
player_walk_counter = 0

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

# Check for collison with platforms
for Platform in Platforms:
    if player_y + player_idel_img.get_height() > Platform[1] and player_y < Platform[1] + platform_img.get_height() and player_x + player_idel_img.get_width() > Platform[0] and player_x < Platform[0] + platform_img.get_width():
        player_y_speed = 0
        player_y = Platform[1] - player_idel_img.get_height()

# Check for collison with coins
for coin in coins:
    if player_y + player_idel_img.get_height() > coin[1] and player_y < coin[1] + coin_img.get_height() and player_x + player_idel_img.get_width() > coin[0] and player_x < coin[0] + coin_img.get_width():
        coins.remove(coin)

 # Draw the background
    screen.fill(WHITE)

# Draw the platforms
    for Platform in Platforms:
            screen.blit(platform_img, Platform)

# Draw the coins
    for coin in coins:
        screen.blit(coin_img, coin)

# Draw the player
    if player_is_idle:
        screen.blit(player_idel_img, (player_x, player_y))
    else:
        if player_walk_counter < 15:
            screen.blit(player_walk1_img, (player_x, player_y))
        elif player_walk_counter < 30:
            screen.blit(player_walk2_img, (player_x, player_y))
        else:
            player_walk_counter = 0
        player_walk_counter += 1

# Game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
           pygame.quit()
           exit()
        if event.type == pygame.KEYDOWN:
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
            elif event.key == pygame.K_UP:
                player_y_speed = 0
                player_is_idle = True