import random  # tarvitaan random modulea kun arvotaan metsän kuvaustekstit
import monsterGenerator
from player import Player

player = Player(hitpoints=30, weapon_damage=1)

############################################################################
# Intro
############################################################################

player_name = input("Your name? ")  # kysyy pelaajan nimen pelin alussa
print(f"Welcome {player_name}")  # toivottaa pelaajan tervetulleeksi

############################################################################
# 1. Woods
############################################################################

print(
    f"""
You are in the middle of the woods. You don't know how did you even get there.
1. Climb the nearest tree
2. Yell for help
3. Check your pockets
"""  # tulostaa pelin ensimmäisen tilanteen ja antaa toimintavaihtoehdot
)
action = ""  # alustetaan action-muuttuja
while action != "1" and action != "2" and action != "3":  # toistetaan kunnes arvo on 1, 2 tai 3
    action = input("What do you do? ")  # tallentaa actioniin käyttäjän syötteen
    if action == "1":  # jos käyttäjän valitsema action on 1, niin peli loppuu
        print("The branch you stepped on snaps and you died.")
        exit(0)  # lopettaa pelin
    elif action == "2":  # myös pelin loppuun johtava haara
        print("You were heard, but not by humans. Your screams echoes in the woods as you're being eaten alive.")
        exit(0)
    elif action == "3":  # jos käyttäjän valitsema action on 3, peli jatkuu
        print("You find a candy bar and ripped piece of a map.")
    else:  # jos käyttäjän valinta ei osu mihinkään vaihtoehdoista tulostetaan herjaus, ja kysytään uudestaan
        print("Trying to cheat, eh?")

############################################################################
# 2. Lost
############################################################################

print(f"""You eat the candy bar and take the map piece to your hands. It seems to lead
you towards crossroads. The candy wrapper informs you that to get out of the woods you have to go Nami.
""")
action = ""
# tehdään lista kuvaustekstejä, joista myöhemmin pomitaan satunnaisesti joku
woods_description = ["You feel the hairs on your neck stand up with every step further.",
                     "You step on something slimy, but dare not to look what exactly it is.",
                     "Cauldron of bats fly over you, almost touching your hair.",
                     "You hear a distant growl, but it doesn't sound like any animal to you.",
                     "A murder of crows take off in an distance. Did something spook them?"]
while action != "nnsswewe":  # toistetaan kunnes pelaaja on syöttänyt oikea suunnat
    print(random.choice(woods_description))  # tulostaa satunnaisen kuvaus tekstin
    print("You arrive at another crossroad.")
    action = action + input("What direction will you go?(n, s, w, e)")  # action stringin perään laitetaan uusi suunta
    action = action[-8:]  # action saa arvon actionin kahdeksan viimeistä merkkiä
print("You found the way out of the woods.")  # the end

############################################################################
# 3. FIGHT!
############################################################################

# taistelussa tarvitaan
# 1. aseet
#   - to_hit, damage
# 2. vihollinen
#   - HP
# 3. pelaajan hitarit
# 4. kenen vuoro
# 5. kuinka monta vuoroa on kulunut

# enemy_hitpoints = 10
# monster_art = f"""
#    SHRIMP ENERGY!
#       \/0~0\/
#       /( V )\\
#         | |
#     X~~/   \~~X
#        | , |
#        d   b
# """


print(f"As you exit the woods a funky looking creature cuts your path.")
# print(f"{monster_art}")
player.weapon_damage = 4
print(f"You pick the nearest stick (1d{player.weapon_damage}) you can find as your weapon.")


def fight(monster, player):
    turn_counter = 0
    monster_name = monster["name"]
    enemy_hitpoints = monster["hp"]
    enemy_max_hp = enemy_hitpoints
    while True:
        turn_counter = turn_counter + 1
        print(
            f"\n*** Turn {turn_counter}, You: {player.hitpoints}/{player.max_hp} hp, {monster_name}:{enemy_hitpoints}/{enemy_max_hp} hp ***")
        ### player turn
        action = input("What will you do? (A)ttack, (R)un or (E)at. ")
        if str.lower(action) == "r":
            print("Sucker! You are too slow!")
        elif str.lower(action) == "e":
            if player.food > 0:
                print("Such deliciousness. You regain 5HP.")
                player.hitpoints += 5
            else:
                print("You already ate it all!")
        else:
            print(f"You attack the {monster_name} in front of you")
            roll = random.randint(1, 20)
            if roll > 10:
                print("You managed to hit!")
                damage = random.randint(1, player.weapon_damage)
                print(f"You deal {damage} damage")
                enemy_hitpoints = enemy_hitpoints - damage
                if enemy_hitpoints <= 0:
                    break
            else:
                print("You miss.")

        ### enemy turn
        print(f"The {monster_name} attacks!")
        roll = random.randint(1, 20)
        if roll > 14:
            print(f"The {monster_name} hits you.")
            damage = random.randint(1, 6)
            print(f"You take {damage} damage")
            player.hitpoints = player.hitpoints - damage
            if player.hitpoints <= 0:
                print("Bwahaha. Nice trip to the guts.")
                exit(0)
        else:
            print(f"The {monster_name} misses.")
    print(f"You have successfully slain the {monster_name}.")


fight(monsterGenerator.generate_monster(max_hp=10, max_dmg=15), player)
##############################################################
# 4. A cabin
##############################################################

print("As you continue the path away from the woods you stumble upon a small cabin")
action = input("What will you do? (G)o in or (C)ontinue your way. ")
if str.lower(action) == "c":
    print("You are dragged in to the darkness.")
    exit(0)
else:
    print("You find yourself in a small entrance with three doors.")
action = ""
cabin_rooms_explored = [False, False, False]
while action != "e":
    action = input("Where will you go? (l)eft, (f)orward, (r)ight, (e)xit ")
    if action == "l":
        if cabin_rooms_explored[0] is False:
            print("You found a knife and replace your stick with it.")
            player.weapon_damage = 5
            print("You go back to the entrance.")
            cabin_rooms_explored[0] = True
        else:
            print("You have already looked inside.")
    if action == "f":
        if cabin_rooms_explored[1] is False:
            print("You stumble upon a monster!")
            fight(monsterGenerator.generate_monster(max_hp=10, max_dmg=15), player)
            print("You go back to the entrance.")
            cabin_rooms_explored[1] = True
        else:
            print("You have already looked inside.")
    if action == "r":
        if cabin_rooms_explored[2] is False:
            print("You found food!")
            player.food += 1
            print("You go back to the entrance.")
            cabin_rooms_explored[2] = True
        else:
            print("You have already looked inside.")
    if action == "e":
        print("You step back outside. Suddenly you hear a loud crack and just when you realize it comes from your own skull, everything goes dark.")
        input("Press enter to continue.")
#################################
# 5. Jail time
#################################