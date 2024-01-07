import pygame

pygame.init()

# Dimensions
WIDTH,HEIGHT = 1200,950
screen = pygame.display.set_mode([WIDTH,HEIGHT])

game_run = True
while game_run:
    #sets up the screen color
    screen.fill((0,0,0))

    #checking for if we are going to end the game so it doesn't run infinite
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
    pygame.display.flip()

pygame.quit()
