from random import randint

class Character():
    def __init__(self):
        self.attack = 5
        self.health = 100
        self.max_health = 1000
        self.defence = 3
        self.alive = True
        self.name = '_error_!'
        self.level = 1
        self.exp = 0
        self.exp_to_next = 100

    def levelup(self):
        self.attack += 2
        self.defence += 1
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.exp = 0
        self.exp_to_next = self.level*100
        print(f'You leveled up! Current level is {self.level}')

    def hit(self, amount=0):
        if amount:
            return amount
        else:
            dmg = randint(self.attack-2, self.attack+2)
            return max(dmg, 1)

    def get_damage(self, amount):
        dmg = amount - self.defence
        self.health -= dmg
        print(f'{self.name} is hit for {dmg} damage! {self.health} HP left')
        if self.health <= 0:
            self.alive = False
            print(f'{self.name} is killed')


class Cave():
    def __init__(self, level):
        self.monsters = []
        self.level = level
        for i in range(randint(level*2, level*2+1)):
            type = randint(1,3)
            if type == 1:
                self.monsters.append(Cyclops())
            if type == 2:
                self.monsters.append(Goblin())
            else:
                self.monsters.append(Vedma())

class Cyclops(Character):
    def __init__(self):
        self.attack = 5
        self.health = 80
        self.max_health = 80
        self.defence = 3
        self.alive = True
        self.name = 'Cyclops'
        self.exp = 10

class Goblin (Character):
    def __init__(self):
        self.attack = 100
        self.health = 10
        self.max_health = 10
        self.defence = 1
        self.alive = True
        self.name = 'Goblin'
        self.exp = 500

class Vedma (Character):
    def __init__(self):
        self.attack = 10
        self.health = 150
        self.max_health = 200
        self.defence = 1
        self.alive = True
        self.name = 'Vedma'
        self.exp = 75

class Zombie (Character):
    def __init__(self):
        self.attack = 5
        self.health = 80
        self.max_health = 80
        self.defence = 3
        self.alive = True
        self.name = 'Zombie'
        self.exp = 50

class Hero (Character):
    def __init__(self):
        super().__init__()
        self.attack = 15
        self.health = 200
        self.max_health = 200
        self.defence = 0
        self.alive = True
        self.name = 'Lena'

def mainloop():
    hero = Hero()
    caves = [Cave(1), Cave(2), Cave(3)]

    offer = 'Choose you cave:\n'
    for number, n in enumerate(caves):
        offer += f'{number}'
    number = int(input(offer))
    monsters = caves[number].monsters



    while hero.alive > 0 and len(monsters)>0:
        offer = 'Choose you target:\n'
        for num, m in enumerate(monsters):
            offer += f'{num}. {m.name} ({m.health}/{m.max_health})\n'
        number = int(input(offer))
        monsters[number].get_damage(hero.hit())
        if monsters[number].alive == False:
            hero.exp += monsters[number].exp
            if hero.exp >= hero.exp_to_next:
                hero.levelup()

        monsters = [i for i in monsters if i.alive]
        for m in monsters:
            hero.get_damage(m.hit())
            if not hero.alive:
                print ('You are dead')
                break

    if hero.alive:
        print('You won')

mainloop()
