import pygame

pygame.init()
screen = pygame.display.set_mode((600, 360)) # Create a window of size 800x600
pygame.display.set_caption("My Game") # Set the window title

pygame.display.set_icon(pygame.image.load('my-project/game1/images/pig.png')) # Set and load the window icon
pig = pygame.image.load('my-project/game1/images/pig.png') # Load an image
pig = pygame.transform.scale(pig, (50, 50)) # Scale the image to 100x100 pixels
backgroud = pygame.image.load('my-project/game1/images/bg.png')


running = True

while running: # бесконечный цикл игры, что бы окно не закрывалось
    
    
    screen.blit(backgroud, (0, 0)) # Draw the background image onto the screen at position (0, 0)
    screen.blit(pig, (50, 210)) # Draw the image onto the screen at position (100, 100)
    
    
    pygame.display.update() # Update the display
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # проверка на закрытие окна
            running = False
            pygame.quit() # Exit the program
       
                 
                    
            
            
    
#pygame.draw.ellipse(screen, ('purple'), (375, 275, 50, 100), 10) # Draw an ellipse
#myfont = pygame.font.Font("game1/fonts/Roboto-Regular.ttf", 36) # Create a font object
#text_surface = myfont.render("PIG", True, "green") # Render text