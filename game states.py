# Setup Python ----------------------------------------------- #
import pygame
from pygame.locals import *
pygame.init()

click = False
running = True
mainClock = pygame.time.Clock()
pygame.display.set_caption('RevsiMusic')
screen = pygame.display.set_mode((800,400))

#Fonts and Backgrounds---------------------------------------- #
titlefont = pygame.font.Font('font/Pixeltype.ttf', 48)
font = pygame.font.Font('font/Pixeltype.ttf', 40)

sky_surface = pygame.image.load('neabg.png').convert()
sky_surface2 = pygame.image.load('neabg2.png').convert()

sky_surface3 = pygame.image.load('neabg3.png').convert()

#------------------------------------------------------------- #
def main_menu():
    global click
    while click:
 
        screen.blit(sky_surface,(0,0))
        draw_text('main menu', titlefont,'#c9cca1', screen, 330, 40)
 
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect(190, 100, 200, 50)
        button_2 = pygame.Rect(410, 100, 200, 50)
        button_3 = pygame.Rect(190, 200, 200, 50)
        button_4 = pygame.Rect(410, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                all()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                WCT()
        if button_4.collidepoint((mx, my)):
            if click:
                Twentieth()
        pygame.draw.rect(screen,'#caa05a', button_1)
        pygame.draw.rect(screen,'#caa05a', button_2)
        pygame.draw.rect(screen,'#8b4049', button_3)
        pygame.draw.rect(screen,'#8b4049', button_4)
        draw_text('ALL', titlefont,'#c9cca1', screen, 260, 110)
        draw_text('Theory', titlefont,'#c9cca1', screen, 450, 110)
        draw_text('Classical', titlefont,'#c9cca1', screen, 225, 210)
        draw_text('20th Century', titlefont,'#c9cca1', screen, 415, 210)
 
        for event in pygame.event.get():    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#----------------------------------------------------------------------------#
def all():
    global running
    while running:
        
        screen.blit(sky_surface,(0,0))
        draw_text('ALL', titlefont, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        main_game()
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    global running
    while running:
        
        screen.blit(sky_surface2,(0,0))
        draw_text('music theory', titlefont, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        main_game()
        
        pygame.display.update()
        mainClock.tick(60)

def WCT():
    global running
    while running:
        
        screen.blit(sky_surface3,(0,0))
        draw_text('western classical tradition', titlefont, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        main_game()
        
        pygame.display.update()
        mainClock.tick(60)

def Twentieth():
    global running
    while running:
        
        screen.blit(sky_surface3,(0,0))
        draw_text('Into the Twentieth Century', titlefont, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        main_game()
        
        pygame.display.update()
        mainClock.tick(60)
