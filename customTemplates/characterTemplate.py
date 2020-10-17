from .nameTemplate import enter_player_name


class CharacterClass:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana


class Warrior(CharacterClass):
    def __init__(self, name, health=130, mana=60):
        super().__init__(name, health, mana)

    def __str__(self):
        return "My name is {}. I am a WARRIOR with {} health and {} mana.".format(self.name, self.health, self.mana)


class Mage(CharacterClass):
    def __init__(self, name, health=85, mana=135):
        super().__init__(name, health, mana)

    def __str__(self):
        return "My name is {}. I am a MAGE with {} health and {} mana.".format(self.name, self.health, self.mana)


class Rogue(CharacterClass):
    def __init__(self, name, health=105, mana=75):
        super().__init__(name, health, mana)

    def __str__(self):
        return "My name is {}. I am a ROGUE with {} health and {} mana.".format(self.name, self.health, self.mana)


# Enemy should inherit CharacterClass
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


class Spider(Enemy):
    def __init__(self, name, hp=10, damage=2):
        super().__init__(name, hp, damage)

    def __str__(self):
        return "\nName: {}\n=====\nHP: {}\nDamage: {} \n".format(self.name, self.hp, self.damage)


class Goblin(Enemy):
    def __init__(self, name, hp=20, damage=5):
        super().__init__(name, hp, damage)

    def __str__(self):
        return "\nName: {}\n=====\nHP: {}\nDamage: {} \n".format(self.name, self.hp, self.damage)


# dredd_spider = Spider('Dredd Spider', 85, 30)
# print(dredd_spider)
#
#
# forest_goblin = Goblin('Forest Goblin')
# print(forest_goblin)




def make_warrior():
    create_warrior = Warrior(enter_player_name())
    print(create_warrior)
    return create_warrior


def make_mage():
    create_mage = Mage(enter_player_name())
    print(create_mage)
    return create_mage


def make_rogue():
    create_rogue = Rogue(enter_player_name())
    print(create_rogue)
    return create_rogue


# class CreateClass:
#     def make_warrior(self):
#         create_warrior = Warrior(enter_player_name())
#         print(self.create_warrior)
#         return self.create_warrior
#
#
#     def make_mage(self):
#         create_mage = Mage(enter_player_name())
#         print(self.create_mage)
#         return self.create_mage
#
#     def make_rogue(self):
#         create_rogue = Rogue(enter_player_name())
#         print(self.make_rogue)
#         return self.make_rogue()


def choose_class():
    print("- Warrior\n- Mage\n- Rogue")
    which_class = input('Type in the class you\'d like to play as: \n').lower()
    if which_class == 'warrior':
        make_warrior()
    elif which_class == 'mage':
        make_mage()
    elif which_class == 'rogue':
        make_rogue()
    else:
        print("You need to choose")