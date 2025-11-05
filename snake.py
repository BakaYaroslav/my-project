import pygame
import random
 
pygame.init()
width = 640 # ширина
height = 480 # висота
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("Snake Game")

game_end = False
game_end2 = False
clock = pygame.time.Clock() #таймер фпс


font_color = (245, 245, 245)
colors = { 
    "bg1":(170, 215, 81),  # светло-зеленый
    "bg2":(162, 209, 73),  # темно-з
    "snake_head": (0, 0, 255),   # синий
    "snake_tall": (0, 100, 255),   # более темный синий
    "snake_tall2": (240, 0, 0),   # красный
    "snake_head2": (200, 0, 0),   # более темный красный
    "apple": (255, 0, 0,)    # красный
}
snake_pos = {
    "x": 120,
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

snake_pos2 = {
    "x": 520,
    "y": 240,
    "x_change": -10,
    "y_change": 0,
}

snake_speed2 = 10

snake_size2 = (10, 10)


snake_tails2 = [
    [snake_pos2["x"] + 10, snake_pos2["y"]],
    [snake_pos2["x"] + 20, snake_pos2["y"]],
    [snake_pos2["x"] + 30, snake_pos2["y"]]
]
apple_size = (10, 10) 
apple_eaten = 0
apple_eaten1 = 0
apple_eaten2 = 0
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
bg_img = pygame.image.load(r"C:\edits\Python\images menu\bgmenu.png").convert_alpha()

player1_rect = player1_img.get_rect(center=(width//2, 150))
player2_rect = player2_img.get_rect(center=(width//2, 250))
exit_rect = exit_img.get_rect(center=(width//2, 350))

dark_bg = pygame.Surface((width, height))
dark_bg.fill((0, 0, 0))
dark_bg.set_alpha(100)



font = pygame.font.SysFont("Arial", 24,)

font_menu = pygame.font.SysFont("Arial", 48)

dark_bg = pygame.Surface((width, height), pygame.SRCALPHA)
dark_bg.fill((0, 0, 0, 180))  # Прозрачное затемнение

run_menu = True
while run_menu:
  
    bg_img = pygame.transform.scale(bg_img, (width, height))
    display.blit(bg_img, (0, 0))
    text_surface = font_menu.render("The Snake Game", True, font_color)
    display.blit(player1_img, player1_rect)  # координати для кнопки
    display.blit(player2_img, player2_rect)  # координати для кнопки
    display.blit(exit_img, exit_rect)  # координати для кнопки
    display.blit(text_surface, (width//4, 25))  # координати для тексту    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player1_rect.collidepoint(event.pos): # collidepoint проверяет нажатие на кнопку
                    run_menu = False
                    game_end = True
                elif player2_rect.collidepoint(event.pos): 
                    run_menu = False
                    game_end2 = True
                elif exit_rect.collidepoint(event.pos):
                    run_menu = False
                    pygame.quit()
                    quit() 
                     
    pygame.display.update()
    clock.tick(30)
                              
# запуск игры при нажатии на кнопку player1

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
                snake_pos["x_change"] = -snake_speed
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
    clock.tick(30)
    
    last_frame = display.copy()
    if game_end == False:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            bg_img = pygame.transform.scale(bg_img, (width, height))
            game_over_text = font_menu.render("Game Over", True, (0,0,200))
            score_text = font.render(f"Your Score: {apple_eaten}", True, (255,255,255))
            display.blit(last_frame, (0, 0)) 
            display.blit(dark_bg, (0, 0)) 
            display.blit(game_over_text, (width//2 - game_over_text.get_width()//2, height//2 - 50))
            display.blit(score_text, (width//2 - score_text.get_width()//2, height//2 + 10))
            pygame.display.update()
            clock.tick(30)

while game_end2:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end2 = False        
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT and snake_pos2["x_change"] == 0:
                snake_pos2["x_change"] = -snake_speed2
                snake_pos2["y_change"] = 0
            elif event.key == pygame.K_RIGHT and snake_pos2["x_change"] == 0:
                snake_pos2["x_change"] = snake_speed2 
                snake_pos2["y_change"] = 0
            elif event.key == pygame.K_UP and snake_pos2["y_change"] == 0:
                snake_pos2["x_change"] = 0 
                snake_pos2["y_change"] = -snake_speed2
            elif event.key == pygame.K_DOWN and snake_pos2["y_change"] == 0:
                snake_pos2["x_change"] = 0 
                snake_pos2["y_change"] = snake_speed2
                     
            elif event.key == pygame.K_a and snake_pos["x_change"] == 0:
                snake_pos["x_change"] = -snake_speed 
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
                
    # движение змейки 1
    
    ilx = snake_pos["x"]
    ily = snake_pos["y"]

    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]

    if len(snake_tails) > 0:
        for i in range(len(snake_tails)-1, 0, -1):
            snake_tails[i][0] = snake_tails[i-1][0]
            snake_tails[i][1] = snake_tails[i-1][1]
        snake_tails[0][0] = ilx
        snake_tails[0][1] = ily
    else:
        snake_tails.append([last_tail])

    last_tail1 = snake_tails[-1] if snake_tails else [ilx, ily]

    # движение змейки 2    
        
    ilx2 = snake_pos2["x"]
    ily2 = snake_pos2["y"]

    snake_pos2["x"] += snake_pos2["x_change"]
    snake_pos2["y"] += snake_pos2["y_change"]

    if len(snake_tails2) > 0:
        for i in range(len(snake_tails2)-1, 0, -1):
            snake_tails2[i][0] = snake_tails2[i-1][0]
            snake_tails2[i][1] = snake_tails2[i-1][1]
        snake_tails2[0][0] = ilx2
        snake_tails2[0][1] = ily2

    if snake_tails2:
        last_tail2= snake_tails2[-1]
    else:
        last_tail2 = [snake_pos2["x"], snake_pos2["y"]]
        snake_tails2.append(last_tail2)
        
    last_tail2 = snake_tails2[-1] if snake_tails2 else [ilx2, ily2]

    # рисуем хвост змеи 1
    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tall"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])
        # рисуем хвост змеи 2
        for t in snake_tails2:
            pygame.draw.rect(display, colors["snake_tall2"], [
                t[0],
                t[1],
                snake_size2[0],
                snake_size2[1]])
            
        # рисуем голову змеи 1
        pygame.draw.rect(display, colors["snake_head"], [
            snake_pos["x"],
            snake_pos["y"],
            snake_size[0],
            snake_size[1]])
        # рисуем голову змеи 2
        pygame.draw.rect(display, colors["snake_head2"], [
            snake_pos2["x"],
            snake_pos2["y"],
            snake_size2[0],
            snake_size2[1]])
        # рисуем яблочки
        pygame.draw.rect(display, colors["apple"], [
            apple_pos["x"],
            apple_pos["y"],
            apple_size[0],
            apple_size[1]])
        text1 = (f"Apples: {apple_eaten1}   L: {len(snake_tails)}")
        text2 = (f"Apples: {apple_eaten2}   L: {len(snake_tails2)}")
        text_surface = font.render(text1, True, (0,0,155)) # синий цвет текста
        text_surface2 = font.render(text2, True, (155,0,0)) # красный цвет текста
        display.blit(text_surface2, (440, 10))
        display.blit(text_surface, (30, 10))

        # проверка змейка на той ли позиции что и яблоко
        ate_by_p1 = (snake_pos["x"] == apple_pos['x'] and snake_pos["y"] == apple_pos['y'])
        ate_by_p2 = (snake_pos2["x"] == apple_pos['x'] and snake_pos2["y"] == apple_pos['y'])

        if ate_by_p1 or ate_by_p2:
            if ate_by_p1:
                apple_eaten1 += 1
                snake_tails.append([last_tail1[0], last_tail1[1]])
            if ate_by_p2:
                apple_eaten2 += 1
                snake_tails2.append([last_tail2[0], last_tail2[1]])
            if apple_pos != snake_pos or snake_tails:
                apple_pos = {
                'x': round(random.randrange(0, width - snake_size[0]) / 10) * 10,
                'y': round(random.randrange(0, height - snake_size[1]) / 10) * 10,
                }



        # Player 1: 

        for t in snake_tails[1:]:
            if snake_pos["x"] == t[0] and snake_pos["y"] == t[1]:
                game_end2 = False

        for t in snake_tails2:
            if snake_pos["x"] == t[0] and snake_pos["y"] == t[1]:
                game_end2 = False


        # Player 2:

        for t in snake_tails2[1:]:
            if snake_pos2["x"] == t[0] and snake_pos2["y"] == t[1]:
                game_end2 = False

        for t in snake_tails:
            if snake_pos2["x"] == t[0] and snake_pos2["y"] == t[1]:
                game_end2 = False
     
        # телепорт змеи если она покидает екран
        if snake_pos["x"] < -snake_size[0]:
            snake_pos['x'] = width - 10
        if snake_pos2["x"] < -snake_size2[0]:
            snake_pos2['x'] = width - 10
                
        elif snake_pos["x"] > width - 10:
            snake_pos["x"] = 0
        if snake_pos2["x"] > width - 10:
            snake_pos2["x"] = 0
                
        elif snake_pos["y"] < -snake_size[1]:
            snake_pos['y'] = height - 10
        if snake_pos2["y"] < -snake_size2[1]:
            snake_pos2['y'] = height - 10
                
        elif snake_pos["y"] > height - 10:
            snake_pos["y"] = 0
        if snake_pos2["y"] > height - 10:
            snake_pos2["y"] = 0

    last_frame2 = display.copy()
    
    pygame.display.update()
    clock.tick(30)
    if game_end2 == False:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            bg_img = pygame.transform.scale(bg_img, (width, height))
            display.blit(last_frame, (0, 0)) 
            display.blit(dark_bg, (0, 0)) 


            
            game_over_text = font_menu.render("Game Over", True, (245,245,245))
            score_text1 = font.render(f"Blue Score: {apple_eaten1}", True, (0,0,200))
            score_text2 = font.render(f"Red Score: {apple_eaten2}", True, (200,0,0))
            
            display.blit(game_over_text, (width//2 - game_over_text.get_width()//2, height//2 - 100))
            display.blit(score_text1, (width//2 - 200 - score_text1.get_width()//2, height//2 + 10))
            display.blit(score_text2, (width//2 + 200 - score_text2.get_width()//2, height//2 + 10))
            pygame.display.update()


    
pygame.quit()