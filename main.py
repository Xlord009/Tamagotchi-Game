import time
import random
import sys
import pygame
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Tamagotchi")

#Music
mixer.init()
mixer.music.load("Sorry About That.mp3")
mixer.music.set_volume(1)
mixer.music.play()





font = pygame.font.Font(None, 36)

button_rect = pygame.Rect(200, 200, 100, 50)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
                
                print("Music was paused")
            elif event.key == pygame.K_r:
                mixer.music.unpause()
                print("music is playing")
            elif event.key == pygame.K_e:
                mixer.music.stop()
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
             print("Mouse button was pressed")

pygame.quit()



class Tama:
        def __init__(self):
                self.hunger = 100
                self.emotions = 100
                self.health = 100
                self.alive = True
                self.days = 1


