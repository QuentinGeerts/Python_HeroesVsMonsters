from abc import ABC

from models.Tools.Dice import Dice


class Character (ABC):

    #
    # Constructeur
    #

    def __init__(self):
        self.__dice4 = Dice(4)
        self.__dice6 = Dice(6)

        self.__stamina = self.__generate_stats()
        self.__strength = self.__generate_stats()
        self.__hp = self.reset_hp()

    #
    # Accesseur & Mutateurs
    #

    @property
    def stamina(self):
        return self.__stamina

    @property
    def strength(self):
        return self.__strength

    @property
    def hp(self):
        return self.__hp

    @property
    def dice4(self):
        return self.__dice4

    @property
    def dice6(self):
        return self.__dice6

    def reset_hp(self):
        self.__hp = self.stamina + self.__modifier(self.stamina)
        return self.__hp

    #
    # Méthodes
    #

    def __generate_stats(self):
        total = 0
        nb_des = 4
        stats = []

        for i in range(nb_des):
            stats.append(self.dice6.roll())

        stats.sort()
        stats.pop(0)

        for value in stats:
            total += value

        return total

    def __modifier(self, value):
        return -1 if value < 5 else 0 if value < 10 else 1 if value < 15 else 2

    def hit(self, target):
        if not isinstance(target, Character):
            raise TypeError("La cible n'est pas un personnage")

        damage = self.dice4.roll() + self.__modifier(self.strength)

        print(f"{self.__class__.__name__} frappe {target.__class__.__name__} et lui inflige {damage} points de dégâts.")

        target.__hp -= damage

    #
    # Redéfinition des méthodes
    #

    def __str__(self):
        return f"\n" \
            + f"{self.__class__.__name__}\n" \
            + f" - Force : {self.strength}\n" \
            + f" - Endurance : {self.stamina}\n" \
            + f" - PV : {self.hp}\n" \
            + f"\n"
