import pygame
import time

pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('really cool game')
screen.fill((0,0,225))

while True:
    print("-----------check for new events-------------")
    recent_events = pygame.event.get()
    print("----------done checking for events----------")
    for event in recent_events:
        print(event)
    pygame.display.flip()
    time.sleep(2)