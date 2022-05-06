from interfaces.IGold import IGold
from interfaces.ILeather import ILeather

from models.Characters.Monsters.Monster import Monster


class Whelp (Monster, IGold, ILeather):

    #
    # Constructeur
    #

    def __init__(self):
        super().__init__()
        self.__leather = self.dice4.roll()
        self.__gold = self.dice6.roll()

    #
    # Accesseurs & Mutateurs
    #

    @property
    def stamina(self):
        return super().stamina + 1

    @property
    def leather(self):
        return self.__leather

    @property
    def gold(self):
        return self.__gold
