import pygame
import math
from player import Player
from move import ScrollingImage
from map import Map

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Modular Python Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the background image
background = ScrollingImage(0, 0)
background_group = pygame.sprite.Group()
background_group.add(background)

# Set up the map image
map = Map(0, 0)
map_group = pygame.sprite.Group()
map_group.add(map)

# Set up the player sprite
player = Player(screen_width / 2, screen_height / 2)
player_group = pygame.sprite.Group()
player_group.add(player)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Update the player sprite
    player.update(mouse_pos)

    # Update the background image
    direction = math.cos(math.radians(player.direction)) * 5
    background.update()

    # Draw the sprites
    screen.fill((255, 255, 255))
    map_group.draw(screen)
    background_group.draw(screen)
    player_group.draw(screen)

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Update the player's position and rotation
    player.update(mouse_pos)

    # Draw the player on the screen
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
