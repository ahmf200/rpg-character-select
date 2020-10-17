class Item:
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "\n{}\n=====\nDescription: {}\nValue: {} gold coins\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage, damageType):
        self.damage = damage
        self.damageType = damageType
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nType: {}\n".format(self.name, self.description, self.value, self.damage, self.damageType)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)

# def get_item(item):
#     test = item(Item())

# linen_cloth = Item('Linen Cloth', 'This might be useful for bandages and light armour.', '5')
# print(linen_cloth)
#
#
# wooden_sword = Weapon('Wooden Sword', "Doesn't post much of a threat.", 10, 5, 'Phyiscal')
# print(wooden_sword)
