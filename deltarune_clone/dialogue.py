import pygame

class Dialogue:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.font = pygame.font.Font("assets/font.ttf", 30)

    def update(self):
        if self.index < len(self.text):
            self.index += 1

    def draw(self, screen):
        box = pygame.Rect(50, 400, 700, 150)
        pygame.draw.rect(screen, (0,0,0), box)
        pygame.draw.rect(screen, (255,255,255), box, 2)

        txt = self.font.render(self.text[:self.index], True, (255,255,255))
        screen.blit(txt, (60, 420))
