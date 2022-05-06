from interfaces.ILeather import ILeather
from interfaces.IGold import IGold

from models.Characters.Character import Character


class Monster (Character):

    #
    # Constructeur
    #

    def __init__(self):
        super().__init__()

    #
    # Accesseurs & Mutateurs
    #

    #
    # Méthodes
    #

    #
    # Redéfinition de méthodes
    #

    def __str__(self):
        return super().__str__() \
            + f"Inventaire :\n" \
            + f" ~ {self.leather}x cuir" if isinstance(self, ILeather) else "" \
            + f" ~ {self.gold}x or" if isinstance(self, IGold) else "" \
            + f"\n"

        # str = super().__str__() + f"Inventaire :\n"

        # if isinstance(self, ILeather): str += f" ~ {self.leather}x cuir"

        # if isinstance(self, ILeather) and isinstance(self, IGold): str += "\n"

        # if isinstance(self, IGold): str += f" ~ {self.gold}x or"

        # str += "\n"

        # return str
