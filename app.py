class Player():
    def __init__(self, name, race, job):
        self.name = name
        self.race = race
        self.job  = job

def greeter():
    name = input("What are you to be called? \n")
    race = input("What race would you like to be? \n")
    job = input("What is your occupation? \n")

    global player

    player = Player(name, race, job)

    intro = "I am {}, a {} {}, at your service!"
    
    print(intro.format(player.name, player.race, player.job))

greeter()

print(player.name)
print(player.race)
print(player.job)
