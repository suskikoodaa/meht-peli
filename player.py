from inventory import Inventory
from enum import Enum


class Player:
    def __init__(self, hitpoints, weapon_damage, magicpoints):
        self.hitpoints = hitpoints
        self.max_hp = hitpoints
        self.max_mp = magicpoints
        self.weapon_damage = weapon_damage
        self.food = 0
        self.inventory = Inventory()
        self.weapon = None

class WeaponType(Enum):
    STICK = "stick"
    STONE = "stone"
    KNIFE = "knife"
    DAGGER = "dagger"
    SWORD = "sword"
    LONG_SWORD = "long sword"
    BATTLE_AXE = "battle axe"
    CLUB = "club"
    CROSSBOW = "crossbow"
    DILDO_BAZOOKA = "dildo bazooka"


class SpecialEffect(Enum):
    BLEED = "bleed"
    SLOW = "slow"
    STUN = "stun"


class Weapon:

    def __init__(self, min_dmg, max_dmg, weapon_type, to_hit, special_effect=None, proc=0):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.weapon_type = weapon_type
        self.special_effect = special_effect
        self.proc = proc
        self.to_hit = to_hit