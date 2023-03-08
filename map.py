import pygame

class Map(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("background/1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
