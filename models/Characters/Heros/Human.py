from models.Characters.Heros.Hero import Hero


class Human (Hero):

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
        return super().stamina + 1

    @property
    def strength(self):
        return super().strength + 1
