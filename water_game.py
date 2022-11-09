import pygame
import sys
import time

pygame.init()

water_image = pygame.image.load('images/water.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width

screen = pygame.display.set_mode((10 + tile_size, 10+tile_size))
pygame.display.set_caption("This is my game")
screen.fill((0,0,0))


#print(water_rect)
#screen.blit(water_image, (168, 168))

screen_rect = screen.get_rect()


pygame.display.flip()
time.sleep(10)
