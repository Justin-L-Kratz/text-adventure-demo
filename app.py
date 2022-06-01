game_state = True

def init():
    import rooms

    potion1 = {
        "description": "A potion that restores your vitality, leaving you feeling refreshed"
    }

    potion2 = {
        "description": "A potion that restores your vitality, leaving you feeling refreshed"
    }

    potion3 = {
        "description": "A potion that restores your vitality, leaving you feeling refreshed"
    }

    potion4 = {
        "description": "A potion that restores your vitality, leaving you feeling refreshed"
    }

    chest1 = [potion1]
    chest2 = [potion2]
    chest3 = [potion3]
    chest4 = [potion4]

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
        "location": dungeon[0]
    }

    print(dungeon[2]["containsEnemy"]["name"])


init()   