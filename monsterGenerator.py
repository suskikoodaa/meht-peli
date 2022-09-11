import random
import colorama
color = {
        "black": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m",
        "bwhite": "\u001b[37;1m"
    }
reset = "\u001b[0m"
# print(f"Shrimpie {random.randint(1, 5)}")

shrimpie = f"""{color["blue"]}
   SHRIMP ENERGY!
      \/0~0\/
      /( V )\\
        | |
    X~~/   \~~X
       | , |
       d   b
{reset}"""

katamari = f"""{color["green"]}
I'LL SHOW YOU A SANDWICH!
       /_ _\\ 
      /( * )\\
         |     /
    O~~/   \~~O
       |___|
       q   p
{reset}"""

glutare = f"""{color["magenta"]}
   CHECK MY GLUTES!
       ^@^@^ 
        *w*  
        / \\    
     3-( X )-E
       (___)
       q   p
{reset}"""

mr_stick = f"""{color["yellow"]}
   I'MMA POKE YOU!
        . .
         U  
         |    
      x--|--x
         |
        / \\
{reset}"""
monster_list = []
monster_list.append(shrimpie)
monster_list.append(katamari)
monster_list.append(glutare)
monster_list.append(mr_stick)

monster_name_list = ["ur", "bal", "mur", "bör", "kra", "blä"]


# print(monster_list[0].split("\n")[2])


def generate_monster(max_hp, max_dmg):
    # randomise hp and damage
    monster_hp = random.randint(10, max_hp)
    monster_max_dmg = random.randint(3, max_dmg)

    # make a random monster portrait
    for i in range(0, 9):
        print(monster_list[random.randint(0, len(monster_list) - 1)].split("\n")[i])

    # generate random monster name
    monster_name = "-".join(random.choices(monster_name_list, k=random.randint(3,6)))
    stats = {
        "hp": monster_hp,
        "damage": monster_max_dmg,
        "name": monster_name,
        "type": "monster"
    }
    return stats


# print(generate_monster(max_hp=30, max_dmg=10))
