import pygame

class Room:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors  # where each direction leads

        self.enemies = [
            {"rect": pygame.Rect(600, 400, 64, 64), "alive": True}
        ]

        self.tile = pygame.image.load("assets/tiles.png")

    def draw(self, screen):
        # TILE BACKGROUND
        tile_size = 64
        for x in range(0, screen.get_width(), tile_size):
            for y in range(0, screen.get_height(), tile_size):
                screen.blit(self.tile, (x, y))

        # ENEMY SPRITE
        enemy_img = pygame.image.load("assets/enemy.png")
        enemy_img = pygame.transform.scale(enemy_img, (64, 64))

        for e in self.enemies:
            if e["alive"]:
                screen.blit(enemy_img, e["rect"])

    def check_transition(self, party):
        leader = party.members[0].rect

        screen = pygame.display.get_surface()

        if leader.left < 0:
            return self.neighbors.get("left")
        if leader.right > screen.get_width():
            return self.neighbors.get("right")
        if leader.top < 0:
            return self.neighbors.get("up")
        if leader.bottom > screen.get_height():
            return self.neighbors.get("down")

        return None

    def check_enemy_collision(self, party):
        leader = party.members[0].rect

        for e in self.enemies:
            if e["alive"] and leader.colliderect(e["rect"]):
                e["alive"] = False
                return True
        return False
