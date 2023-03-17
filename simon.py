import pygame
import random
import winsound
import math
pygame.init()#initializes Pygame
pygame.display.set_caption("Simon!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

#game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers in a TUPLE
turn = False
pattern = [] #this holds the random pattern
pi = 3.1415
def collision(xpos, ypos):
    if math.sqrt((xpos - 400)**2 + (ypos - 400)*2)>200 or math.sqrt((xpos - 300)**2 + (ypos - 200)*2)<200:
     #   print("outside of ring")
    #else:
     #   print("inside of ring")
        if xpos < 400 and ypos < 400:
            print("overblue botton")
            return 0
        elif xpos < 400 and ypos > 400:
            print("over yellow botton")
            return 1
            pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), 0, (pi/2), 100)
            pygame.flip()
            winsound.Beep(440, 500)
            return 0
        elif xpos < 400 and ypos > 400:
            #print(over green button")
            pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3 * pi / 2), 100)
            pygame.displayflip()
            windsound.Beep(640, 500)
            return 1
            playerpattern.append(collision(mousePos[0], mousePos[1]))
            print(playerpattern)
#draw everything first so things don't appear one at a time
pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), pi, (0), 100)###
pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), 0, (pi/2), 100)###
#more colors go here!  
pygame.display.flip()
playerpattern
#gameloop###################################################
while True:
   
    event = pygame.event.wait()#event queue

    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        turn = True

    if event.type == pygame.MOUSEBUTTONUP:
        turn = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        
    collision(mousePos[0],mousePos[1])
  #player turn========================================================================
    print("starting player turn")
    if playerTurn == True:
        if len(playerpattern) < len(pattern):
            if hasClicked == True
                playerpatteren.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False
                
                
                
                
                
                
    else:
        playerTurn = False
        pygame.time.wait(800) #slows the game down a bit 
    #update section---------------------------------------------
    if turn == True:
        pattern.append(random.randrange(0,4 )) #push a new value into the pattern list
       
        #brighten colors and play beep for each number in the pattern
        for i in range(len(pattern)):
            if pattern[i]==0: #RED
                pygame.draw.arc(screen, (255, 0,0), (200,200,400,400), pi/2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
               
            elif pattern[i]==1:#GREEN
                pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)
           
            elif pattern[i]==2:#blue###
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 3*pi/2, (0), 100)
                pygame.display.flip()
                winsound.Beep(840, 500)
               
               
            elif pattern[i]==3:##yellow
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), 0, (pi/2), 100)
                pygame.display.flip()
                winsound.Beep(1040, 500)
            
               
           
               
            #redraw board after every beep
            pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
            pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
            pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 3*pi/2, (0), 100)###
            pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), 0, pi/2 ,  100)###
            pygame.display.flip()
            pygame.time.wait(200) #slows the game down a bit
       
    turn = False      
    #render section---------------------------------------------
   
    #game board
    pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 3*pi/2, (0), 100)###
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 3*pi/2, (0), 100)
    #more colors go here!
   
   
    pygame.display.flip()
   

#end game loop##############################################

pygame.quit()