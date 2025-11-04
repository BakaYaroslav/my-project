import pygame
import random
 
pygame.init()
width = 640 # ширина
height = 480 # висота
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("Snake Game")

game_end = False
clock = pygame.time.Clock() #таймер фпс

font_color = (245, 245, 245)
colors = { 
    "bg1":(170, 215, 81),  # светло-зеленый
    "bg2":(162, 209, 73),  # темно-з
    "snake_head": (0, 0, 255),   # синий
    "snake_tall": (0, 100, 255),   # более темный синий
    "apple": (255, 0, 0,)    # красный
}
snake_pos = {
    "x": 220,
    "y": 240,
    "x_change": 10,
    "y_change": 0,
}

snake_speed = 10

snake_size = (10, 10)


snake_tails = [
    [snake_pos["x"] - 10, snake_pos["y"]],
    [snake_pos["x"] - 20, snake_pos["y"]],
    [snake_pos["x"] - 30, snake_pos["y"]]
]
apple_size = (10, 10) 
apple_eaten = 0
# рандомный спавн для яблочек
apple_pos = {
    'x': round(random.randrange(0, width - snake_size[0]) / 10)* 10,
    'y': round(random.randrange(0, height - snake_size[1]) / 10)* 10,

}
        
font_menu = pygame.font.SysFont("Arial", 48)
font_color = (245, 245, 245)

player1_img = pygame.image.load(r"C:\edits\Python\images menu\player1.png").convert_alpha()
player2_img = pygame.image.load(r"C:\edits\Python\images menu\player2.png").convert_alpha()
exit_img = pygame.image.load(r"C:\edits\Python\images menu\exit.png").convert_alpha()

player1_rect = player1_img.get_rect(center=(width//2, 150))
player2_rect = player2_img.get_rect(center=(width//2, 250))
exit_rect = exit_img.get_rect(center=(width//2, 350))


font = pygame.font.SysFont("Arial", 24,)

font_menu = pygame.font.SysFont("Arial", 48)



run_menu = True
while run_menu:
     
    display.fill((0, 0, 0))  # Черный фон 
    text_surface = font_menu.render("Menu Snake Game", True, font_color)
    display.blit(player1_img, player1_rect)  # координати для кнопки
    display.blit(player2_img, player2_rect)  # координати для кнопки
    display.blit(exit_img, exit_rect)  # координати для кнопки
    display.blit(text_surface, (width//4, 25))  # координати для тексту    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = False  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player1_rect.collidepoint(event.pos): # collidepoint проверяет нажатие на кнопку
                    run_menu = False
                elif exit_rect.collidepoint(event.pos):
                    run_menu = False
                    game_end = False
                    pygame.quit()
                     
    pygame.display.update()
    clock.tick(30)
                    
                    
                
                    
# запуск игры при нажатии на кнопку player1
game_end = True

while game_end:

    if apple_pos['x'] == snake_pos['x'] and apple_pos['y'] == snake_pos['y']:
        apple_pos = {
            'x': round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            'y': round(random.randrange(0, height - snake_size[1]) / 10) * 10,
            
            }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = False        
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_a and snake_pos["x_change"] == 0:
                snake_pos["x_change"] = -snake_speed # смещение влево на 10 пикселей заданных ранее
                snake_pos["y_change"] = 0
            elif event.key == pygame.K_d and snake_pos["x_change"] == 0:
                snake_pos["x_change"] = snake_speed 
                snake_pos["y_change"] = 0
            elif event.key == pygame.K_w and snake_pos["y_change"] == 0:
                snake_pos["x_change"] = 0 
                snake_pos["y_change"] = -snake_speed
            elif event.key == pygame.K_s and snake_pos["y_change"] == 0:
                snake_pos["x_change"] = 0 
                snake_pos["y_change"] = snake_speed
    # draw background 

    for x in range(0, width, 10):  # рисуем сетку
        for y in range(0, height, 10):
            if (x + y) % 20 == 0:
                pygame.draw.rect(display, colors["bg1"], [x, y, 10, 10])
            else:
                pygame.draw.rect(display, colors["bg2"], [x, y, 10, 10])
    # движение змейки

    ilx = snake_pos["x"]
    ily = snake_pos["y"]
            
    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]
    if len(snake_tails) > 0:
        for i in range(len(snake_tails) -1, 0, -1): # обновление хвоста с начала до конца
            snake_tails[i][0] = snake_tails[i-1][0] # x-координата i-го сегмента хвоста
            snake_tails[i][1] = snake_tails[i-1][1] # y-координата i-го сегмента хвоста
        if snake_tails:
        
            snake_tails[0][0] = ilx
            snake_tails[0][1] = ily
    if snake_tails:
        last_tail = snake_tails[-1]
    else:
        last_tail = [snake_pos["x"], snake_pos["y"]]
        snake_tails.append(last_tail)
    # рисуем хвост змеи
    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tall"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])
        
    # рисуем голову змеи
    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]])
    # рисуем яблочки
    pygame.draw.rect(display, colors["apple"], [
        apple_pos["x"],
        apple_pos["y"],
        apple_size[0],
        apple_size[1]])
    text = (f"Apples: {apple_eaten}   L: {len(snake_tails)}")
    text_surface = font.render(text, True, (245,245,245)) # белый цвет текста
    display.blit(text_surface, (10, 10))

    # проверка змейка на той ли позиции что и яблоко
    if(snake_pos["x"] == apple_pos['x'] and
        snake_pos["y"] == apple_pos['y']):
        apple_eaten += 1
        snake_tails.append([last_tail[0], last_tail[1]])  # добавление нового сегмента хвоста
        if apple_pos != snake_pos or snake_tails:
            apple_pos = {
            'x': round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            'y': round(random.randrange(0, height - snake_size[1]) / 10) * 10,
            }
        if [apple_pos['x'], apple_pos['y']] not in snake_tails and (apple_pos['x'] != snake_pos['x'] or apple_pos['y'] != snake_pos['y']):
            pass
    '''for i in range(len(snake_tails)): # обновление хвоста с начала до конца
        if(snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
        and snake_pos ['y'] + snake_pos["y_change"] == snake_tails[i][1]):
            snake_tails = snake_tails[:i]
            break'''
    for t in snake_tails:
        if(snake_pos["x"] == t[0] and snake_pos["y"] == t[1]):
            game_end = False
            break
        
    ''' # телепорт змеи если она покидает екран
    if(snake_pos["x"] < -snake_size[0]):
        snake_pos['x'] = width - 10
        
    elif(snake_pos["x"] > width - 10):
        snake_pos["x"] = 0
        
    elif(snake_pos["y"] < -snake_size[1]):
        snake_pos['y'] = height -10
        
    elif(snake_pos["y"] > height -10):
        snake_pos["y"] = 0'''
    # конец игры если змейка выходит за границы экрана
    if(snake_pos["x"] < 0 or snake_pos["x"] > width -10 or
        snake_pos["y"] < 0 or snake_pos["y"] > height -10):
        game_end = False
        
    pygame.display.update()
    clock.tick(30)  #ограничение фпс
pygame.quit()