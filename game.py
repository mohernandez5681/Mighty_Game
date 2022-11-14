import pygame
import time
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("This is my game!")
screen.fill((0, 0, 255))

while True:
   #step 1 - check for user input (key press, mouse clicks)
   recent_events = pygame.event.get()
   print("-----------Checking for new events ------------")
   for event in recent_events:
       #print(event.type)
       if event.type == pygame.QUIT:
           print("Ha Ha I will never quit!")
           pygame.quit()
           sys.exit()
       elif event.type == pygame.KEYUP:
           screen.fill((255, 0, 0))
       elif event.type == pygame.MOUSEMOTION:
           screen.fill((0, 255, 0))
   print("----------Done Checking -----------------")
   pygame.display.flip()
   time.sleep(1)
