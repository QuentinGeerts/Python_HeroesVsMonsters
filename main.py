from models.Forest import Forest
from models.Characters.Heros.Human import Human
from models.Characters.Heros.Dwarf import Dwarf

#
# Variables
#

choice = ""

print("~~~ Heroes vs Monster ~~~")

#
# Création du personnage
#

name = input("Quel est ton pseudo : ")

print("Sélection de la classe : ")
print("1. Humain")
print("2. Nain")
while choice != "1" and choice != "2":
    choice = input("Choix : ")
    if choice != "1" and choice != "2":
        print("Erreur...")

my_hero = Human(name) if choice == "1" else Dwarf(name)

print(my_hero)

#
# Création de la forêt
#

shorewood = Forest("Shorewood", my_hero)
shorewood.start()

print("~~~ Fin de la partie ~~~")
