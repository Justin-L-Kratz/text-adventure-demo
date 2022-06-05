game_state = True

def init():
    import rooms

    player = {
        "hp": 30,
        "attack": 5,
        "inventory": [],
        "alive": True,
        "location": 0
    }

    def open():
        if player["location"]["containsChest"]:
            if not player["location"]["containsChest"]["open"]:
                print("You open the chest")
            else:
                print("The chest is already open")
        else:
            print("You can see no such item in this room")

    def move(direction):
        if rooms.dungeon[player["location"]][direction] != False:
            player["location"] += rooms.dungeon[player["location"]][direction]
            print(player["location"])
        else:
            print("You can not go that way")

    def attack(target):
        target["hp"] -= 5
        battle_text = "You attack {} for 5 damage"
        print(battle_text.format(target["name"]))

    attack(rooms.enemies.kobold0)

init()   