import pygame
import math

class ScrollingImage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('sprites/1.png').convert()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image_width = self.image.get_width()
        self.screen_width = pygame.display.get_surface().get_width()
        self.image_height = self.image.get_height()
        self.screen_height = pygame.display.get_surface().get_height()

    def update(self):
        # Calculate direction vector from mouse pointer to center of screen
        mouse_pos = pygame.mouse.get_pos()
        screen_center = (self.screen_width // 2, self.screen_height // 2)
        direction = (screen_center[0] - mouse_pos[0], screen_center[1] - mouse_pos[1])

        # Normalize direction vector to unit length
        length = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
        if length == 0:
            return
        direction = (direction[0] / length, direction[1] / length)

        # Move the image in the direction of the normalized vector
        self.rect.x += direction[0]
        if self.rect.right <= 0:
            self.rect.x += self.image_width
        elif self.rect.left >= self.screen_width:
            self.rect.x -= self.image_width

        self.rect.y += direction[1]
        if self.rect.top >= self.screen_height:
            self.rect.y -= self.image_height
        elif self.rect.bottom <= 0:
            self.rect.y += self.image_height
