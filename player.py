from inventory import Inventory
class Player:
    def __init__(self, hitpoints, weapon_damage, magicpoints):
        self.hitpoints = hitpoints
        self.max_hp = hitpoints
        self.max_mp = magicpoints
        self.weapon_damage = weapon_damage
        self.food = 0
        self.inventory = Inventory()