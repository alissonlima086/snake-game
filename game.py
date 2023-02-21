import pygame
import time
import random

pygame.init()



# Display

# Size variables
displayWidth = 800
displayHeight = 800

# Window
display = pygame.display.set_mode((displayWidth, displayHeight))

# Window information
pygame.display.set_caption("Snake Game - alissonlima086")

# Snake and screen colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

#snake size/speed
snakeBlock = 10
snakeSpeed = 20


clock = pygame.time.Clock()

# Font config
font = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 30)


#Text config
def message(text, color):
    text = font.render(text, True, color)
    display.blit(text, [displayWidth/2, (displayHeight/2)-10])


#Function
def gameLoop():
    gameOver = False
    gameClose = False
    
    # Movement variables
    x1 = displayWidth / 2
    y1 = displayHeight /2
    
    x1Change = 0
    y1Change = 0
    
    #food
    foodX = round(random.randrange(0, displayWidth - snakeBlock) / 10.0) * 10.0
    foodY = round(random.randrange(0, displayHeight - snakeBlock) / 10.0) * 10.0
      
    # Game Over condition

    while not gameOver:
        
        while gameClose == True:
            display.fill(black)
            message("Q - Quit or C - Play again", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.Key == pygame.K_c:
                        gameLoop()
        
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver=True
        
        # Snake Move keys
            if event.type == pygame.KEYDOWN:
                
                # Left Key
                if event.key == pygame.K_LEFT:
                    x1Change = -10
                    y1Change = 0
                
                # Right Key
                elif event.key == pygame.K_RIGHT:
                    x1Change = 10
                    y1Change = 0
                    
                # Up Key
                elif event.key == pygame.K_UP:
                    y1Change = -10
                    x1Change = 0
                    
                # Down Key
                elif event.key == pygame.K_DOWN:
                    y1Change = 10
                    x1Change = 0
                
                
        # Game over
        if x1 >= displayWidth or x1 < 0 or y1 >= displayHeight or y1 <0:
            gameClose = True
                
                
        x1 += x1Change
        y1 += y1Change
            
        
        #color background
        display.fill(black)
        
        #snake / food
        pygame.draw.rect(display, white, [x1, y1, snakeBlock, snakeBlock])
        pygame.draw.rect(display, blue, [foodX, foodY, snakeBlock, snakeBlock])
        
        pygame.display.update()
        
        if x1 == foodX and y1 == foodY:
            print("Comeu")
        
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()
    
gameLoop()
