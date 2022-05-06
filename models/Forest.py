from models.Characters.Character import Character
from models.Tools.Dice import Dice

from models.Characters.Monsters.Orc import Orc
from models.Characters.Monsters.Whelp import Whelp
from models.Characters.Monsters.Wolf import Wolf

from models.Characters.Heros.Hero import Hero
from models.Characters.Monsters.Monster import Monster


class Forest:

    #
    # Constructeur
    #

    def __init__(self, name : str, hero: Hero):
        self.__name = name
        self.__hero = hero

        self.__monster = None
        self.__nb_won_fights = 0
        self.__is_game_over = False

        self.__monster_dice = Dice(3)

    #
    # Accesseurs & Mutateurs
    #

    @property
    def name(self):
        return self.__name

    @property
    def hero(self):
        return self.__hero

    @property
    def monster(self):
        return self.__monster

    @property
    def nb_won_fights(self):
        return self.__nb_won_fights

    @property
    def is_game_over(self):
        return self.__is_game_over

    #
    # Méthodes
    #

    def start(self):
        self.__monster = self.generate_monster()
        character_turn = True


        while not self.is_game_over:

            if character_turn:
                self.hero.hit(self.monster)
                if self.monster.hp <= 0: self.die(self.monster)

            else:
                self.monster.hit(self.hero)
                if self.hero.hp <= 0: self.die(self.hero)

            character_turn = not character_turn

    def generate_monster(self):
        monster = None
        monster_roll = self.__monster_dice.roll()

        if monster_roll == 1:
            monster = Wolf()

        elif monster_roll == 2:
            monster = Orc()

        else:
            monster = Whelp()

        print("Nous rencontrons un monstre : ")
        print(monster)
        
        input("\nAppuyez sur une touche pour lancer le prochain combat...\n")
        
        print("\n~~~ Lancement du combat ~~~\n")

        return monster

    def die(self, character: Character):
    
        print("\n~~~ Fin du combat ~~~\n")

        if isinstance(character, Hero):
            self.__is_game_over = True

            print(f"{character.name} est mort.")
            print(f"{self.hero.name} a gagné {self.nb_won_fights} combat(s)")
            print(f"{self.hero.name} a accumulé {self.hero.gold}x or")
            print(f"{self.hero.name} a accumulé {self.hero.leather}x cuir")

        else:
            self.__nb_won_fights += 1
            print(f"{character.__class__.__name__} est mort.")
            self.hero.repose()
            self.hero.loot(character)

            self.__monster = self.generate_monster()
