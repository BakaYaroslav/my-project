import pygame

pygame.init()
width = 640 # ширина
height = 480 # висота
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("Menu Snake Game")
game_pause = False

font_menu = pygame.font.SysFont("Arial", 48)
font_color = (245, 245, 245)

player1_img = pygame.image.load("C:\edits\Python\images menu\player1.png").convert_alpha()
player2_img = pygame.image.load("C:\edits\Python\images menu\player2.png").convert_alpha()
exit_img = pygame.image.load("C:\edits\Python\images menu\exit.png").convert_alpha()


run_menu = True
while run_menu:
    
    
    text_surface = font_menu.render("Menu Snake Game", True, font_color)
    display.blit(player1_img, (width//4.5, 150))  # координати для кнопки
    display.blit(player2_img, (width//6, 250))  # координати для кнопки
    display.blit(exit_img, (width//3, 350))  # координати для кнопки
    display.blit(text_surface, (width//4, 25))  # координати для тексту
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = True     
        if event.type == pygame.QUIT:
            run_menu = False 
            
    pygame.display.update()
        
pygame.quit()       

    