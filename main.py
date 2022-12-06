# Remove Pygame Message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
# import modules
import random, sys


# Include With Variables as Globals
def include( filepath ):
    exec(open( filepath ).read(), globals())

include("window.py")
include("colors.py")
include("cell.py")
include("mouse.py")
include("timer.py")
include("grid.py")

def disp():
    print("Hey")

Grid = grid()
Mouse = mouse()

run = True
while( run ):

    Screen.fill( Darkgray )
    Clock.tick( 100 )


    for event in pygame.event.get():
        # Mouse Inputs
        if event.type == pygame.MOUSEMOTION:
            Mouse.set_pos( event.pos )
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(1, 6, 1):
                if event.button == i :
                    Mouse.button[i-1] = 1
                    
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(1, 6, 1):
                if event.button == i :
                    Mouse.button[i-1] = 0

        # Keyboard Inputs
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                Grid.running = not(Grid.running)
                
            if event.key == pygame.K_ESCAPE:
                run = False
                
            if event.key == pygame.K_SPACE:
                pass
            
            elif event.key == pygame.K_BACKSPACE:
                Grid.running = False
                Grid.clear()
                    
            
        # Quit Event
        if event.type == pygame.QUIT:
            run = False

    if not( Grid.running ): # Editing cells
        if   Mouse.button[0] :
            Mouse.set_cell( 1 ) 
        elif Mouse.button[2] :
            Mouse.set_cell( 0 )
    elif  ( Grid.running ):
        Grid.chrono.update()
     
    Grid.blit()
    Mouse.get_cell().blit(White)
    
    pygame.display.update()
    
# Quit the program
pygame.quit 
pygame.display.quit()
