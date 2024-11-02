import pygame
import sys
import random

car_x_list = [55, 135, 220, 298]



pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Car game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

bg_surface = pygame.image.load('background.png').convert_alpha()
# bg_surface = pygame.image.load('backgronud.png').convert_alpha()
fitted_image = pygame.transform.scale(bg_surface, (400, 630))


# game over surface
game_over = pygame.image.load('cars/gameover.png').convert_alpha()
game_over = pygame.transform.scale(game_over, (400, 630))

# car 1 
car_1 = pygame.image.load('cars/car_1.png').convert_alpha()
car_1_surface = pygame.transform.scale(car_1, (50, 80))
car_1_x = 55
car_1_y = 500
car_1_surface_rect = car_1_surface.get_rect(topleft = (55, 500))

# car 2 
car_2 = pygame.image.load('cars/car_2.png').convert_alpha()
car_2_surface = pygame.transform.scale(car_2, (50, 80))
car_2_surface_rect = car_2_surface.get_rect(topleft = (55, 100))

# car 3 
car_3 = pygame.image.load('cars/car_3.png').convert_alpha()
car_3_surface = pygame.transform.scale(car_3, (50, 80))
car_3_surface_rect = car_3_surface.get_rect(topleft = (135, 150))

# car 4 
car_4 = pygame.image.load('cars/car_4.png').convert_alpha()
car_4_surface = pygame.transform.scale(car_4, (50, 80))
car_4_surface_rect = car_4_surface.get_rect(topleft = (220, 0))

# car 5 
car_5 = pygame.image.load('cars/car_5.png').convert_alpha()
car_5_surface = pygame.transform.scale(car_5, (50, 80))
car_5_surface_rect = car_5_surface.get_rect(topleft = (298, -100))



# points counter
points = 0


start = False
moving_left = False
moving_right = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # left button pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False

        # right button pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               moving_right = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               start = True
        
    


    screen.blit(fitted_image, (0, -15))
    # screen.blit(bird_size, bird_size.get_rect(topleft = (100, bird_size_y)))
    screen.blit(car_1_surface, car_1_surface_rect)
    screen.blit(car_2_surface, car_2_surface_rect)
    screen.blit(car_3_surface, car_3_surface_rect)
    screen.blit(car_4_surface, car_4_surface_rect)
    screen.blit(car_5_surface, car_5_surface_rect)

    # left right bottom car moving
    if moving_left == True:
        car_1_surface_rect.x -= 2
    elif moving_right == True:
        car_1_surface_rect.x += 2


    # car moving down
    if start == True:
        car_2_surface_rect.y += 2
        car_3_surface_rect.y += 1
        car_4_surface_rect.y += 3
        car_5_surface_rect.y += 1

    # resetting car position
    if car_2_surface_rect.y > 610:
        car_2_surface_rect.y = random.randint(-300, -250)
        points += 1
        car_2_surface_rect.x = random.choice(car_x_list)
    
    if car_3_surface_rect.y > 610:
        car_3_surface_rect.y = random.randint(-200, -150)
        points += 1
        car_3_surface_rect.x = random.choice(car_x_list)
    
    if car_4_surface_rect.y > 610:
        car_4_surface_rect.y = random.randint(-200, -150)
        points += 1
        car_4_surface_rect.x = random.choice(car_x_list)
    
    if car_5_surface_rect.y > 610:
        car_5_surface_rect.y = random.randint(-200, -150)
        points += 1
        car_5_surface_rect.x = random.choice(car_x_list)
    
    # checking colliions
    if car_1_surface_rect.colliderect(car_2_surface_rect):
        start = False
        moving_left, moving_right = False, False
        screen.blit(game_over, (0, 0))
        

    elif car_1_surface_rect.colliderect(car_3_surface_rect):
        start = False
        moving_left, moving_right = False, False
        screen.blit(game_over, (0, 0))
        

    elif car_1_surface_rect.colliderect(car_4_surface_rect):
        start = False
        moving_left, moving_right = False, False
        screen.blit(game_over, (0, 0))
        

    elif car_1_surface_rect.colliderect(car_5_surface_rect):
        start = False
        moving_left, moving_right = False, False
        screen.blit(game_over, (0, 0))
        

    pygame.display.update()
    clock.tick(60)




