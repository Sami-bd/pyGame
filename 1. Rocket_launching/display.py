import pygame
import time
import star


# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((400, 600))  # Set the window size to 800x600 pixels
pygame.display.set_caption("Rocket to space")  # Set the window title


font = pygame.font.Font(None, 48)
def render_text(surface, text, position):
    text_image = font.render(text, True, (255,255,255))  # Create text surface
    surface.blit(text_image, position)  # Draw text on screen


# Define colors (optional)
bg_color = 240

# rect co-ordinate
rect_x = 180
rect_y = 480

# triangle y co-ordinate
point_1y = 430
point_2y = 480
point_3y = 480

# left_right y co-ordinate triange 
left_right_point_1y = 520
left_right_point_23y = 560

# cercle y co-ordinate
circle_y = 510


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user wants to close the window
            running = False


    # Fill the screen with a color (e.g., white)
    if bg_color < 0:
        bg_color = 0
    screen.fill((bg_color, bg_color, bg_color))
    render_text(screen, "Welcome to Space!", (45, 530))

    if left_right_point_23y <= 0:
        render_text(screen, "The End", (135, 400))

    pygame.draw.polygon(screen, (0, 102, 255), [(200, point_1y), (180, point_2y), (220, point_3y)])
    pygame.draw.polygon(screen, (0, 102, 255), [(180, left_right_point_1y), (160, left_right_point_23y), (180, left_right_point_23y)])
    pygame.draw.polygon(screen, (0, 102, 255), [(220, left_right_point_1y), (220, left_right_point_23y), (240, left_right_point_23y)])
    pygame.draw.rect(screen, (213, 45, 45), (rect_x, rect_y, 40, 80))
    pygame.draw.circle(screen, (255, 255, 128), (200,circle_y), 10)
    
    star.call_star(screen)

    # Update the display
    pygame.display.flip()
    
    # point y co ordinate decreament
    if left_right_point_23y >= 0:
        point_1y -= 5
        point_2y -= 5
        point_3y -= 5
        rect_y -= 5
        left_right_point_1y -= 5
        left_right_point_23y -= 5
        circle_y -= 5

    # color value change
    if bg_color >= 0:
        bg_color -= 3

    time.sleep(0.2)


# Quit Pygame
pygame.quit()
