import pygame
import sys
import time

pygame.init()

water_image = pygame.image.load('images/water.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((tile_size*10, tile_size*10))
pygame.display.set_caption("This is my game")
screen.fill((0,0,0))

# load my island images
top_left = pygame.image.load('images/top_left.png')
top_mid = pygame.image.load('images/top_mid.png')
top_right = pygame.image.load('images/top_right.png')
bottom_left = pygame.image.load('images/bottom_left.png')
bottom_mid = pygame.image.load('images/bottom_mid.png')
bottom_right = pygame.image.load('images/bottom_right.png')



screen_rect = screen.get_rect()

rows = screen_rect.height // tile_size
cols = screen_rect.width // tile_size

for x in range(rows):
    for y in range(cols):
        screen.blit(water_image, (x * water_rect.height, y * water_rect.width))

screen.blit(top_left,(screen_rect.centerx - 2*tile_size, screen_rect.centery - tile_size))
screen.blit(top_mid,(screen_rect.centerx - tile_size, screen_rect.centery - tile_size))
screen.blit(top_right,(screen_rect.centerx, screen_rect.centery - tile_size))
screen.blit(bottom_left,(screen_rect.centerx - 2*tile_size, screen_rect.centery))
screen.blit(bottom_mid,(screen_rect.centerx - 1*tile_size, screen_rect.centery))
screen.blit(bottom_right,(screen_rect.centerx, screen_rect.centery))





pygame.display.flip()
time.sleep(5)
