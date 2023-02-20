import pygame
import time

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
white = (255, 255, 255)

# Movement variables
x1 = displayWidth / 2
y1 = displayHeight /2

snakeBlock = 10

x1Change = 0
y1Change = 0

clock = pygame.time.Clock()
snakeSpeed = 30


# Font config
font = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 30)


#Text config
def message(text, color):
    text = font.render(text, True, color)
    display.blit(text, [displayWidth/2, (displayHeight/2)-10])
    
# Game Over condition
gameOver = False

while not gameOver:
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
        gameOver = True
            
            
    x1 += x1Change
    y1 += y1Change
        
    
    #color background
    display.fill(black)
    
    #snake
    pygame.draw.rect(display, white, [x1, y1, snakeBlock, snakeBlock])
    
    pygame.display.update()
    
    clock.tick(snakeSpeed)

message("YOU DIED", red)
# Yes, this is a mutherfucking Dark Souls reference

pygame.display.update()


time.sleep(2)

# Encerrar programa
pygame.quit()
quit()
