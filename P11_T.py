import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 400
width = 200
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

'''Create a kite shape using vertices
with .Poly() function and KINEMATIC body'''

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
    space.debug_draw(draw_options)
    
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)