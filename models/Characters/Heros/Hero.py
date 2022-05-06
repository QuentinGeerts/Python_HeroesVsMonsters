from interfaces.IGold import IGold
from interfaces.ILeather import ILeather

from models.Characters.Character import Character
from models.Characters.Monsters.Monster import Monster
from models.Characters.Monsters.Orc import Orc
from models.Characters.Monsters.Whelp import Whelp
from models.Characters.Monsters.Wolf import Wolf


class Hero (Character, ILeather, IGold):

    #
    # Constructeur
    #

    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__gold = 0
        self.__leather = 0
    #
    # Accesseurs & Mutateurs
    #

    @property
    def name(self):
        return self.__name

    @property
    def gold(self):
        return self.__gold

    @property
    def leather(self):
        return self.__leather

    #
    # Méthodes
    #

    def repose(self):
        self.reset_hp()

    def loot(self, target : Monster):

        print("")
        
        if isinstance(target, ILeather):
            self.__leather += target.leather
            print(f"[Dépouille] : {self.name} a gagné {target.leather}x cuir")

        if isinstance(target, IGold):
            self.__gold += target.gold
            print(f"[Dépouille] : {self.name} a gagné {target.gold}x or")

        print("")

    #
    # Redéfinition de méthodes
    #

    def __str__(self):
        return f"\nNom : {self.__name}" \
            + super().__str__()
