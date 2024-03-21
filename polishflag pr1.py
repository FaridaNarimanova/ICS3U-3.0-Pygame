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
pygame.display.set_caption("Polish Falg")    # I can change name of window

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
    pygame.draw.rect(screen, RED, pygame.Rect(240, 195, 300, 90))  # if i go lesser on left side, i move to left side
    pygame.draw.rect(screen, WHITE, pygame.Rect(240, 110, 300, 90))  # width is third one, increse gets wider



    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
