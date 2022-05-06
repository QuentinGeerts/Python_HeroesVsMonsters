from interfaces.IGold import IGold

from models.Characters.Monsters.Monster import Monster


class Orc (Monster, IGold):

    #
    # Constructeur
    #

    def __init__(self):
        super().__init__()
        self.__gold = self.dice6.roll()

    #
    # Accesseurs & Mutateurs
    #

    @property
    def strength(self):
        return super().strength + 1

    @property
    def gold(self):
        return self.__gold
