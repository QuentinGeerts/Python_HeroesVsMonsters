from interfaces.ILeather import ILeather

from models.Characters.Monsters.Monster import Monster


class Wolf (Monster, ILeather):

    #
    # Constructeur
    #

    def __init__(self):
        super().__init__()
        self.__leather = self.dice4.roll()

    #
    # Accesseurs & Mutateurs
    #

    @property
    def leather(self):
        return self.__leather
