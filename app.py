game_state = True

def init():
    import rooms

    dungeon = [
        rooms.room1,
        rooms.room2,
        rooms.room3,
        rooms.room4,
        rooms.room5,
        rooms.room6,
        rooms.room7,
        rooms.room8,
        rooms.room9,
        rooms.room10,
        rooms.room11,
        rooms.room12,
        rooms.room13,
        rooms.room14,
        rooms.room15,
        rooms.room16,
        rooms.room17,
        rooms.room18
    ]

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
        pass
    
    print(player["location"] + dungeon[player["location"]]["north"])    

init()   