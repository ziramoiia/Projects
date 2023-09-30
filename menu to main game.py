# Setup Python ----------------------------------------------- #
import pygame
from sys import exit
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('RevsiMusic')
screen = pygame.display.set_mode((800,400))
 
titlefont = pygame.font.Font('font/Pixeltype.ttf', 48)
font = pygame.font.Font('font/Pixeltype.ttf', 40)

sky_surface = pygame.image.load('neabg.png').convert()
sky_surface2 = pygame.image.load('neabg2.png').convert()
sky_surface3 = pygame.image.load('neabg3.png').convert()

x = 400
y = 200
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    global click
    while True:
 
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
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
#----------------------------------------------------------------------------#
def all():
    running = True
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
    running = True
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
    running = True
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
    running = True
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

#-------------------------------------------------------------------------#
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = titlefont.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time




Clock = pygame.time.Clock()

game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('neabg.png').convert()
ground_surface = pygame.image.load('neaground.png').convert()

snail_surf = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,330))

player_surf = pygame.image.load('sprite.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,330))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('sprite.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = titlefont.render('RevsiMusic',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = titlefont.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

#---------------------------------------------------------------------------#

def main_game():
    global game_active
    global score
    global player_gravity
    global x
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                   if player_rect.collidepoint(event.pos):
                       player_gravity = -20
                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and player_rect.bottom >= 300:
                       player_gravity = -20
                    if event.key == pygame.K_LEFT and player_rect.bottom >= 300:
                        x -= 10
                       
                if event.type == obstacle_timer:
                    print('test')
      
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)




        if game_active:
            screen.blit(sky_surface,(0,0))
            screen.blit(ground_surface,(0,331))
            score = display_score()
        

        
            #Player
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= 330: player_rect.bottom = 330
            screen.blit(player_surf,player_rect)

            # collision
            if snail_rect.colliderect(player_rect):
                game_active = False
        else:
            screen.fill((94,129,162))
            screen.blit(player_stand,player_stand_rect)

            score_message = titlefont.render(f'Your Score: {score}',False,(111,196,169))
            score_message_rect = score_message.get_rect(center = (400,330))
            screen.blit(game_name,game_name_rect)

            if score == 0: screen.blit(game_message,game_message_rect)
            else: screen.blit(score_message,score_message_rect)
            

                
        pygame.display.update()
        Clock.tick(60)
    
main_menu()
