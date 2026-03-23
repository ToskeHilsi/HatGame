import pygame
from settings import *
from player import PlayerParty
from room import Room
from battle import Battle
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

party = PlayerParty()

# 🗺️ ROOM GRAPH (this defines the world layout)
rooms = {
    "center": Room("center", {
        "left": "left",
        "right": "right",
        "up": "up",
        "down": "down"
    }),
    "left": Room("left", {
        "right": "center"
    }),
    "right": Room("right", {
        "left": "center"
    }),
    "up": Room("up", {
        "down": "center"
    }),
    "down": Room("down", {
        "up": "center"
    }),
}

current_room = "center"

state = "overworld"
battle = None

running = True
while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🎮 BATTLE INPUT
        if state == "battle" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                battle.player_action("fight")
            if event.key == pygame.K_2:
                battle.player_action("act")
            if event.key == pygame.K_3:
                battle.player_action("defend")
            if event.key == pygame.K_4:
                battle.player_action("magic")
            if event.key == pygame.K_5:
                result = battle.player_action("mercy")
                if result == "spared":
                    state = "overworld"

    # 🌍 OVERWORLD
    if state == "overworld":
        room = rooms[current_room]

        party.move(keys)

        # 🔴 ENEMY COLLISION → START BATTLE
        if room.check_enemy_collision(party):
            battle = Battle(party, Enemy())
            state = "battle"

        # 🟦 ROOM TRANSITION
        next_room = room.check_transition(party)
        if next_room:
            current_room = next_room

            # reset position + fix follower bug
            for m in party.members:
                m.rect.center = (WIDTH // 2, HEIGHT // 2)
                m.history.clear()

        # 🎨 DRAW
        room.draw(screen)
        party.draw(screen)

    # ⚔️ BATTLE
    elif state == "battle":
        battle.move_heart(keys)
        battle.enemy_turn()
        battle.update_bullets()
        battle.draw(screen)

        # enemy defeated
        if battle.enemy.hp <= 0:
            party.gold += 10
            party.xp += 5
            state = "overworld"

    pygame.display.flip()

pygame.quit()
