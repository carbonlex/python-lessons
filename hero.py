class Hero():
    """" Class to Create Hero for Game"""
    def __init__(self, name, level, race):
        """"Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """Pring all parametrs of this Hero"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is " + self.race + " Health is " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level +=1
    def move(self):
        """Start moving hero"""
        print("Hero " + self.name + " start moving...")

class SuperHero(Hero):
    """Class to create SuperHero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100

    def makemagic(self):
        """Use magic"""
        self.__magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is: " + str(self.level) + " Race is " + self.race + " Health is " + str(self.health).title() +
        " Magic is: " + str(self.magic)).title()
        print(discription)