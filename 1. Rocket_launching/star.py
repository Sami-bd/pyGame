
import pygame

def draw_star(surface, center, size):
    # Define the vertices of the star
    points = [
        (center[0], center[1] - size),
        (center[0] + size * 0.3, center[1] - size * 0.3),
        (center[0] + size, center[1]),
        (center[0] + size * 0.3, center[1] + size * 0.3),
        (center[0], center[1] + size),
        (center[0] - size * 0.3, center[1] + size * 0.3),
        (center[0] - size, center[1]),
        (center[0] - size * 0.3, center[1] - size * 0.3)
    ]

    # Draw the star
    pygame.draw.polygon(surface, (255,255,255), points)


def call_star(screen):
    draw_star(screen, (150, 230), 10)
    draw_star(screen, (100, 210), 5)
    draw_star(screen, (20, 20), 8)
    draw_star(screen, (270, 100), 4)
    draw_star(screen, (230, 270), 6)
    draw_star(screen, (290, 120), 7)
    draw_star(screen, (120, 180), 4)
    draw_star(screen, (240, 50), 10)
    draw_star(screen, (180, 20), 2)
    draw_star(screen, (70, 260), 4)
    draw_star(screen, (90, 130), 6)

    draw_star(screen, (230, 150), 2)
    draw_star(screen, (210, 100), 3)
    draw_star(screen, (20, 20), 3)
    draw_star(screen, (100, 270), 4)
    draw_star(screen, (270, 230), 5)
    draw_star(screen, (120, 290), 6)
    draw_star(screen, (180, 120), 7)
    draw_star(screen, (50, 240), 8)
    draw_star(screen, (20, 180), 9)
    draw_star(screen, (260, 70), 10)
    draw_star(screen, (130, 90), 9)
    draw_star(screen, (150, 60), 8)

    draw_star(screen, (330, 150), 2)
    draw_star(screen, (310, 100), 3)
    draw_star(screen, (30, 20), 3)
    draw_star(screen, (300, 270), 4)
    draw_star(screen, (370, 230), 5)
    draw_star(screen, (320, 290), 6)
    draw_star(screen, (380, 120), 4)
    draw_star(screen, (330, 240), 1)
    draw_star(screen, (330, 180), 3)
    draw_star(screen, (360, 70), 2)
    draw_star(screen, (330, 90), 3)
    draw_star(screen, (350, 60), 2)

    draw_star(screen, (30, 150), 2)
    draw_star(screen, (10, 100), 3)
    draw_star(screen, (30, 20), 3)
    draw_star(screen, (30, 270), 4)
    draw_star(screen, (70, 230), 5)
    draw_star(screen, (20, 290), 6)
    draw_star(screen, (80, 120), 4)
    draw_star(screen, (30, 240), 1)
    draw_star(screen, (30, 180), 3)
    draw_star(screen, (60, 70), 2)
    draw_star(screen, (30, 90), 3)
    draw_star(screen, (50, 60), 2)


