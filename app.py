game_state = True
game_over = False
game_end = False

def init():
    import rooms

    player = {
        "hp": 30,
        "attack": 5,
        "inventory": [rooms.items.potion1, rooms.items.potion2, rooms.items.potion3, rooms.items.potion4],
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

    def use(item):
        for i in player["inventory"]:
            if i["name"] == item:
                # print("You heal yourself for 5 health")
                print(player["inventory"])
                break 
            else:
                print("You don't have that item")

    def inventory():
        for item in player["inventory"]:
            print(item["name"])

    # use("potion")
    # inventory()
    print(player["inventory"][0])

init()   