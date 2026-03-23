from inventory import Item

shop_items = [
    Item("Potion", heal=30),
    Item("Sword", attack=5)
]

def open_shop(player):
    print("Welcome to shop!")

    for i, item in enumerate(shop_items):
        print(f"{i}: {item.name}")

    choice = int(input("Buy item #: "))
    item = shop_items[choice]

    if player.gold >= 10:
        player.inventory.append(item)
        player.gold -= 10
        print("Bought", item.name)
