import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

bg_surface = pygame.image.load('road.jpg').convert_alpha()
fitted_image = pygame.transform.scale(bg_surface, (600, 400))

bike1_surface = pygame.transform.scale(pygame.image.load("bike1.png"), (66, 59))
bike1_surface_x = 222
bike2_surface = pygame.transform.scale(pygame.image.load("bike2.png"), (100, 100))
bike2_surface_x = 333

bike3_surface = pygame.transform.flip(pygame.transform.scale(pygame.image.load("bike2.png"), (100, 100)), True, False)
bike3_surface_x = 443

bike4_surface = pygame.transform.scale(pygame.image.load("bike4.png"), (100, 100))
bike4_surface_x = 43

# plane
fly_surface = pygame.transform.scale(pygame.image.load("fly.png"), (100, 100))
fly_surface_x = 43



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(fitted_image, (0, 0))
    screen.blit(bike4_surface, (bike4_surface_x, 200))
    bike4_surface_x += 3
    
    screen.blit(bike3_surface, (bike3_surface_x, 200))
    bike3_surface_x += 2

    
    screen.blit(bike1_surface, (bike1_surface_x, 250))
    bike1_surface_x -= 2
    screen.blit(bike2_surface, (bike2_surface_x, 230))
    bike2_surface_x -= 3
    
    screen.blit(fly_surface, (fly_surface_x, 20))
    fly_surface_x += 3

    if bike1_surface_x < -66:
        bike1_surface_x = 600 

    if bike2_surface_x < -100:
        bike2_surface_x = 600

    if bike3_surface_x > 610:
        bike3_surface_x = -30 
    
    if bike4_surface_x > 610:
        bike4_surface_x = -70 

    if fly_surface_x > 620:
        fly_surface_x = -550 


    pygame.display.update()
    clock.tick(60)


