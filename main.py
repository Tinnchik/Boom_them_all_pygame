import os
import sys
from random import choice, randrange, randint
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Gameover(pygame.sprite.Sprite):
    image = load_image("gameover.png")
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Gameover.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x != 0:
            self.rect.x += 1

pygame.init()
all_sprites = pygame.sprite.Group()


pygame.display.set_caption("Gameover")
fullname = os.path.join('data', "gameover.png")
bomb_image = pygame.image.load(fullname)
screen = pygame.display.set_mode((600, 300), pygame.RESIZABLE)

Gameover(all_sprites)
running = True
while running:
    screen.fill("blue")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.time.Clock().tick(200)
    pygame.display.update()
pygame.quit()
sys.exit()
