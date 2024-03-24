
from random import randint

def update_score(score, die_value):
    if die_value == 1:
        return 0 
    else:
        return score + die_value

def display_scoreboard(player_score, opponent_score):
    print()
    print("#" * 20)
    print(f"Spēlētāja rezultāts: {player_score}")
    print(f"Pretinieka rezultāts: {opponent_score}")
    print("#" * 20)
    print()

def print_with_effects(text, effects):
    effect_string = "\033[" + ";".join(map(str, effects)) + "m"
    reset_string = "\033[0m"
    print(effect_string + text + reset_string)

intro_message = """
       Laipni lūdzam 'Cūka', kauliņu spēlē!
   
     Šajā spēlē lietotājs un pretinieks
     metīs 6-pusēju kauliņu katrā kārtā. Ja vērtība
     kauliņš ir 1, spēlētājs, kurš uzmetīs 1, zaudē
     visus viņa punktus. Pretējā gadījumā spēlētājs saņem
     to punktu pievienoto kauliņa vērtība. Pirmais
     spēlētājs, kurš sasniedz 30 punktus, uzvar!
"""
print(intro_message)
username = input("Kā tevi sauc? ")

player_score = 0
opponent_score = 0

while True:
    input(f"Uzspied 'Enter' lai mestu kauliņu {username}!\n")
    player_roll = randint(1, 6)
    print_with_effects(f"{username} uzmet {player_roll}", [33])  

    opponent_roll = randint(1, 6)
    print(f"Pretinieks uzmet {opponent_roll}")

    player_score = update_score(player_score, player_roll)
    opponent_score = update_score(opponent_score, opponent_roll)

    display_scoreboard(player_score, opponent_score)
    
    if player_score >= 30:
        print_with_effects(f"{username} uzvar!👑", [1, 35, 4])  
        break
    elif opponent_score >= 30:
        print_with_effects("Pretinieks uzvar!👑", [1, 35, 4])  
        break

