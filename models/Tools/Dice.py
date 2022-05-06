from random import randint


class Dice:

    #
    # Constructeur
    #

    def __init__(self, max):
        self.__min = 1
        self.__max = max
    #
    # Accesseurs - Lecture seule
    #

    @property
    def min(self):
        return self.__min

    @property
    def max(self):
        return self.__max

    #
    # Méthodes
    #

    def roll(self):
        return randint(self.min, self.max)


if __name__ == '__main__':

    de = Dice(6)
    print(de.roll())
