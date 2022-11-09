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
        if event.type == pygame.QUIT:
            print("Ha Ha I will never quit")
            pygame.quit()
            sys.exit()

        if event.type == pygame.K_r:
            screen.fill((255,0,0))
        elif event.type == pygame.K_g:
            screen.fill((0,255,0))

    pygame.display.flip()
    time.sleep(1)