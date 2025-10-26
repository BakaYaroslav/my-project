import pygame
import random
 
pygame.init()
width = 640 # ширина
height = 480 # висота
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("Snake Game")

game_end = True
clock = pygame.time.Clock() #таймер фпс


colors = { 
    "snake_head": (0,255,0),   # зелений
    "snake_tall": (0,200,0),   # зелений более темный
    "apple": (255, 0, 0,)    # красный
}
snake_pos = {
    "x": 320,
    "y": 240,
    "x_change": 0,
    "y_change": 0,
}

snake_speed = 10

snake_size = (10, 10)

snake_tails = 10

snake_tails = []
# рандомный спавн для яблочек
apple_pos = {
    'x': round(random.randrange(0, width - snake_size[0]) / 10)* 10,
    'y': round(random.randrange(0, height - snake_size[1]) / 10)* 10,
    
}

apple_size = (10, 10) 
apple_eaten = 0
# начальные елементы для хвоста

snake_tails.append([snake_pos["x"]+10, snake_pos["y"]])
snake_tails.append([snake_pos["x"]+20, snake_pos["y"]])
snake_tails.append([snake_pos["x"]+30, snake_pos["y"]])


while game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = False        
        elif event.type == pygame.KEYDOWN:  # 
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
     # draw snake  
    display.fill((0,0,0)) #что бы змейка не оставляла безконечный след
    ilx = snake_pos["x"]
    ily = snake_pos["y"]
             
    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]
    
    for i in range(len(snake_tails) -1, 0, -1): # обновление хвоста с начала до конца
        snake_tails[i][0] = snake_tails[i-1][0]
        snake_tails[i][1] = snake_tails[i-1][1]
    if snake_tails:
        
        snake_tails[0][0] = ilx
        snake_tails[0][1] = ily
 
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
    
    # проверка змейка на той ли позиции что и яблоко
    if(snake_pos["x"] == apple_pos['x'] and
        snake_pos["y"] == apple_pos['y']):
        apple_eaten += 1
        snake_tails.append([apple_pos["x"], apple_pos["y"]]) 
        
        apple_pos = {
        'x': round(random.randrange(0, width - snake_size[0]) / 10) * 10,
        'y': round(random.randrange(0, height - snake_size[1]) / 10) * 10,
        
        }
    for i in range(len(snake_tails)): # обновление хвоста с начала до конца
        if(snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
           and snake_pos ['y'] + snake_pos["y_change"] == snake_tails[i][1]):
            snake_tails = snake_tails[:i]
            break
        
    

        
    # телепорт змеи если она покидает екран
    if(snake_pos["x"] < -snake_size[0]):
        snake_pos['x'] = width - 10
        
    elif(snake_pos["x"] > width - 10):
        snake_pos["x"] = 0
        
    elif(snake_pos["y"] < -snake_size[1]):
        snake_pos['y'] = height -10
        
    elif(snake_pos["y"] > height -10):
        snake_pos["y"] = 0
        
    pygame.display.update()
    clock.tick(30)  #ограничение фпс
pygame.quit()
quit()