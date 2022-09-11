import random  # tarvitaan random modulea kun arvotaan metsän kuvaustekstit
import sys
import colorama
import monsterGenerator
from player import Player
import os
def p(s, c):
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
    colorama.init()
    print(color[c] + s + reset)
def death(msg):
    p(f"""
                                 _____  _____
                                <     `/     |
                                 >          (
                                |   _     _  |
                                |  |_) | |_) |
                                |  | \\ | |   |
                                |            |
                 ______.______%_|            |__________  _____
               _/       {player_name.center(32," ")}\\|     |
              |         {msg.center(32," ")}       <
              |_____.-._________              ____/|___________|
                                |            |
                                |            |
                                |            |
                                |            |
                                |   _        <
                                |__/         |
                                 / `--.      |
                               %|            |%
                           |/.%%|          -< @%%%
                           `\\%`@|     v      |@@%@%%    - mfj
                         .%%%@@@|%    |    % @@@%%@%%%%
                    _.%%%%%%@@@@@@%%_/%\\_%@@%%@@@@@@@%%%%%%
    """, "magenta")

    # input("Press enter to continue.")



player = Player(hitpoints=30, weapon_damage=1, magicpoints=0)

############################################################################
# Intro
############################################################################
p(r"""
      _     ___       _  _   _
|\/| |_ |_|  |  /_\  |_ |_) |_ |   |
|  | |_ | |  | /   \ |_ |   |_ |__ |
""", "red")
player_name = input("Your name? ")  # kysyy pelaajan nimen pelin alussa
print(f"Welcome {player_name}")  # toivottaa pelaajan tervetulleeksi

############################################################################
# 1. Woods
############################################################################
def woods():
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
            death("Too fat to sit on branches")
            return False
        elif action == "2":  # myös pelin loppuun johtava haara
            print("You were heard, but not by humans. Your screams echoes in the woods as you're being eaten alive.")
            death("Lambs should stay quiet")
            return False
        elif action == "3":  # jos käyttäjän valitsema action on 3, peli jatkuu
            print("You find a candy bar and ripped piece of a map.")
            return True
        else:  # jos käyttäjän valinta ei osu mihinkään vaihtoehdoista tulostetaan herjaus, ja kysytään uudestaan
            print("Trying to cheat, eh?")

############################################################################
# 2. Lost
############################################################################
def lost():
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
    woods_hints = [
        "Go Nami?",
        "Gonami?",
        "Sounds kinda like Konami?",
        "Maybe a code related to Konami?",
        "Up, up, down, down, left, right, left, right, B, A.",
        "Maybe I should translate them into compass directions?"]
    woods_hints.reverse()
    turns_used = 0
    while action != "nnsswewe":  # toistetaan kunnes pelaaja on syöttänyt oikea suunnat
        turns_used += 1
        if turns_used % 10 == 0:
            if len(woods_hints) == 0:
                print("You starved to death.")
                death("Couldn't navigate.")
                return False
            p(woods_hints.pop(), "green")
        p(random.choice(woods_description), "yellow")  # tulostaa satunnaisen kuvaus tekstin
        print("You arrive at another crossroad.")
        action = action + input("What direction will you go?(n, s, w, e)")  # action stringin perään laitetaan uusi suunta
        action = action[-8:]  # action saa arvon actionin kahdeksan viimeistä merkkiä
    print("You found the way out of the woods.")
    return True
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
            p("Sucker! You are too slow!", "bwhite")
        elif str.lower(action) == "e":
            if player.food > 0:
                p("Such deliciousness. You regain 5HP.", "cyan")
                player.hitpoints += 5
            else:
                p("You already ate it all!", "cyan")
        else:
            p(f"You attack the {monster_name} in front of you", "red")
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
        p(f"The {monster_name} attacks!", "red")
        roll = random.randint(1, 20)
        if roll > 14:
            print(f"The {monster_name} hits you.")
            damage = random.randint(1, 6)
            print(f"You take {damage} damage")
            player.hitpoints = player.hitpoints - damage
            if player.hitpoints <= 0:
                if monster["type"] == "monster":
                    p("Bwahaha. Nice trip to the guts.", "red")
                    death("Became monster food")
                    return False
                p("You got your ass kicked.", "red")
                death("Sucked at fighting")
                return False
        else:
            print(f"The {monster_name} misses.")
    p(f"You have successfully slain the {monster_name}.", "red")
    return True

def tappelu():
    print(f"As you exit the woods a funky looking creature cuts your path.")
    # print(f"{monster_art}")
    player.weapon_damage = 4
    print(f"You pick the nearest stick (1d{player.weapon_damage}) you can find as your weapon.")
    return fight(monsterGenerator.generate_monster(max_hp=10, max_dmg=15), player)




##############################################################
# 4. A cabin
##############################################################
def cabin():
    print("As you continue the path away from the woods you stumble upon a small cabin")
    action = input("What will you do? (G)o in or (C)ontinue your way. ")
    if str.lower(action) == "c":
        print("You are dragged in to the darkness.")
        death("What an idiot")
        return False
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
                fight_result = fight(monsterGenerator.generate_monster(max_hp=10, max_dmg=15), player)
                if not fight_result:
                    return False
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
            p(
                "You step back outside. Suddenly you hear a loud crack and just when you realize it comes from your own skull, everything goes dark.", "bwhite")
            input("Press enter to continue.")
            return True
#################################
# 5. Jail time
#################################
def jail():
    print("You wake up to distant dripping sound. Looking around you notice you are being held in an old musty dungeon.")
    while True:
        choice = input("What will you do? ")
        words = choice.split(" ")
        if words[0] in ["search", "look", "seek"]:
            if len(words) <2:
                p("You look around and see some loose stones, barred window and hear distant snores. The wooden door with small latch shines small amount of light inside.", "bwhite")
                continue
            if words[1] in ["window", "bars"]:
                p("The bars feel very strong. No escape through here.", "bwhite")
            elif words[1] in ["door", "latch"]:
                p("The door seems to be old and slightly rotten. With right tools you might be able to break through.", "bwhite")
        if words[0] in ["take", "get", "pick"]:
            if len(words) < 2:
                p("Take what?", "bwhite")
                continue
            if words[1] in ["stone", "rock", "pebble"]:
                p("You put a stone in your pocket.", "bwhite")
                player.inventory.add_item("stone")
        if choice in ["pockets", "inventory", "items"]:
            player.inventory.print_inventory()
    return True
def main():
    if not woods():
        return
    if not lost():
        return
    if not tappelu():
        return
    if not cabin():
        return
    if not jail():
        return

while True:
    main()
    a = input("Restart game? (Y/n)")
    if a.lower() == "n":
        exit(0)