class Item:
    def __init__(self, name, heal=0, attack=0):
        self.name = name
        self.heal = heal
        self.attack = attack

def use_item(player, item):
    player.hp = min(player.max_hp, player.hp + item.heal)
