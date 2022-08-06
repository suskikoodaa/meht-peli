import random  # tarvitaan random modulea kun arvotaan metsän kuvaustekstit

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

player_hitpoints = 30
player_max_hp = player_hitpoints
enemy_hitpoints = 10
enemy_max_hp = enemy_hitpoints
stick_damage = 4
turn_counter = 0
monster_art = f"""
   SHRIMP ENERGY!
      \/0~0\/
      /( V )\\
        | |
    X~~/   \~~X
       | , |
       d   b
"""

print(f"As you exit the woods a funky looking creature cuts your path.")
print(f"{monster_art}")
print(f"You pick the nearest stick (1d{stick_damage}) you can find as your weapon.")
while enemy_hitpoints > 0:
    turn_counter = turn_counter + 1
    print(
        f"\n*** Turn {turn_counter}, You: {player_hitpoints}/{player_max_hp} hp, Enemy:{enemy_hitpoints}/{enemy_max_hp} hp ***")
    ### player turn
    action = input("What will you do? (A)ttack or (R)un ")
    if str.lower(action) == "r":
        print("Sucker! You are too slow!")
    else:
        print("You attack the creature in front of you")
        roll = random.randint(1, 20)
        if roll > 10:
            print("You managed to hit!")
            damage = random.randint(1, stick_damage)
            print(f"You deal {damage} damage")
            enemy_hitpoints = enemy_hitpoints - damage
            if enemy_hitpoints <= 0:
                break
        else:
            print("You miss.")

    ### enemy turn
    print("The creature attacks!")
    roll = random.randint(1, 20)
    if roll > 14:
        print("The creature hits you.")
        damage = random.randint(1, 6)
        print(f"You take {damage} damage")
        player_hitpoints = player_hitpoints - damage
        if player_hitpoints <= 0:
            print("Bwahaha. Nice trip to the guts.")
            exit(0)
    else:
        print("The creature misses.")
print("You have successfully slain the creature.")

##############################################################
# 4. A gabin
##############################################################