"""
File: template.py
Author: Your Name
Date: 2024-03-20
Description: Template for basic Pygame graphics setup.
"""
# First, i enable the  Pygame library function
import pygame
import sys

# Second, I need to intialize the Pygame
pygame.init()

# Third, I set up the window in which i will have flag, size
width, height = 600, 500       # I can change size 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Youtube Logo")    # I can change name of window

# Define colours from https://www.pygame.org/docs/ref/color_list.html
WHITE = pygame.Color("white")    # I can change the value of contsant variable, but it will stay
RED = pygame.Color("brown1")
BLACK = pygame.Color("black")

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    # The thing thta i draw las, is on the top
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [100, 140, 450, 220], 15, border_radius=15)
    pygame.draw.rect(screen, RED, pygame.Rect(115, 155, 420, 200))  # if i go lesser on left side, i move to left side
    pygame.draw.polygon(screen, WHITE, [(250, 190), (370, 250), (250, 300)])    #1. Lefttop vertex 2.Right topvertex 3. Buttom


    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
