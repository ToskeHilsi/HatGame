import pygame

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (128, 128))

        self.hp = 50
        self.mercy = 0
