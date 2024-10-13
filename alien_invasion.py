import sys
import pygame

def run_game():
    # Initializing game and creating a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Alien Invasion")

    # setting the bg color
    bg_color = (0,255,255)


    # main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw screen
        screen.fill(bg_color)
        
        pygame.display.flip()

run_game()
