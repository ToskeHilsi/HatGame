import pygame

class Character:
    def __init__(self, name, sprite, role):
        self.name = name
        self.role = role

        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.rect = self.image.get_rect()

        self.history = []  # ✅ FIXED BUG (needed for followers)

        # 🎭 ROLE-BASED STATS
        if role == "mage":  # Hat Guy
            self.max_hp = 90
            self.attack = 8
            self.defense = 4
            self.magic = 12

        elif role == "tank":  # Sword Girl
            self.max_hp = 140
            self.attack = 10
            self.defense = 10
            self.magic = 2

        elif role == "fire_mage":  # Fire Thing
            self.max_hp = 80
            self.attack = 6
            self.defense = 3
            self.magic = 16

        self.hp = self.max_hp


class PlayerParty:
    def __init__(self):
        self.members = [
            Character("Hat Guy", "assets/hat_guy.png", "mage"),
            Character("Sword Girl", "assets/sword_girl.png", "tank"),
            Character("Fire Thing", "assets/fire_thing.png", "fire_mage")
        ]

        # leader start position
        start_x, start_y = 400, 300

        for i, m in enumerate(self.members):
            m.rect.center = (start_x - i * 100, start_y)

        self.tp = 0
        self.inventory = []
        self.gold = 0
        self.xp = 0

    def move(self, keys):
        leader = self.members[0]
        old_pos = leader.rect.topleft

        speed = 6
        if keys[pygame.K_LEFT]:
            leader.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            leader.rect.x += speed
        if keys[pygame.K_UP]:
            leader.rect.y -= speed
        if keys[pygame.K_DOWN]:
            leader.rect.y += speed

        # store movement history
        leader.history.insert(0, old_pos)

        # 👥 FOLLOWERS
        for i in range(1, len(self.members)):
            if len(self.members[i-1].history) > 12:
                self.members[i].rect.topleft = self.members[i-1].history[12]

    def draw(self, screen):
        for m in reversed(self.members):
            screen.blit(m.image, m.rect)
