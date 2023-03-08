import pygame
import math

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Ship/nyul 1.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = 0  # initial direction is right
        self.speed = 5  # speed of movement
        self.turn_speed = 2  # speed of turning
        self.max_offset = 20  # max distance from center while turning
        self.offset = 0  # current distance from center while turning

    def update(self, mouse_pos):
        # Calculate the angle between the player and the mouse position
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))

        # Update the player sprite's direction based on the angle
        if -45 <= angle <= 45:
            self.direction = 0  # right
        elif 45 < angle <= 135:
            self.direction = 90  # up
        elif -135 <= angle < -45:
            self.direction = 270  # down
        else:
            self.direction = 180  # left

        # Rotate the player sprite to face the mouse cursor
        self.image = pygame.transform.rotate(pygame.image.load('Ship/nyul 1.png').convert_alpha(), angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Move the player sprite
        if self.offset == 0:
            # if not turning, move directly towards the center of the screen
            dx, dy = self.rect.centerx - (screen.get_width() / 2), self.rect.centery - (screen.get_height() / 2)
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > self.speed:
                dx, dy = dx / dist * self.speed, dy / dist * self.speed
            self.rect.move_ip(-dx, -dy)
        else:
            # if turning, move in a curve away from the center of the screen
            angle_radians = math.radians(self.direction)
            dx, dy = math.cos(angle_radians), -math.sin(angle_radians)
            dx *= self.speed
            dy *= self.speed
            self.offset += self.turn_speed
            if self.offset > self.max_offset:
                self.offset = 0
            # Add an offset in the direction 90 degrees away from the turning direction
            dx += math.cos(angle_radians + math.radians(90)) * self.offset
            dy += -math.sin(angle_radians + math.radians(90)) * self.offset
            self.rect.move_ip(-dx, -dy)


player = Player(screen_width/2, screen_height/2)