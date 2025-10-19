import pygame

pygame.init()
screen = pygame.display.set_mode((600, 360)) # Create a window of size 800x600
pygame.display.set_caption("My Game") # Set the window title

pygame.display.set_icon(pygame.image.load('my-project/game1/images/player.goes straight1.png')) # Set and load the window icon
backgroud = pygame.image.load('my-project/game1/images/bg.png')
walk_right = [pygame.image.load('my-project/game1/images/player.goes right1.png'),
              pygame.image.load('my-project/game1/images/player.goes right2.png'),
              pygame.image.load('my-project/game1/images/player.goes right3.png'),
              pygame.image.load('my-project/game1/images/player.goes right4.png'),
              ]
walk_left = [pygame.image.load('my-project/game1/images/player.goes left1.png'),
             pygame.image.load('my-project/game1/images/player.goes left2.png'),
             pygame.image.load('my-project/game1/images/player.goes left3.png'),
             pygame.image.load('my-project/game1/images/player.goes left4.png'),
             ]
player_anim_count = 0
walk_right = [pygame.transform.scale(img, (50, 50)) for img in walk_right] # Scale images to 50x50
walk_left = [pygame.transform.scale(img, (50, 50)) for img in walk_left] # Scale images to 50x50

running = True

while running: # бесконечный цикл игры, что бы окно не закрывалось
    
    
    screen.blit(backgroud, (0, 0)) # Draw the background image onto the screen at position (0, 0)
    screen.blit(walk_right[player_anim_count], (50,260)) # Draw the image onto the screen at position (100, 100)
    
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1
    
    
    pygame.display.update() # Update the display
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # проверка на закрытие окна
            running = False
            pygame.quit() # Exit the program
            
       
                 
                    
            
            
    
#pygame.draw.ellipse(screen, ('purple'), (375, 275, 50, 100), 10) # Draw an ellipse
#myfont = pygame.font.Font("game1/fonts/Roboto-Regular.ttf", 36) # Create a font object
#text_surface = myfont.render("PIG", True, "green") # Render text