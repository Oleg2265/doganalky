import pygame
from pygame import image
from Player import *
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()


background = pygame.transform.scale(image.load("background.png"), (700, 500))

roma = Player(100 , 100, 50, 50, "sprite1.png", 4)
worog = Enemy(400, 100, 50, 50, "sprite2.png", 4)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if roma.hitbox.colliderect(worog.hitbox):
            print("ПРОГРАВ!!!!")
            pygame.quit()

    roma.move()
    worog.move()
    window.blit(background, (0, 0))
    roma.draw(window)
    worog.draw(window)
    pygame.display.flip()
    fps.tick(60)