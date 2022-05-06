from models.Characters.Heros.Hero import Hero


class Dwarf (Hero):

    #
    # Constructeur
    #

    def __init__(self, name):
        super().__init__(name)

    #
    # Accesseurs & Mutateurs
    #

    @property
    def stamina(self):
        return super().stamina + 2
