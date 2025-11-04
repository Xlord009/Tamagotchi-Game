import time
import random
import sys
import pygame
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Tamagotchi")

fps = 60
timer = pygame.time.Clock()

#Music
mixer.init()
mixer.music.set_volume(1)
mixer.music.load("Music/Sorry About That.mp3")
mixer.music.play()

playlist = [
     "Music/Sorry About That.mp3",
     "Music/Never see me again Kanye West.mp3"
]

current = 0
mixer.music.load(playlist[current])
mixer.music.play()

def next_song():
    global current
    current = (current + 1) % len(playlist)
    mixer.music.load(playlist[current])
    mixer.music.play()
    print("Playing:", playlist[current])




font = pygame.font.Font(None, 36)

button_rect = pygame.Rect(200, 200, 100, 50)
pause_but = pygame.Rect(100, 50, 100, 70)
button_enabled = True
button_enabled2 = True
button_enabled3 = True
new_press = True

class Button:
     def __init__(self, text, x_pos, y_pos, enabled):
          self.text = text
          self.x_pos = x_pos
          self.y_pos = y_pos
          self.enabled = enabled
          self.draw() 
     
     def draw(self):
          button_text = font.render(self.text, True, "black")
          button_rect = pygame.Rect((self.x_pos, self.y_pos), (150, 25))
          if self.enabled:
                if self.check_click():
                    pygame.draw.rect(screen, 'dark grey', button_rect, 0, 15)
                else:
                    pygame.draw.rect(screen, 'purple', button_rect, 0, 15)   
          else:
            pygame.draw.rect(screen, 'black', button_rect, 0, 15)
                  
            pygame.draw.rect(screen, 'black', button_rect, 2, 15)   
          screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

     def check_click(self):
          mouse_pos = pygame.mouse.get_pos()
          left_click = pygame.mouse.get_pressed()[0]
          button_rect = pygame.Rect((self.x_pos, self.y_pos), (150, 25))
          if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
               return True
          else:
               return False


running = True
while running:
    screen.fill("pink")
    timer.tick(fps)

    my_button = Button("Pause", 10, 10, button_enabled)
    my_button2 = Button("Play", 10, 40, button_enabled2)
    my_button3 = Button("Skip", 10, 70, button_enabled3)

    if pygame.mouse.get_pressed()[0] and new_press:
         new_press = False
         if my_button.check_click():
              mixer.music.pause()
              print("Music was paused")
         
         elif my_button2.check_click():
              mixer.music.unpause()
              print("Music is playing")

         elif my_button3.check_click():
              next_song()
              print("Skipping song")
              
        
    if not pygame.mouse.get_pressed()[0] and not new_press:
         new_press = True
    

              
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
                print("Music was paused")
            elif event.key == pygame.K_r:
                mixer.music.unpause()
                print("Music is playing")
            elif event.key == pygame.K_e:
                mixer.music.stop()
                running = False
            elif event.key == pygame.K_s:
                next_song()
                print("skipping song")



    pygame.display.flip()


pygame.quit()



class Tama:
        def __init__(self):
                self.hunger = 100
                self.emotions = 100
                self.health = 100
                self.alive = True