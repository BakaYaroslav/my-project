import pygame
 
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
snake_tails.append([snake_pos["x"]+10, snake_pos["y"]])
snake_tails.append([snake_pos["x"]+20, snake_pos["y"]])
snake_tails.append([snake_pos["x"]+30, snake_pos["y"]])


while game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = False        
        elif event.type == pygame.KEYDOWN:  # 
            if event.key == pygame.K_a:
                snake_pos["x_change"] = -snake_speed # смещение влево на 10 пикселей заданных ранее
                snake_pos["y_change"] = 0
            elif event.key == pygame.K_d:
                snake_pos["x_change"] = snake_speed 
                snake_pos["y_change"] = 0
            elif event.key == pygame.K_w:
                snake_pos["x_change"] = 0 
                snake_pos["y_change"] = -snake_speed
            elif event.key == pygame.K_s:
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
        

    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]
    ])
    # телепорт змеи если она покидает екран
    if(snake_pos["x"] < -snake_size[0]):
        snake_pos['x'] = width
        
    elif(snake_pos["x"] > width):
        snake_pos["x"] = 0
        
    elif(snake_pos["y"] < -snake_size[1]):
        snake_pos['y'] = height
        
    elif(snake_pos["y"] > height):
        snake_pos["y"] = 0
        
    pygame.display.update()
    clock.tick(30)  #ограничение фпс
pygame.quit()
quit()