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


class Tama:
        def __init__(self):
                self.hunger = 100
                self.emotions = 100
                self.alive = True

my_tama = Tama()

death_started = None

#Music
mixer.init()
mixer.music.set_volume(1)
mixer.music.load("Music/Sorry About That.mp3")
mixer.music.play()

playlist = [
     "Music/Sorry About That.mp3",
     "Music/Never see me again Kanye West.mp3",
     "music/This Is New.mp3"
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

def previous_song():
    global current
    current = (current - 1) % len(playlist)
    mixer.music.load(playlist[current])
    mixer.music.play()
    print("Playing:", playlist[current])





font = pygame.font.Font(None, 36)

button_rect = pygame.Rect(200, 200, 100, 50)
pause_but = pygame.Rect(100, 50, 100, 70)
button_enabled = True
button_enabled2 = True
button_enabled3 = True
button_exit_enabled = True
button_enabled5 = True
button_enabled_feed = True
button_enabled_pat = True
button_enabled_kill = True

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
    my_button4 = Button("Previous", 10, 100, button_enabled5)
    my_button5 = Button("EXIT", 10, 130, button_exit_enabled)
    my_button6 = Button("Feed", 270, 600, button_enabled_feed)
    my_button7 = Button("Pat", 90, 600, button_enabled_feed)
    my_button8 = Button("Kill", 450, 600, button_enabled_feed)

    

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

         elif my_button4.check_click():
              previous_song()
              print("Playing previous song")

         elif my_button6.check_click():
              my_tama.hunger + 5
              print(f"You feeded your tamagotchi (o･ω･o) hunger: {my_tama.hunger}%") 
         
         elif my_button7.check_click():
              my_tama.emotions + 5
              print(f"You patted your Tamagotchi (⌒ω⌒) emotion: {my_tama.emotions}%") 
         
         elif my_button8.check_click():
              print(f"He died (｡•́︿•̀｡)")
              mixer.music.unload()
              mixer.music.load("music/Church Bell - Sound Effect.mp3")
              mixer.music.play()
              
              death_started = pygame.time.get_ticks()

         
         elif my_button5.check_click():
              pygame.quit()
              
        
    if not pygame.mouse.get_pressed()[0] and not new_press:
         new_press = True
    

    if death_started is not None:
         now = pygame.time.get_ticks()
         if now - death_started >= 4700:
              mixer.music.unload()
              mixer.music.load(playlist[current])
              mixer.music.play()
              print("Wait he's back")

              death_started = None

              
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



