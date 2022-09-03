class Player:
    def __init__(self, hitpoints, weapon_damage):
        self.hitpoints = hitpoints
        self.max_hp = hitpoints
        self.weapon_damage = weapon_damage
        self.food = 0