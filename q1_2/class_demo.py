class Felidae:

    def __init__(self, name, species, color):
        """
        Initialize a Felidae object
        :param name: the name of the animal
        :param species: the species of the animal
        :param color: the color of the animal
        """
        self.name = name
        self.species = species
        self.color = color

    @classmethod
    def from_string(cls, string):
        """
        This method will not be implemented in Felidae class
        :param string:
        :return:
        """
        raise NotImplementedError

    def get_info(self):
        """
        This method will not be implemented in Felidae class
        :return:
        """
        raise NotImplementedError


class Cat(Felidae):

    def __init__(self, name, color, fav_food, fav_toy, species='cat'):
        super(Cat, self).__init__(name, species, color)
        self.fav_food = fav_food
        self.fav_toy = fav_toy

    @classmethod
    def from_string(cls, string):
        """
        Create a new Cat object from a string
        :param string: the string with the information of the cat
        :return:
        """
        name, color, fav_food, fav_toy = string.split(',')
        return cls(name, color, fav_food, fav_toy)

    def get_info(self):
        """
        Return a string with the information of the cat
        :return: a string with the information of the cat
        """
        return "This Felidae is a {} named {}. It's fur is {}. " \
               "Want to win it's heart? " \
               "Bring some {} and a new {}.".format(self.species,
                                                    self.name,
                                                    self.color,
                                                    self.fav_food,
                                                    self.fav_toy)
