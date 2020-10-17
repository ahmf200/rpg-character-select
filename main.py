from customTemplates import characterTemplate, itemTemplate


# def choose_class():
#     which_class = input('Type in the class you\'d like to play as: \n').lower()
#     if which_class == 'warrior':
#         characterTemplate.make_warrior()
#     elif which_class == 'mage':
#         characterTemplate.make_mage()
#     elif which_class == 'rogue':
#         characterTemplate.make_rogue()

def inven():
    linen_cloth = itemTemplate.Item('Linen Cloth', 'This might be useful for bandages and light armour.', '5')
    inventory = []
    inventory.append(linen_cloth.name)
    print("This is what's in my inventory: \n{}".format(inventory))


def main():
    characterTemplate.choose_class()


if __name__ == '__main__':
    main()
