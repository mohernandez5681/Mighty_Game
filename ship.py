import pygame

class Ship:
    def __init__(self):
        self.image = pygame.image.load('images/blue_ship.png')
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self):