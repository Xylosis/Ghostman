import pygame
from board import boards
import math

pygame.init()

# information for game
WIDTH,HEIGHT = 1200,950
screen = pygame.display.set_mode([WIDTH,HEIGHT])
level = boards
color = "teal"

def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH//30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            # draws little pellet
            if level[i][j] == 1:
                # circle function takes the screen, color of object, x and y position, and the radius of object for size
                pygame.draw.circle(screen,'white',(j*num2 + (0.5*num2), i*num1 + (0.5*num1)),3)
            # draws big pellet
            if level[i][j] == 2:
                # circle function takes the screen, color of object, x and y position, and the radius of object for size
                pygame.draw.circle(screen,'yellow',(j*num2 + (0.5*num2), i*num1 + (0.5*num1)),8)
            # draws vertical line
            if level[i][j] == 3:
                pygame.draw.line(screen,color,(j * num2 + (0.5 * num2), i*num1), (j*num2 + (0.5*num2), i*num1 + num1),3)
            # draws horizontal line
            if level[i][j] == 4:
                pygame.draw.line(screen,color,(j * num2, i*num1 + (0.5*num1)), (j*num2 + num2, i*num1 + (0.5*num1)),3)
            # draws right top corner wall
            if level[i][j] == 5:
                pygame.draw.arc(screen,color, [(j*num2 - (num2*0.5)), (i*num1+(0.5*num1)), num2, num1],0, math.pi/2, 3)
            # draws down right corner wall
            if level[i][j] == 6:
                pygame.draw.arc(screen,color, [(j*num2 + (num2*0.5)), (i*num1+(0.5*num1)), num2, num1],math.pi/2,math.pi, 3)
            # top left corner wall
            if level[i][j] == 7:
                pygame.draw.arc(screen,color, [(j*num2 + (num2*0.5)), (i*num1-(0.5*num1)), num2, num1],math.pi,3*math.pi/2,3)
            # down left corner wall
            if level[i][j] == 8:
                pygame.draw.arc(screen,color, [(j*num2 - (num2*0.5)), (i*num1-(0.5*num1)), num2, num1],3*math.pi/2,2*math.pi, 3)
            # gate for the ghosts
            if level[i][j] == 9:
                pygame.draw.line(screen,"white",(j * num2, i*num1 + (0.5*num1)), (j*num2 + num2, i*num1 + (0.5*num1)),3)

            
            
            




game_run = True
while game_run:
    #sets up the screen color
    screen.fill((0,0,0))
    draw_board()

    #checking for if we are going to end the game so it doesn't run infinite
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    pygame.display.flip()

pygame.quit()
