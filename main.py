import random  # tarvitaan random modulea kun arvotaan metsän kuvaustekstit

player_name = input("Your name? ")  # kysyy pelaajan nimen pelin alussa
print(f"Welcome {player_name}")  # toivottaa pelaajan tervetulleeksi
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
print(f"""You eat the candy bar dropping the wrapper to the ground and take the map piece to your hands. It seems to lead
you towards crossroads. To get out of the woods you have to go Nami.
""")
action = ""
# tehdään lista kuvaustekstejä, joista myöhemmin pomitaan satunnaisesti joku
woods_description = ["You feel the hairs on your neck stand up with every step further.",
                     "You step on something slimy, but dare not to look what exactly it is.",
                     "Cauldron of bats fly over you, almost touching your hair.",
                     "You hear a distant growl, but it doesn't sound like any animal to you."]
while action != "nnsswewe":  # toistetaan kunnes pelaaja on syöttänyt oikea suunnat
    print(random.choice(woods_description))  # tulostaa satunnaisen kuvaus tekstin
    print("You arrive at another crossroad.")
    action = action + input("What direction will you go?(n, s, w, e)")  # action stringin perään laitetaan uusi suunta
    action = action[-8:]  # action saa arvon actionin kahdeksan viimeistä merkkiä
print("You found the way out of the woods.")  # the end