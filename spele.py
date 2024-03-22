
def update_score(rezultāts,die_value ):
 if die_value == 1:
        return randint
 else:
        return rezultāts + die_value

Spēlētāja_rezultāts = 0
Pretinieka_rezultāts = 0
from random import randint
def display_scoreboard(Spēlētāja_rezultāts, Pretinieka_rezultāts):
    print()
    print("#" * 20)
    print(f"Spēlētja rezultāts: {Spēlētāja_rezultāts}")
    print(f"Pretinieka rezultāts: {Pretinieka_rezultāts}")
    print("#" * 20)
    print()
uzruna = """
       Laipni lūdzam 'Cūka', kauliņu spēlē!
   
     Šajā spēlē lietotājs un pretinieks
     metīs 6-pusēju kauliņu katrā kārtā. Ja vērtība
     kauliņš ir 1, spēlētājs, kurš uzmetīs 1, zaudē
     visus viņa punktus. Pretējā gadījumā spēlētājs saņem
     to punktu pievienoto kauliņa vērtība. Pirmais
     spēlētājs, kurš sasniedz 30 punktus, uzvar!
"""
print(uzruna)
username = input("Kā tevi sauc? ")


while True:
    input(f"Uzspied 'Enter' lai mestu kauliņu {username}!\n")
    spēlētājs = randint(1, 6)
    print(f"{username} uzmet {spēlētājs}")

    dators = randint(1, 6)
    print(f"Pretinieks uzmet {dators}")
    Spēlētāja_rezultāts = update_score(Spēlētāja_rezultāts, spēlētājs)
    Pretinieka_rezultāts = update_score(Pretinieka_rezultāts, dators)
    display_scoreboard(Spēlētāja_rezultāts, Pretinieka_rezultāts)
    
    if Spēlētāja_rezultāts >= 30:
        print(f"{username} uzvar!👑")
        break
    elif Pretinieka_rezultāts >= 30:
        print("Pretinieks uzvar!👑")
        break    
