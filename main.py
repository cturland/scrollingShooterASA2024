import random

import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Screen resolution
screen_width = 1000
screen_height = 500

# Creating the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Scrolling Shooter")

# Spaceship settings
sprite_image = pygame.image.load("spaceship.png")
sprite_width = 50
sprite_height = 75
sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
sprite_rect = sprite_image.get_rect()
square_x = (screen_width - sprite_width) // 2
square_y = screen_height - sprite_height - 100
speed = 3
mov_up = False
mov_down = False
mov_left = False
mov_right = False
score = 0

# Asteroids
asteroids = []
amount_of_asteroids = 10

asteroid_image = pygame.image.load("asteroid.png")
asteroid_width = 50
asteroid_height = 50
asteroid_image = pygame.transform.scale(asteroid_image, (asteroid_width, asteroid_height))
for _ in range(amount_of_asteroids):
    x = random.randrange(0, screen_width - asteroid_width)
    y = random.randrange(-600, 0 - asteroid_height)
    velocity = random.randint(1, 5)
    asteroid = {"image" : asteroid_image,
                "rect" : asteroid_image.get_rect(topleft = (x, y)),
                "velocity" : velocity}
    asteroids.append(asteroid)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mov_up = True
            if event.key == pygame.K_s:
                mov_down = True
            if event.key == pygame.K_a:
                mov_left = True
            if event.key == pygame.K_d:
                mov_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                mov_up = False
            if event.key == pygame.K_s:
                mov_down = False
            if event.key == pygame.K_a:
                mov_left = False
            if event.key == pygame.K_d:
                mov_right = False

    if mov_up:
        square_y -= speed
        if square_y < 0:
            square_y = 0
    if mov_down:
        square_y += speed
        if square_y > screen_height - sprite_height:
            square_y = screen_height - sprite_height
    if mov_right:
        square_x += speed
        if square_x > screen_width - sprite_width:
            square_x = screen_width - sprite_width
    if mov_left:
        square_x -= speed
        if square_x < 0:
            square_x = 0

    screen.fill((255, 0, 0))

    for asteroid in asteroids:
        # Move asteroid
        asteroid["rect"].y += asteroid["velocity"]
        # Draw asteroid
        screen.blit(asteroid["image"], asteroid["rect"])

        if sprite_rect.colliderect(asteroid["rect"]):
            print("Game Over!")
            print(f"Your score was: {score}")
            running = False

        if asteroid["rect"].top > screen_height:
            score += 1
            asteroid["rect"].x = random.randrange(0, screen_width - asteroid_width)
            asteroid["rect"].y = random.randrange(-600, 0 - asteroid_height)
            asteroid["velocity"] = random.randint(1, 5)

    #pygame.draw.rect(screen, (0, 255, 0), (square_x, square_y, square_size, square_size))
    sprite_rect.topleft = (square_x, square_y)
    screen.blit(sprite_image, sprite_rect)

    ### Next week ###
    # Text for score on screen
    # Sounds/music
    # Shooting mechanism

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
