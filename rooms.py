import enemies
import items 

# To-Do's
# Add room descriptions

room1 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": 1,
    "east": False,
    "south": False,
    "west": False 
}

room2 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": False,
    "south": -1,
    "west": 1
}

room3 = {
    "containsChest": False,
    "containsEnemy": enemies.kobold0,
    "description": "Lorem",
    "north": 1,
    "east": -1,
    "south": False,
    "west": False
}

room4 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": 1,
    "south": -1,
    "west": False
}

room5 = {
    "containsChest": items.chest1,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": 1,
    "south": False,
    "west": -1
}

room6 = {
    "containsChest": False,
    "containsEnemy": enemies.kobold1,
    "description": "Lorem",
    "north": 1,
    "east": False,
    "south": False,
    "west": -1
}

room7 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": 1,
    "east": False,
    "south": -1,
    "west": False
}

room8 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": False,
    "south": -1,
    "west": 1
}

room9 = {
    "containsChest": items.chest2,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": -1,
    "south": 1,
    "west": False
}

room10 = {
    "containsChest": False,
    "containsEnemy": enemies.kobold2,
    "description": "Lorem",
    "north": -1,
    "east": False,
    "south": False,
    "west": 1
}

room11 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": 1,
    "east": -1,
    "south": False,
    "west": False
}

room12 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": 1,
    "east": False,
    "south": -1,
    "west": False
}

room13 = {
    "containsChest": items.chest3,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": 1,
    "south": -1,
    "west": False
}

room14 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": 1,
    "south": False,
    "west": -1
}

room15 = {
    "containsChest": False,
    "containsEnemy": enemies.kobold3,
    "description": "Lorem",
    "north": 1,
    "east": False,
    "south": False,
    "west": -1
}

room16 = {
    "containsChest": False,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": False,
    "south": -1,
    "west": 1
}

room17 = {
    "containsChest": items.chest4,
    "containsEnemy": False,
    "description": "Lorem",
    "north": False,
    "east": -1,
    "south": False,
    "west": 1
}

room18 = {
    "containsChest": False,
    "containsEnemy": enemies.koboldB,
    "description": "Lorem",
    "north": False,
    "east": -1,
    "south": False,
    "west": False
}

dungeon = [
    room1,
    room2,
    room3,
    room4,
    room5,
    room6,
    room7,
    room8,
    room9,
    room10,
    room11,
    room12,
    room13,
    room14,
    room15,
    room16,
    room17,
    room18
]