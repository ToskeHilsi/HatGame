import pygame
import random
from settings import *

class Battle:
    def __init__(self, party, enemy):
        self.party = party
        self.enemy = enemy
        self.turn_index = 0
        self.state = "menu"

        self.heart = pygame.image.load("assets/heart.png")
        self.heart_rect = self.heart.get_rect(center=(WIDTH//2, HEIGHT//2))

        self.bullets = []
        self.timer = 0

    def next_turn(self):
        self.turn_index += 1
        if self.turn_index >= len(self.party.members):
            self.state = "enemy"
            self.turn_index = 0

    def player_action(self, action):
        char = self.party.members[self.turn_index]

        if action == "fight":
            dmg = char.attack + random.randint(0, 5)
            self.enemy.hp -= dmg
            self.party.tp += 5

        elif action == "act":
            self.enemy.mercy += 20

        elif action == "defend":
            self.party.tp += 16

        elif action == "magic":
            if char.role == "mage":  # Hat Guy
                if self.party.tp >= 20:
                    self.enemy.hp -= char.magic * 2
                    self.party.tp -= 20

            elif char.role == "tank":  # Sword Girl
                if self.party.tp >= 10:
                    char.defense += 5
                    self.party.tp -= 10

            elif char.role == "fire_mage":  # Fire Thing
                if self.party.tp >= 30:
                    self.enemy.hp -= char.magic * 3
                    for m in self.party.members:
                        m.attack += 2
                    self.party.tp -= 30

        elif action == "mercy":
            if self.enemy.mercy >= 100:
                return "spared"

        self.next_turn()

    def enemy_turn(self):
        self.timer += 1
        if self.timer % 20 == 0:
            self.spawn_pattern()

    def spawn_pattern(self):
        for i in range(10):
            rect = pygame.Rect(i * 80, 0, 10, 10)
            self.bullets.append(rect)

    def update_bullets(self):
        for b in self.bullets:
            b.y += 6

            # grazing (TP gain)
            if self.heart_rect.inflate(20, 20).colliderect(b):
                self.party.tp += 1

            if b.colliderect(self.heart_rect):
                self.party.members[0].hp -= 1

    def draw(self, screen):
        screen.fill(BLACK)

        for b in self.bullets:
            pygame.draw.rect(screen, RED, b)

        screen.blit(self.heart, self.heart_rect)

    def move_heart(self, keys):
        speed = 6
        if keys[pygame.K_LEFT]:
            self.heart_rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.heart_rect.x += speed
        if keys[pygame.K_UP]:
            self.heart_rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.heart_rect.y += speed
