import pygame
pygame.init()
size = [1200, 900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption( "A Background")
done = False
clock = pygame.time.Clock()
background_position = [0, 0]
background_image = pygame.image.load("images/spacebridge.jpg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, background_position)

    pygame.display.flip()

    clock.tick(60)

    
