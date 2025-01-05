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


class Car(pygame.sprite.Sprite):
    image = load_image("car.png")
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.direction = 0

    def update(self):
        if self.rect.x == 450 and self.direction == 0:
            self.direction = 1
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.x == 0 and self.direction == 1:
            self.direction = 0
            self.image = pygame.transform.flip(self.image, True, False)
        if not self.direction :
            self.rect = self.rect.move(1, 0)
            print(self.rect.x)
        else: self.rect = self.rect.move(-1, 0)

pygame.init()
all_sprites = pygame.sprite.Group()

width = 500
height = 500
Car(all_sprites)
pygame.display.set_caption("Бомбочки 0.1")
fullname = os.path.join('data', "car.png")
car_image = pygame.image.load(fullname)
screen = pygame.display.set_mode((600, 95), pygame.RESIZABLE)


running = True
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
