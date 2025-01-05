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


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width)
        self.rect.y = randrange(height)

    def update(self):
        self.image = load_image("boom.png")

pygame.init()
all_sprites = pygame.sprite.Group()

width = 450
height = 449
pygame.display.set_caption("Бомбочки 0.1")
fullname = os.path.join('data', "bomb.png")
bomb_image = pygame.image.load(fullname)
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

s = []
for _ in range(20):
    s.append(Bomb(all_sprites))

running = True
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for el in s:
                if el.rect.collidepoint(event.pos):
                    el.update()
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
sys.exit()