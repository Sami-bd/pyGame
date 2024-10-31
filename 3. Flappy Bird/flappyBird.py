import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

bg_surface = pygame.image.load('background.jpg').convert_alpha()
fitted_image = pygame.transform.scale(bg_surface, (600, 400))


bird_surface = pygame.image.load('bird.png').convert_alpha()
bird_size = pygame.transform.scale(bird_surface, (60, 50))
bird_size_y = 200
gravity = 0

start = False


rect_one_x = 300
rect_two_x = rect_one_x + 200
rect_three_x = rect_two_x + 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gravity = -15
                start = True
                print("Up arrow key pressed!")
                

    screen.blit(fitted_image, (0, 0))
    screen.blit(bird_size, (100, bird_size_y))

    pygame.draw.rect(screen, (213, 45, 45), (rect_one_x, 300, 40, 100))
    pygame.draw.rect(screen, (213, 45, 45), (rect_two_x, 200, 40, 200))
    pygame.draw.rect(screen, (213, 45, 45), (rect_three_x, 250, 40, 150))


    if rect_one_x < -40:
        rect_one_x = 620
    if rect_two_x < -40:
        rect_two_x = 620
    if rect_three_x < -40:
        rect_three_x = 620


    if start == True:
        gravity += 1
        bird_size_y += gravity

        rect_one_x -= 1
        rect_two_x -= 1
        rect_three_x -= 1
    
    if bird_size_y >= 380:
        start = False


    pygame.display.update()
    clock.tick(60)


